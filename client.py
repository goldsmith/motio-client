import multiprocessing

from flask import Flask, render_template, request
from flask_sockets import Sockets

from websocket import create_connection

from utils import pipe

app = Flask(__name__)
sockets = Sockets(app)

gestures = {}
web_socket = None

def run(name):
	path = gestures[name]
	# do something with path

@app.route("/")
def index():
	return render_template('page.html')

@app.route("/add_gesture_filepath")
def add_gesture_filepath():
	name = request.form['name']
	path = request.form['path'] 
	gestures[name] = path

	print "name", name
	print "path", path

def get_from_server():
	# ws = create_connection("ws://localhost:8000/client_socket")
	ws = create_connection("ws://motio.herokuapp.com/client_socket")
	print ws
	while True:
		print "hi", ws
		data = ws.recv()
		print 'data', data
		if data["action"] == "add_gesture":
			gestures[data["name"]] = ''
			web_socket.send(data)
		elif data["action"] == "do_gesture":
			run(gestures[data["name"]])
		else:
			print "damn!"
 
web_view = pipe()

@sockets.route('/gesture')
def echo_socket(ws):

	web_socket = ws

	while True:
		continue

if __name__ == '__main__':
	server = multiprocessing.Process(target=get_from_server)
	server.start()
	# connect_to_server()
	app.run()