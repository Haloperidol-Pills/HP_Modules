__version__ = 2, 0, 1
# name: foundation
# meta developer: @hp_modules
# description: sends NSFW pics from foundation

import random
import logging
import time
from telethon.tl.functions.messages import ImportChatInviteRequest
from herokutl.types import Message
from .. import loader, utils

logger = logging.getLogger("foundation")

link = "https://t.me/+ZfmKdDrEMCA1NWEy"

entity = link

@loader.tds
class Foundation(loader.Module):
    """sends NSFW pics from foundation"""

    strings = {
    "name": "Foundation",
    "sending": "<emoji document_id=5276395476646653290>🔍</emoji>Searching for NSFW pic",
    "error": "<emoji document_id=5276240711795107620>⚠️</emoji>An error accured, check logs",
    }

    strings_ru = {
    "sending": "<emoji document_id=5276395476646653290>🔍</emoji>Ищем NSFW картинку",
    "error": "<emoji document_id=5276240711795107620>⚠️</emoji>Произошла ошибка, чекай логи",
    }
            
    @loader.command(
    en_doc="Send NSFW pic from Foundation",
    ru_doc="Отправить NSFW картинку с Фонда",
)

    async def fond(self, message):
        """Отправить NSFW картинку с Фонда"""
        send = await utils.answer(message, self.strings("sending"))
    
        try:
            mes = await self.client.get_messages(entity, limit=1500)
        except Exception:
            return await utils.answer(message, self.strings("error")), logger.error("An error! Probably, your request to enter Foundation is pending and wasn't accepted yet, if you didn't sent request, you can do this by link:" f"{link}")
	        
        rndm_mes = random.choice(mes)
        await message.client.send_message(
        message.peer_id,
        message=rndm_mes,
        reply_to=getattr(message, "reply_to_msg_id", None)
    )
        time.sleep(0.2)
        await self.client.delete_messages(message.chat_id, send)
