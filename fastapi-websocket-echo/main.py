from fastapi import FastAPI, WebSocket, Request, WebSocketDisconnect
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.websocket("/ws")
async def web_socket_method(websocket: WebSocket):
    await websocket.accept()

    try:
        while True:
            data = await websocket.receive_text()
            response = "server received " + data
            await websocket.send_text(response)
    except WebSocketDisconnect :
        print("connection closed")

