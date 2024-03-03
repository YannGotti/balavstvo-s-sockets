import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .service import userConnected, userDisconnected, actionUser


class SomeConsumer(AsyncWebsocketConsumer):
    groups = ['players_group']
    connected_users = {}

    async def connect(self):
        await userConnected(self)
        await self.accept()


    async def disconnect(self, close_code):
        await userDisconnected(self)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        await actionUser(self, message)

    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event))