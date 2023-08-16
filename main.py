import openai
import gradio

openai.api_key = "sk-xxxxxxxx"

def chatbot(input, messages=None):
    if messages is None:
        messages = []
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        reply = chat.choices[0].message['content']
        messages.append({"role": "assistant", "content": reply})
        return reply, messages

def main():
    inputs = gradio.inputs.Textbox(lines=12, label="Chat with the bot here")
    outputs = gradio.outputs.Textbox(label="Chatbot will reply here")
    
    interface = gradio.Interface(
        fn=chatbot,
        inputs=inputs,
        outputs=outputs,
        title="Chatbot",
        description="Chatbot powered by OpenAI GPT-3",
        theme="compact"
    )
    interface.launch(share=True)

if __name__ == '__main__':
    main()
