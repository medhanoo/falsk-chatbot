from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os
app = Flask(__name__)

#trainer.train("chatterbot.corpus.english")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("Majestic Admin.html")

@app.route("/chatsetup")
def chatsetup():
    custname = request.args.get('custname')
    #print(custname)
    #print(os.getcwd())
    trainer = ChatterBotCorpusTrainer(english_bot)
    if os.path.exists(custname + '.yml'):
        print ("found custname yaml file")
        trainer.train(custname)
        #trainer.train("chatterbot.corpus.english")
    else:
        print("file not found")
        trainer.train("abc")
        #trainer.train("chatterbot.corpus.english")
    return "OK" 

@app.route("/chatbox")
def chatbox():
    return render_template("chat.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))


if __name__ == "__main__":
    if os.path.exists('db.sqlite3'):
        os.remove('db.sqlite3')
        print("removed db.sqlite3")
    english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
    app.run()
