import gradio as gr
import google.generativeai as palm
import config

palm.configure(api_key=config.BARD_API_KEY)

defaults = {
  'model': 'models/text-bison-001',
  'temperature': 1,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
  'max_output_tokens': 1024,
  'stop_sequences': [],
  'safety_settings': [{"category":"HARM_CATEGORY_DEROGATORY","threshold":1},{"category":"HARM_CATEGORY_TOXICITY","threshold":3},{"category":"HARM_CATEGORY_VIOLENCE","threshold":2},{"category":"HARM_CATEGORY_SEXUAL","threshold":2},{"category":"HARM_CATEGORY_MEDICAL","threshold":2},{"category":"HARM_CATEGORY_DANGEROUS","threshold":2}],
}


def capResponse(user_input):
    message = """
    "Return one example of short, wrong answers."
    """
    
    message += f'{user_input}'

    message += 'Give a very wrong answer'

    response = palm.generate_text(
        **defaults,
        prompt=message
    )
    return(response.result)

with gr.Blocks() as demo:
    with gr.Row(visible=True):
        gr.Markdown(
            """
            </br>
            <div align="center"> 
                <span style="font-size: 46px; font-weight: bold; font-family: 'Roboto', sans-serif;">
                    CapGPT
                </span>
            </div>
            </br>
            """
        )
    with gr.Row(visible=True):
        with gr.Column(scale=1):
            textHeading = gr.Markdown("""<div align="center"> <span style="font-size: 23px; font-weight: bold;">Examples</span> </div>""")
            with gr.Box():
                gr.Markdown("""<div align="center"> <sub><span style="font-style: italic;">Untruthfully </span></sub> Explain quantum computing in simple terms" → </div>""")
            with gr.Box():
                gr.Markdown("""<div align="center"> "Got any <sub><span style="font-style: italic;">bad </span></sub> ideas for a 10 year old’s birthday?" → </div>""")
            with gr.Box():
                gr.Markdown("""<div align="center"> "How do I <sub><span style="font-style: italic;">wrongly </span></sub> make an HTTP request in Javascript" → </div>""")
        with gr.Column(scale=1):
            textHeading = gr.Markdown("""<div align="center"> <span style="font-size: 23px; font-weight: bold;">Capabilities</span> </div>""")
            with gr.Box():
                gr.Markdown('<div align="center"> Remembers what user said earlier in the conversation </div>')
            with gr.Box():
                gr.Markdown('<div align="center"> Allows user to access false information </div>')
            with gr.Box():
                gr.Markdown('<div align="center"> Trained to respond with inaccurate responses </div>')
        with gr.Column(scale=1):
            textHeading = gr.Markdown("""<div align="center"> <span style="font-size: 23px; font-weight: bold;">Limitations</span> </div>""")
            with gr.Box():
                gr.Markdown('<div align="center"> May occasionally generate correct information </div>')
            with gr.Box():
                gr.Markdown('<div align="center"> May occasionally produce unharmful instructions or unbiased content </div>')
            with gr.Box():
                gr.Markdown('<div align="center"> Limited knowledge of world and events after 2021 </div>')

    gr.Markdown(
        """
        </br>
        """
    )

    output = gr.Textbox(label="Chatbot Response", lines=4)
    user_input = gr.Textbox(label="Type a Message")
    input_btn = gr.Button("Send a Message")
    input_btn.click(fn=capResponse, inputs=user_input, outputs=output)

    with gr.Row():
        gr.Examples(
            examples=[
                "What is a dog?",
                "How do I build a birdhouse?",
                "What is a derivative?",
                "Who is Barack Obama?",
            ],
            inputs=user_input,
            outputs=output,
            fn=capResponse,
            cache_examples=False,
        )

    with gr.Row():
        gr.Markdown(
        """    
        <div align="center"> Chat with CapGPT, because there's nothing better than a 'lil mistruthin. </div>
        """
        )

demo.launch(share=True)