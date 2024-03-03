from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.api import *
from api.model import *

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/chat")
def gpt_call_post(chat_message: ChatMessage):
    return gpt_call(chat_message.message)