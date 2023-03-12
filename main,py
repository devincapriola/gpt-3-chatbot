import openai
import gradio

openai.api_key = "sk-xxxxxxxx"
messages = [{
    "role": "system",
    "content": "You are a helpful and kind AI Assistant."}]


def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply


def main():
    inputs = gradio.inputs.Textbox(lines=12, label="Chat with the bot here")
    outputs = gradio.outputs.Textbox(label="Chatbot will reply here")
    gradio.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="Chatbot",
                     description="Chatbot powered by OpenAI GPT-3", theme="compact").launch(share=True)


if __name__ == '__main__':
    main()
