from app import settitng_up_bot_and_dispatcher

from settings import token, username, port

def main():
	bot, dispatcher = settitng_up_bot_and_dispatcher(token)
	bot.delete_webhook()
	bot.setWebhook(url=f'https://{username}.pythonanywhere.com:{port}/{token}')

if __name__ == '__main__':
	main()
