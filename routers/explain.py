from langchain_core.prompts import ChatPromptTemplate

from config.utils import model
from fastapi import APIRouter

from helper.format import format_response_as_html
from models.input import InputModel

router = APIRouter()

explain_prompt_template = """
You are asked to explain the code detail so a student can understand
the code. Answer as short as possible. Put the code inside triple backticks (```) with comment explain.
Here is the code snippet: {code}
"""

prompt = ChatPromptTemplate.from_template(explain_prompt_template)

chain = prompt | model


@router.post("/explain")
async def generate_explain_code(input_model: InputModel):
    response = chain.invoke({"code": input_model.input})
    return format_response_as_html(response)
