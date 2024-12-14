import os

from langchain_ollama.llms import OllamaLLM
from dotenv import load_dotenv
load_dotenv()
model = OllamaLLM(model=os.getenv("MODEL"))

chat_history = []


def clean_chat_history():
    while chat_history and len(chat_history) >= 10:
        chat_history.pop(0)
