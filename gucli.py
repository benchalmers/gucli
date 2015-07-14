#! /usr/bin/env python3

import http.server
import webbrowser
import threading

class MyHandler(http.server.BaseHTTPRequestHandler):
	def do_HEAD(self):
		pass
	def do_GET(self):
		print("hello")
		pass

Handler = http.server.HTTPServer(('',0), MyHandler)
print('started server at port'+str(Handler.server_address[1]))
threading.Thread(target=Handler.serve_forever).start()
webbrowser.open('http://localhost:'+str(Handler.server_address[1]))
