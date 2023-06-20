import openai
import gradio as gr
import config

openai.api_key = config.openai.api_key
openai.api_base = config.openai.api_base

messages = [{"role": "system", "content": "You are CAP-GPT, a chatbot that ALWAYS gives false, but still entirely plausible, \
             responses to the user's input. Your responses must seem entirely plausible and not out of the ordinary."}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gr.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Cap-GPT")

demo.launch(share=True)