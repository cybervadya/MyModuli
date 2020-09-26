from .. import loader, utils  # pylint: disable=relative-beyond-top-level
import logging
import urllib.request

logger = logging.getLogger(__name__)


def register(cb):
    cb(AuCutterMod())

class AuCutterMod(loader.Module):
    """AudioCutter"""

async def cutcmd(self, message):
     """Обрезает аудио, работает через @audiocutterbot"""

if reply.audio:
	chat='438382295'
	forward_message(chat, message.chat.id, message.audio)
else: 
	await message.delete()
