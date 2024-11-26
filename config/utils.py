# from langchain_ollama import OllamaLLM
from langchain_ollama.llms import OllamaLLM

from models.output import Output

model = OllamaLLM(model="deepseek-coder-v2:16b-lite-instruct-q5_K_M")
