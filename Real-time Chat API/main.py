# main.py

from fastapi import FastAPI, WebSocket, HTTPException, Depends
from fastapi.security import APIKeyHeader
from fastapi.responses import HTMLResponse
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from typing import Dict

app = FastAPI()

# Enable CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define API key security
api_key_header = APIKeyHeader(name="X-API-Key")

# Store WebSocket connections and rooms
connections: Dict[str, Dict[str, WebSocket]] = {}


# Authentication function
async def get_user(api_key: str = Depends(api_key_header)):
    # Implement your authentication logic here
    # For simplicity, you can use a predefined set of API keys
    api_keys = {"user1": "key1", "user2": "key2"}
    if api_key not in api_keys.values():
        raise HTTPException(status_code=403, detail="Invalid API key")
    return {"user_id": [user_id for user_id, key in api_keys.items() if key == api_key][0]}


# Serve a simple HTML page for the frontend
@app.get("/")
async def read_root():
    return HTMLResponse(content=open("static/index.html").read(), status_code=200)


# WebSocket endpoint
@app.websocket("/ws/{room_id}/{user_id}")
async def websocket_endpoint(websocket: WebSocket, room_id: str, user_id: str, user: dict = Depends(get_user)):
    # Validate room_id
    # In a real application, you might have a more sophisticated room management system
    # For simplicity, let's assume any string is a valid room_id
    if not room_id:
        raise HTTPException(status_code=400, detail="Invalid room_id")

    # Store the WebSocket connection
    if room_id not in connections:
        connections[room_id] = {}
    connections[room_id][user_id] = websocket

    # Notify the user has joined the room
    await broadcast(room_id, f"User {user_id} has joined the room {room_id}")

    # Infinite loop to handle incoming messages
    while True:
        try:
            # Receive message from the user
            message = await websocket.receive_text()
            # Broadcast the message to all users in the room
            await broadcast(room_id, f"{user_id}: {message}")
        except WebSocketDisconnect:
            # Notify when a user disconnects
            await broadcast(room_id, f"User {user_id} has left the room {room_id}")
            break


# Broadcast message to all users in the room
async def broadcast(room_id: str, message: str):
    if room_id in connections:
        for user_id, connection in connections[room_id].items():
            await connection.send_text(message)
