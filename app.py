from flask import Flask, redirect, url_for, render_template, request, session
from flask_socketio import SocketIO
import datetime

app = Flask(__name__)
app.secret_key = "hello" 
socketio = SocketIO(app)
news = []
db = SQLAlchemy(app)



@app.route("/register", methods=["POST", "GET"])
def register_name():
    if request.method == "POST":
        session["name"] = request.form["name"]
        return redirect(url_for("chatroom"))
    else:
        return render_template("register.html")


app.route("/chatroom", mathods=["POST", "GET"])
def chatroom():
    if request.method == "POST":
        pass
    
    if request.method == "GET":
        return render_template("chatroom.html")

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
