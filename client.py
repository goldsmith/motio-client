import multiprocessing

from flask import Flask, render_template, request
from flask_sockets import Sockets

from websocket import create_connection

from client import pipe

app = Flask(__name__)
sockets = Sockets(app)

gestures = {}

def run(name):
	path = gestures[name]
	# do something with path

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
	ws = create_connection("ws://motio.herokuapp.com/client_socket")
	while True:
		data = ws.recv()
		if data["action"] == "add_gesture":

web_view = pipe()

@sockets.route('/gesture')
def echo_socket(ws):
    for message in web_view:
    	if message['action'] == "do_gesture":
    		run(message['name'])
    	else:
        	ws.send(message)

if __name__ == '__main__':
	# start_gui()
	# connect_to_server()
    app.run()