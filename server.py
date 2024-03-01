from fastapi import FastAPI
from api.api import *

app = FastAPI()

# @app.post("/gpt_call")
# def gpt_call_post(message_input: str):
#     return gpt_call(message_input)



# APENAS PARA TESTAR O CHAT NO FRONT
@app.post("/test_chat")
def test_chat_call(message_input: str):
    return test_chat(message_input)