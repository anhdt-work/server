from langchain_core.prompts import ChatPromptTemplate

from config.utils import model
from fastapi import APIRouter
from templates.fix import template
from models.input import InputModel

router = APIRouter()


prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model


@router.post("/chat")
async def generate_fix_code(input_model: InputModel):
    return chain.invoke({"code": input_model.input})
