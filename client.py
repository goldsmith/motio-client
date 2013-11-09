import Tkinter
from flask import Flask
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

def start_gui():
	master = Tk()
	listbox = Listbox(master)
	listbox.pack()   
	listbox.insert(END, "a list entry")
	for item in ["one", "two", "three", "four"]:
   	 	listbox.insert(END, item)
	mainloop()

if __name__ == '__main__':
	start_gui()
	# connect_to_server()
    # app.run()