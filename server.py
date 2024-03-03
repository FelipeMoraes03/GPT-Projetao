from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from api.api import *

class ChatMessage(BaseModel):
    message: str

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.post("/gpt_call")
# def gpt_call_post(message_input: str):
#     return gpt_call(message_input)



# APENAS PARA TESTAR O CHAT NO FRONT
@app.post("/test_chat")
def test_chat_call(chat_message: ChatMessage):
    return test_chat(chat_message.message)