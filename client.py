import Tkinter
from flask import Flask, render_template, request
from flask_sockets import Sockets
from Tkinter import *

app = Flask(__name__)
sockets = Sockets(app)

gestures = {}

# @sockets.route('/get_all_gestures')
# def set_gestures(ws):
# 	while True:
# 		names = ws.receive()
# 		for name in names:
# 			gestures[name] = ''

# @sockets.route('/add_gesture')
# def add_gesture(ws):
# 	while True:
# 		name = ws.receive()
# 		gestures[name] = ''

# @sockets.route('/do_gesture')
# def do_gesture(ws):
#     while True:
#         name = ws.receive()
#         program = gestures[name]
#         run(program)

@app.route("/"):
def index():
	return render_template('page.html')

@app.route("/add_gesture_filepath")
def add_gesture_filepath():
	# name = request.data['name']
	# path = request.data['path'] 
	# gestures[name] = path
	pass

def get_from_server():
	while True:
		yield

@sockets.route('/gesture')
def echo_socket(ws):
    while True:
        message = get_from_server()
        ws.send(message)

if __name__ == '__main__':
	# start_gui()
	# connect_to_server()
    app.run()