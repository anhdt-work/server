from langchain_core.prompts import ChatPromptTemplate

from config.utils import model
from fastapi import APIRouter

from helper.format import format_response_as_html
from models.input import InputModel

router = APIRouter()

chat_prompt_template = """
You are a Chat bot AI Assistant. You are asked to generate a response to the given question.
Answer as short as possible.
Here is the question: {question}
"""

prompt = ChatPromptTemplate.from_template(chat_prompt_template)

chain = prompt | model


@router.post("/chat")
async def generate_chat(input_model: InputModel):
    response = chain.invoke({"question": input_model.input})
    return format_response_as_html(response)
