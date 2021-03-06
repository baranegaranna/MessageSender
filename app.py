from logging import disable
from telegram import Bot, Update
from telegram.ext import Updater, Dispatcher, PicklePersistence

from handlers import handlers

from settings import token, persistence_filename, group_chat_id, bot_is_working_message

from flask import Flask, request
from flask_sslify import SSLify

def settitng_up_bot_and_dispatcher(token, persistence_filename=persistence_filename):
	bot_persistence = PicklePersistence(filename=persistence_filename)

	updater = Updater(token=token, persistence=bot_persistence, use_context=True)

	bot = updater.bot
	dispatcher = updater.dispatcher

	for hdlr in handlers:
		dispatcher.add_handler(hdlr)

	return bot, dispatcher

app = Flask(__name__)
SSLify(app)

bot, dispatcher = settitng_up_bot_and_dispatcher(token, persistence_filename=persistence_filename)

@app.route('/')
def website():
    return 'MessageSender2'

@app.route('/{}'.format(token), methods=['POST'])
def update():
	dispatcher.process_update(Update.de_json(request.json, bot))
	return 'ok'

bot.sendMessage(chat_id=group_chat_id, text=bot_is_working_message)

#! if you have not set webhook yet comment
#! codes above and uncomment codes below:

"""
from telegram.ext import Updater

from settings import token
from handlers import handlers
def main():
	updater = Updater(token=token, use_context=True)
	dispatcher = updater.dispatcher

	for i in handlers:
		dispatcher.add_handler(i)

	updater.start_polling()
	updater.idle()


if __name__ == '__main__':
	main()
"""