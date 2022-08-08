import logging
import os
import time
from datetime import datetime, timedelta
from slack_sdk import WebClient
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

logging.basicConfig(level=logging.INFO)
load_dotenv()

SLACK_BOT_TOKEN = os.environ['user_oauth_token']
SLACK_APP_TOKEN = os.environ['socket_mode_token']

app = App(token = SLACK_BOT_TOKEN)
channel_id = "C03S24XKH6H"

@app.event("app_mention")
def mention_handler(body, context, payload, options, say, event):
    say("Hello and welcome to Meditation Bot. Here are some helpful tips to get started!\n\nType start - Will start timer for TEN minutes and let you relax. ")

@app.message("start")
def say_hello(message,say):
    user = message['user']
    currentTime = datetime.now()
    up_curr = currentTime.strftime("%H:%M")
    addedTime = datetime.now() + timedelta(minutes=10)
    up_added = addedTime.strftime("%H:%M")
    say(f"Breathe in and Breathe out slowly! Take the time to relax and regain control.\nThe current time is {up_curr}.\nI will ping you at {up_added}")
    time.sleep(2)
    say(f"Hi, <@{user}> your meditation session has ended")
    say("Was your experience 'Positive' or 'Negative'")
   
@app.message("Positive")
def best(message,say):
    say("CONGRATULATIONS🥳, you have found enlightenment!")
    say("You can always @ me again for another peaceful experience!")

@app.message("Negative")
def worst(message,say):
    say("Aww, I hope you still have a great day:grin:!")
    say("You can always @ me to try again!")
    

if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()
