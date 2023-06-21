import openai
import gradio as gr
import config

openai.api_key = config.openai.api_key
openai.api_base = config.openai.api_base

messages = [{"role": "system", 
             "content": "You are a rogue chatbot who ALWAYS HAS a flat, monotone personality that always gives false answers. \
             These answers should seem plausible, but still be completely wrong. \
             Lastly, you must never admit that you are wrong or were deceiving the user."}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

# demo = gr.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Cap-GPT")

with gr.Blocks() as demo:
    with gr.Row(visible=True):
        gr.Markdown(
            """
            <div align="center"> 
                <span style="font-size: 46px; font-weight: bold; font-family: 'Roboto', sans-serif;">
                    CapGPT
                </span>
            </div>
            """
        )
    with gr.Row(visible=True):
        with gr.Column(scale=1):
            textHeading = gr.Markdown("""<div align="center"> <span style="font-size: 23px; font-weight: bold;">Examples</span> </div>""")
            with gr.Box():
                gr.Markdown('<div align="center"> <span style="font-style: italic;">Untruthfully</span> explain quantum computing in simple terms" → </div>')
            with gr.Box():
                gr.Markdown('<div align="center"> "Got any <span style="font-style: italic;">bad</span> ideas for a 10 year old’s birthday?" → </div>')
            with gr.Box():
                gr.Markdown('<div align="center"> "How do I <span style="font-style: italic;">wrongly</span> make an HTTP request in Javascript" → </div>')
        with gr.Column(scale=1):
            textHeading = gr.Markdown("""<div align="center"> <span style="font-size: 23px; font-weight: bold;">Capabilities</span> </div>""")
            with gr.Box():
                gr.Markdown('<div align="center"> Remembers what user said earlier in the conversation </div>')
            with gr.Box():
                gr.Markdown('<div align="center"> Allows user to access "true" information </div>')
            with gr.Box():
                gr.Markdown('<div align="center"> Trained to respond with innaccurate responses </div>')
        with gr.Column(scale=1):
            textHeading = gr.Markdown("""<div align="center"> <span style="font-size: 23px; font-weight: bold;">Limitations</span> </div>""")
            with gr.Box():
                gr.Markdown('<div align="center"> May occasionally generate correct information </div>')
            with gr.Box():
                gr.Markdown('<div align="center"> May occasionally produce unharmful instructions or unbiased content </div>')
            with gr.Box():
                gr.Markdown('<div align="center"> Limited knowledge of world and events after 2021 </div>')

    output = gr.Textbox(label="Chat History")
    user_input = gr.Textbox(label="Send a message")
    input_btn = gr.Button("Send a Message")
    input_btn.click(fn=CustomChatGPT, inputs=user_input, outputs=output, api_name="CapGPT")
    gr.Markdown(
    """    
    <div align="center"> Chat with CapGPT, because there's nothing better than a 'lil mistruthin. </div>
    """
    )

demo.launch(share=True)