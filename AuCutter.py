from .. import loader, utils  # pylint: disable=relative-beyond-top-level
import logging
from os import remove as DelFile
import urllib.request
import math

logger = logging.getLogger(__name__)


def register(cb):
    cb(AuCutterMod())


@loader.tds
class AuCutterMod(loader.Module):
    """AudioCutter"""

  async def client_ready(self, client, db):
        self.client = client

    @loader.sudo
    async def cutcmd(self, message):
        """Обрезает аудио, работает через @audiocutterbot"""

if reply or reply.media:
	try:
		if reply.audio:
			chat='438382295'
			forward_message(chat, message.chat.id, message.audio)
else: 
	await message.edit('РЕПЛАЙ НА АУДИО!!' )		