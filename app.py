from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
import datetime

app = Flask(__name__)
app.secret_key = "hello" 
socketio = SocketIO(app)
news = []
db = SQLAlchemy(app)



@app.route("/register", methods=["POST", "GET"])
def register_name():
    render_template()


@socketio.on('my event')
def handle_my_custom_event(json):
    if 'message' in json:
        if json['message'] != "":
            if json['message'] == '#pw01':
                json['message'] = session['user-name'] + " connected"
                json['username'] = "Local Bot"
                socketio.emit('my response', json, namespace="/")
            else:
                json['username'] = session['user-name']
                socketio.emit('my response', json)
    else:
        pass
