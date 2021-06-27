import logging

from telegram import Update, Message, ParseMode
from telegram.ext import CallbackContext, MessageHandler, CommandHandler, Filters

# from pprint import pformat, pprint
from re import match

from settings import *

logger = logging.getLogger(__name__)

about_message = (
				'This bot is made bye Negar Tavakoli.🙃\n'+
				'Join our <a href="https://t.me/yourbots1">channel</a> below to get new bots!😉\n'+
				'<a href="https://github.com/baranegaranna">GitHub</a>')

def copy_a_message_and_reply_to_it(chat_id:int, update:Update, context:CallbackContext, reply_to_message_id:int):
	try:
		bot_message = context.bot.copyMessage(chat_id=chat_id, from_chat_id=update.effective_chat.id, 
						message_id=update.message.message_id, reply_to_message_id=reply_to_message_id)
		text = (
			f'{NAME}: {update.effective_user.full_name}\n'+
			f'{CHAT_ID}: {update.effective_chat.id}\n'+
			f'{MESSAGE_ID}: {update.effective_message.message_id}\n')

		context.bot.sendMessage(chat_id=chat_id, text=text, reply_to_message_id=bot_message.message_id)

	except Exception:
		bot_message = context.bot.copyMessage(chat_id=chat_id, from_chat_id=update.effective_chat.id, 
						message_id=update.message.message_id, reply_to_message_id=None)
		text = (
			f'{NAME}: {update.effective_user.full_name}\n'+
			f'{CHAT_ID}: {update.effective_chat.id}\n'+
			f'{MESSAGE_ID}: {update.effective_message.message_id}\n')

		context.bot.sendMessage(chat_id=chat_id, text=text, reply_to_message_id=bot_message.message_id)

	except:
		update.effective_message.reply_text(text=unable_to_reply_message)
		
#--------------------------------------Callbacks--------------------------------------#

def start(update:Update, context:CallbackContext) -> None:
	update.message.reply_text(text=welcome_message)
	update.message.reply_text(text=about_message, parse_mode=ParseMode.HTML, disable_web_page_preview=True)

def about(update:Update, context:CallbackContext) -> None:
	update.message.reply_text(text=about_message, parse_mode=ParseMode.HTML, disable_web_page_preview=True)

def available_commands(update:Update, context:CallbackContext) -> None:
	update.message.reply_text(text=available_commands_message)
	update.message.reply_text(text=10 + 'hi')

def new_member(update:Update, context:CallbackContext) -> None:
	new_chat_members: list = update.message.new_chat_members
	bot_id = context.bot.id 
	
	for user in new_chat_members:
		if user.id == bot_id:
			context.bot.sendMessage(chat_id=update.effective_chat.id,
						 text=group_message)
			break

def sending_message(update:Update, context:CallbackContext) -> None:
	bot_id = context.bot.id

	reply_to_message:Message = update.message.reply_to_message
	if reply_to_message:
		if reply_to_message.from_user.id == bot_id and reply_to_message.text != None:

			lines = reply_to_message.text.splitlines()

			try:
				user_chat_id = lines[-2]
				user_mssg_id = lines[-1]
			except IndexError:
				user_chat_id = ''
				user_mssg_id = ''
			
			match_chat_id = match( rf'^{CHAT_ID}: (-\d*$|\d*$)', user_chat_id ) 
			match_mssg_id = match( rf'^{MESSAGE_ID}: \d*$', user_mssg_id )

			if bool(match_chat_id) and bool(match_mssg_id):
				chat_id = int(user_chat_id.split()[-1])
				mssg_id = int(user_mssg_id.split()[-1])
				copy_a_message_and_reply_to_it(chat_id=chat_id, update=update, context=context, reply_to_message_id=mssg_id)
	
	elif update.effective_chat.id != group_chat_id and update.effective_chat.type == 'private':
		copy_a_message_and_reply_to_it(chat_id=group_chat_id, update=update, context=context, reply_to_message_id=None)


handlers = [
	CommandHandler('start', start  , Filters.chat_type.private),
	CommandHandler('about', about  , Filters.chat_type.private),
	MessageHandler(Filters.command & Filters.chat_type.private, available_commands),

	MessageHandler(Filters.status_update.new_chat_members, new_member),
	MessageHandler(Filters.update.message, sending_message),
]
