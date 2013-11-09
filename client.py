from flask import Flask
from flask_sockets import Sockets
from Tkinter import *

app = Flask(__name__)
sockets = Sockets(app)

gestures = {}

@sockets.route('/get_all_gestures')
def set_gestures(ws):
	while True:
		names = ws.receive()
		for name in names:
			gestures[name] = ''

@sockets.route('/add_gesture')
def add_gesture(ws):
	while True:
		name = ws.receive()
		gestures[name] = ''

@sockets.route('/do_gesture')
def do_gesture(ws):
    while True:
        name = ws.receive()
        program = gestures[name]
        run(program)

if __name__ == '__main__':
	start_gui()
	connect_to_server()
    app.run()