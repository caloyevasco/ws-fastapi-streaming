from fastapi import APIRouter
from fastapi import WebSocket
from datetime import datetime

import wave
import struct
import json


speech_to_text_router = APIRouter()


@speech_to_text_router.websocket('/{user_id}')
async def create_room(websocket : WebSocket, user_id : int):
    await websocket.accept()
    while True:
        print(f"{user_id}")
        data = await websocket.receive()
        if data.get('text'):
            data = json.loads(data['text'])['binary']
            with wave.open(f"temp/audio.wav", 'w') as f:
                f.setparams((1, 2, 16000, 512, "NONE", "NONE"))
                f.writeframes(struct.pack("h" * len(data), *data))
