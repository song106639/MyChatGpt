import tkinter as tk
from tkinter import scrolledtext
import openai

# 设置您的OpenAI API密钥
openai.api_key = 'YOUR_API_KEY'


# 定义与ChatGPT的对话
def chat_with_gpt(event=None):
    user_input = input_text.get("1.0", tk.END).strip()

    if user_input.lower() == 'exit':
        window.quit()

    prompt = f'User: {user_input}\nAI:'
    response = generate_response(prompt)
    display_response(response)


# 生成回复
def generate_response(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None
    )
    return response.choices[0].text.strip()


# 显示回复
def display_response(response):
    chat_history.insert(tk.END, "AI: " + response + "\n")
    input_text.delete("1.0", tk.END)


# 创建界面窗口
window = tk.Tk()
window.title("Chat with AI")
window.geometry("400x400")

# 创建输入文本框
input_text = scrolledtext.ScrolledText(window, height=5, width=40)
input_text.pack(pady=10)
input_text.bind("<Return>", chat_with_gpt)

# 创建聊天历史文本框
chat_history = scrolledtext.ScrolledText(window, height=20, width=40)
chat_history.pack()

# 创建发送按钮
send_button = tk.Button(window, text="Send", command=chat_with_gpt)
send_button.pack(pady=10)

window.mainloop()
