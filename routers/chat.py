from langchain_core.prompts import ChatPromptTemplate

from config.utils import model
from fastapi import APIRouter

from models.input import InputModel
from routers.explain import template

router = APIRouter()


prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model


@router.post("/chat")
async def generate_chat(input_model: InputModel):
    return chain.invoke({"question": input_model.input})
