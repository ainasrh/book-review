from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ReviewConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # review is the chat room name  
        # clien add to thsi chat room 
        
        await self.channel_layer.group_add("reviews", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("reviews", self.channel_name)

    async def send_review(self, event):
        await self.send(text_data=json.dumps(event["review"]))