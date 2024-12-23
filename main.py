from fastapi import FastAPI
from routers import chat, explain, fix
app = FastAPI()


app.include_router(chat.router)
app.include_router(explain.router)
app.include_router(fix.router)
