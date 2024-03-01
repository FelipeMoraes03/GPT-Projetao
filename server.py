from fastapi import FastAPI
from api.api import *

app = FastAPI()

@app.post("/gpt_call")
def gpt_call_post(message_input: str):
    return gpt_call(message_input)