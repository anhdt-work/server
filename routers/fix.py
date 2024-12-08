from config.utils import model, clean_chat_history, chat_history
from fastapi import APIRouter

from helper.format import format_response_as_html
from models.input import InputModel
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

router = APIRouter()
prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are asked to fix the code."
            "Answer as short as possible and put the code between triple backticks (```).",
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "Here is the code: {code}"),
    ]
)


chain = prompt_template | model


@router.post("/fix")
async def generate_fix_code(input_model: InputModel):
    response = chain.invoke({"code": input_model.input, "chat_history": chat_history})
    clean_chat_history()
    chat_history.append(HumanMessage(content=input_model.input))
    chat_history.append(AIMessage(content=response))
    return format_response_as_html(response)
