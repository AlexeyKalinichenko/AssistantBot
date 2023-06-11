from django.core.management.base import BaseCommand
import telebot

def runBot():
	bot = telebot.TeleBot('')

	@bot.message_handler(content_types = ['text'])
	def GetMessage(message):
		print('=' * 20)
		print(message.text)
		print('=' * 20)
		myChatId = 0
		bot.send_message(myChatId, 'Test message!')

	bot.polling(none_stop = True, interval = 0)

class Command(BaseCommand):
	help = "test-django-bot"

	def handle(self, *args, **options):
		print('===before launch===')
		runBot()
		print('===after launch===')
