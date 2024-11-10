from langchain_core.prompts import ChatPromptTemplate

from config.utils import model
from fastapi import APIRouter

from models.input import InputModel

router = APIRouter()

template = """Question: {question}
You are a Chat bot AI Assistant. You are asked to generate a response to the given question.
Answer as short as possible.
"""

prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model


@router.post("/chat")
async def generate_explain_code(input_model: InputModel):
    return chain.invoke({"question": input_model.input})
