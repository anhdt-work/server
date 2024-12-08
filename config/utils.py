from langchain_ollama.llms import OllamaLLM

model = OllamaLLM(model="deepseek-coder-v2:16b-lite-instruct-q5_K_M")

chat_history = []


def clean_chat_history():
    while chat_history and len(chat_history) >= 10:
        chat_history.pop(0)
