from flask import Flask
from flask_sockets import Sockets

app = Flask(__name__)
sockets = Sockets(app)

@sockets.route('/command')
def echo_socket(ws):
    while True:
        message = ws.receive()
        do_command(message)

def do_command(command):
	"""
	Execute a command recieved from the server (should be a dictionary)

	command = {
		"command": <command>
	}

	<command> should be one of (so far):
	(
		"volume up",
		"volume down",
		"volume mute"
	)

	Hint: look into system commands

	"""

	pass

if __name__ == '__main__':
    app.run()