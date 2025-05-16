import queue
import threading

from fastapi import FastAPI

from battlesheep.game import BSGame

message_queue = queue.Queue()

app = FastAPI()


@app.get("/check")
def check():
    return {"status": "ok"}


@app.post("/message")
def message(payload: dict):
    message = payload.get("message")
    if message:
        message_queue.put(message)
        print(f"Message received: {message}")
    return {"received": payload}


def start_pygame():
    game = BSGame(message_queue)
    game.launch()


pygame_thread = threading.Thread(target=start_pygame, daemon=True)
pygame_thread.start()
