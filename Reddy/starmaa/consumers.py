import json
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
from django.utils import timezone

class TimeConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        while True:
            current_time = timezone.localtime(timezone.now()).strftime('%H:%M:%S')
            await self.send(text_data=json.dumps({'current_time': current_time}))
            await asyncio.sleep(60)  # Update every minute
