# name: Voices
# meta developer: @HP_Modules
# author: @HaloperidolPills
__version__ = 1, 0, 0

from .. import loader, utils

@loader.tds
class Voices(loader.Module):

    strings = {
        "name": "Voices"
    }

    @loader.command()
    async def kisicmd(self, message):
        """киси киси мяу мяу"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/iluglhjfjky/2",
            voice_note = True,
            reply_to = reply.id if reply else None,
        )
        return

    async def creditcmd(self, message):
        """social credit siren"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/iluglhjfjky/3",
            voice_note = True,
            reply_to = reply.id if reply else None,
        )
        return
        
    async def goydacmd(self, message):
        """Гойда"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/iluglhjfjky/4",
            voice_note = True,
            reply_to = reply.id if reply else None,
        )
        return

    async def kakashkicmd(self, message):
        """Грызть какашки"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/iluglhjfjky/5",
            voice_note = True,
            reply_to = reply.id if reply else None,
        )
        return 

    async def dobroeutrocmd(self, message):
        """Доброе утро"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/iluglhjfjky/6",
            voice_note = True,
            reply_to = reply.id if reply else None,
        )
        return

    async def womancmd(self, message):
        """ААААААА ЖЕНЩИНА"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/iluglhjfjky/7",
            voice_note = True,
            reply_to = reply.id if reply else None,
        )
        return