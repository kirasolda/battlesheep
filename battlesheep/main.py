from fastapi import FastAPI

app = FastAPI()


@app.get("/check")
def check():
    return {"status": "ok"}


@app.post("/message")
def message(payload: dict):
    print(payload)
    return {"received": payload}


# Invoke-WebRequest -Uri http://localhost:8000/message -Method POST -Headers @{ "Content-Type" = "application/json" } -Body '{"message": "Hello, World!"}'
