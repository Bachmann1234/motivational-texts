import logging
import random
from flask import Flask
from properties import twilio_sid, twilio_auth, receiver_number, twilio_number
from twilio.rest import TwilioRestClient

app = Flask(__name__)

# 4 times a week (on average) if run every minute
HOURS_A_DAY_CRON_RUNS = 14
MINUTES_IN_WEEK = float(60 * HOURS_A_DAY_CRON_RUNS * 7)
TEXTS_PER_WEEK = 4
text_probability = float(TEXTS_PER_WEEK) / MINUTES_IN_WEEK

messages = [
    "You can do this",
    "Don't rely on your future self, they are unreliable",
    "If you're tempted today. Take a minute and ask why. Is it really *that* good?",
    "Love yourself today",
    "Think about amusement park rides",
    "Think about marrying her",
    "Think about going to the store and everything fitting"
]


@app.route('/text/motivate')
def motivate():
    client = TwilioRestClient(twilio_sid, twilio_auth)
    if random.random() < text_probability:
        logging.info("Sending Text")
        client.messages.create(
            to=receiver_number,
            from_=twilio_number,
            body=random.choice(messages)
        )
    else:
        logging.info("No text this time!")
    return 'OK'
