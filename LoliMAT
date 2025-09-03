__version__ = 1, 5
# meta developer: @Enceth,fork by @haloperidol_pills
# change-log: fix link
# invite link: https://t.me/+s8GoAISy21ZjZWEy

import asyncio
from telethon.tl.functions.messages import ImportChatInviteRequest
import random
from .. import loader, utils

@loader.tds
class LoliMAT(loader.Module):
    """
    Абсолютно рандом порнуха с фонда 
    """

    strings = {
        "name": "LoliMAT",
        "forwarding": "📥 Ща будет",
        "done": "✅ Вот",
        "error": "❌ Ошибка: {}, if you not participating in channel, here the link:https://t.me/+6ZqZs2bIyLAxYTUy",
        "no_messages": "❌ Ну все пизда",
    }
    
    async def client_ready(self, client, db):
        self.client = client

    async def _join_chat(self, invite_link):
        """
        ах ох ох ахахахахах
        """
        try:
            return await self.client.get_entity(invite_link)
        except Exception:
            await self.client(ImportChatInviteRequest(invite_link.split("+")[1]))
            return await self.client.get_entity(invite_link)

    @loader.command(
        ru_doc="Рандом порнуха с канала",
        en_doc="Random nsfw from channel ",
    )
    async def loliMAT(self, message):
        """
        Рандом порнушка
        """
        chat_invite_link = "https://t.me/+s8GoAISy21ZjZWEy"

        try:
            entity = await self._join_chat(chat_invite_link)
            await utils.answer(message, self.strings["forwarding"])

            messages = await self.client.get_messages(entity, limit=300)
            if not messages:
                await utils.answer(message, self.strings["no_messages"])
                return

            random_msg = random.choice(messages)
            await self.client.send_message(
                message.to_id,
                random_msg.message,
                file=random_msg.media,
            )
            sent_message = await utils.answer(message, self.strings["done"])
            await asyncio.sleep(3)
            await self.client.delete_messages(message.chat_id, sent_message)
        except Exception as e:
            await utils.answer(message, self.strings["error"].format(e))
