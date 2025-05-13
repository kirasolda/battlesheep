from fastapi import FastAPI

import battlesheep.config

app = FastAPI()


@app.get("/check")
def check():
    return {"status": "ok"}


@app.post("/message")
def message(payload: dict):
    return {"received": payload}
