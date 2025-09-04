__version__ = 1, 0
# name = Aneks
# description = send aneks from AKB
# meta developer = @halopedidol_pills

import time
import random
import os
import logging
from herokutl.types import Message
from .. import loader, utils

logger = logging.getLogger("simplename")

entity = ("https://t.me/baneksru")

@loader.tds
class Aneks(loader.Module):
	"""Рандомные анекдоты из акб"""
	strings = {
	    "name": "Aneks", 
		"sending": "отправляю несмешной анек", 
		"error": "ааааа ашибка 00000",
		"nomes": "hz ashibka"
			}
		
	@loader.command(ru_doc="случайный анек из АКБ")
	async def anek(self, message):
	    """random akb anek"""
	    
	    try:
	        mes = await self.client.get_messages(entity, limit=300)
	    except Exception as e:
	        return await utils.answer(message, self.strings("error"))
	        
	        await utils.answer(message, self.strings("sending"))
	            
	    rndm_mes = random.choice(mes)
	    await message.client.send_message(
	        message.peer_id,
	        message=rndm_mes,
	        reply_to=getattr(message, "reply_to_msg_id", None)
	        )
	        