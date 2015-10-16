import os
from datetime import datetime
from flask import Flask, request, flash, url_for, redirect, abort

app = Flask(__name__)
app.config.from_pyfile('flaskapp.cfg')

TWILIO_MESSAGE_TEMP =
"""
<?xml version="1.0" encoding="UTF-8"?>
<Response>
<Message>{}</Message>
</Response>
"""

@app.route("/", methods=['POST'])
def index():
    return TWILIO_MESSAGE_TEMP.format("hi")


@app.route("/", methods=['GET'])
def test():
    return "<strong>It's Alive!</strong>"

if __name__ == '__main__':
    app.run()
