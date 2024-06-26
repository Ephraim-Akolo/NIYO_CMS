import json
from channels.generic.websocket import AsyncWebsocketConsumer

class TaskConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("tasks", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("tasks", self.channel_name)

    async def receive(self, text_data):
        pass  # Not expecting to receive data from the client in this example

    async def task_update(self, event):
        await self.send(text_data=json.dumps(event["message"]))
