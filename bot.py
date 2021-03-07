import telebot
import requests

def req():
	response = requests.get("https://api.coinbase.com/v2/prices/spot?currency=USD")
	price = response.json()["data"]["amount"]
	return price

price = req()

bot = telebot.TeleBot("TOKEN")


@bot.message_handler(commands=['start',])
def send_welcome(message):
	bot.reply_to(message, "MESSAGE ONE")

@bot.message_handler(commands=["bitcoin"])
def bitcoin_price(message):
	bot.reply_to(message, f"قیمت بیت کوین در حال حاضر برابر "
						  f"{price}"
						  f" دلار میباشد ")

@bot.message_handler(func=lambda message: True )
def echo_all(message):
	bot.reply_to(message,f' \n  از دستورات  \n'
						 f'/start \n'
						 f'/help \n'
						 f'/bitcoin \n'
						 f'استفاده کنید')



@bot.message_handler(content_types=["new_chat_photo"])
def welcome(message):
	bot.reply_to(message,"MESSAGE TWO")


@bot.message_handler(func=lambda message: "MESSAGE TWO" )
def echo_aز(message):
	bot.reply_to(message,f' \n  از دستورات  \n'
						 f'/ \n'
						 f'/help \n'
						 f'/bitcoin \n'
						 f'استفاده کنید')




bot.polling()
