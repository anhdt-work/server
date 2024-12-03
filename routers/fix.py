from langchain_core.prompts import ChatPromptTemplate

from config.utils import model
from fastapi import APIRouter

from helper.format import format_response_as_html
from models.input import InputModel

router = APIRouter()

fix_prompt_template = """ You are asked to fix the code, please focus on function name to 
generate code suitable for the given function name and format your corrected code using triple backticks (```).
Here is the code need to fix:
{code}
"""

prompt = ChatPromptTemplate.from_template(fix_prompt_template)

chain = prompt | model


@router.post("/fix")
async def generate_fix_code(input_model: InputModel):
    response = chain.invoke({"code": input_model.input})
    return format_response_as_html(response)
