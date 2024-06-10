from flask import Flask # Flask is a web server that can be used to host the bot
from threading import Thread

bot = Flask('')

@bot.route('/')
def home():
    return "I'm alive"

def run():
    bot.run(host='0.0.0.0', port=8080)
    
def keep_alive():
    t = Thread(target=run)
    t.start()