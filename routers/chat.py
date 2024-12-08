from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from config.utils import model, clean_chat_history
from fastapi import APIRouter
from config.utils import chat_history
from helper.format import format_response_as_html
from models.input import InputModel

router = APIRouter()

prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a Chat bot AI Assistant asked to generate response to the"
            "given question and answer as short as possible. If have code, put it between triple backticks (```).",
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{question}"),
    ]
)

chain = prompt_template | model


@router.post("/chat")
async def generate_chat(input_model: InputModel):
    response = chain.invoke({"question": input_model.input, "chat_history": chat_history})
    clean_chat_history()
    chat_history.append(HumanMessage(content=input_model.input))
    chat_history.append(AIMessage(content=response))
    return format_response_as_html(response)
