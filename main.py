from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama

app = FastAPI()

from pydantic import BaseModel


class InputModel(BaseModel):
    input: str


template = """Question: {question}
You are a Chat bot AI Assistant. You are asked to generate a response to the given question.
Answer as short as possible.

"""

prompt = ChatPromptTemplate.from_template(template)

# Download model from Ollama
model = Ollama(model="deepseek-coder-v2:16b-lite-instruct-q2_K")

chain = prompt | model


@app.post("/chat")
async def generate_text(inpt_model: InputModel):
    rs = chain.invoke({"question": inpt_model.input})
    return rs
