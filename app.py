from flask import Flask, redirect, url_for, render_template, request, session
from flask_socketio import SocketIO
import datetime

app = Flask(__name__)
app.secret_key = "hello" 
socketio = SocketIO(app)
news = []



@app.route("/register", methods=["POST", "GET"])
def register_name():
    if request.method == "POST":
        session["name"] = request.form["name"]
        return redirect(url_for("chatroom"))
    else:
        return render_template("login.html")


@app.route("/chatroom", methods=["POST", "GET"])
def chatroom():
    if request.method == "POST":
        pass

    else:
        print(session["name"])
        return render_template("ChatRoom.html")

@socketio.on('my event')
def handle_my_custom_event(json):
    if 'message' in json:
        if json['message'] != "":
            if json['message'] == '#pw01':
                json['message'] = session['name'] + " connected"
                json['username'] = "Local Bot"
                socketio.emit('my response', json, namespace="/")
            else:
                json['username'] = session['user-name']
                socketio.emit('my response', json)
    else:
        pass

if __name__ == "__main__":
    app.run()
