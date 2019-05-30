from .message import Message
import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug("Initialising db layer")

messages = []

m1 = Message()
m1.time = "2019-02-18 11:00"
m1.content = "Hallo!"
    
m2 = Message()
m2.time = "2019-02-18 11:05"
m2.content = "De muur?"

messages.append(m1)
messages.append(m2)


def get_messages():
    global messages
    return messages


def add_message(timestamp, content):
    global messages
    m = Message()
    m.time = timestamp
    m.content = content
    messages.append(m)
