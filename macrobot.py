
import os
from fbchat import Client
from fbchat.models import *
import time
from fbchat import log
from random import *
import glob


default_macro = "./macros/default.gif"

class MacroBot(Client):

	def _getMacro(self, text):
		global default_macro

		basefolder = "./macros/"
		file = basefolder + text
		jpg_file = file + ".jpg"
		png_file = file + ".png"
		gif_file = file + ".gif"
		
		if glob.glob(jpg_file):
			return jpg_file


		if glob.glob(gif_file):
			return gif_file


		if glob.glob(png_file):
			return png_file

		return default_macro

	def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
	   
		# log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))

		if  message_object.text is None:
			return

		text = message_object.text.lower()

		if (text.startswith("#m ")):
			text = text[3:]
			text = text.strip()
			print(self._getMacro(text))
			self.sendLocalImage(self._getMacro(text), message=Message(text=''), thread_id=thread_id, thread_type=thread_type)

lines = []
with open('credentials', 'r') as f:
    lines = f.readlines()


if len(lines) < 2:
	print("please provide email and password")

email = lines[0].strip()
password = lines[1].strip()

client = MacroBot(email, password)
print('Own id: {}'.format(client.uid))

client.listen()
