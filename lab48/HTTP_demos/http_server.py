""" Example using http.server built-in module

	Reference :https://docs.python.org/3/library/http.server.html

"""

import argparse
from http.server import HTTPServer, BaseHTTPRequestHandler, socketserver
import os
import re


SERVER_IP = '127.0.0.1'
SERVER_PORT = '8080'
SERVER_ROOT = '/MyWebSite/'



class RequestHandler(BaseHTTPRequestHandler):
	def __init__(self, request: bytes, client_address: tuple[str, int], server: socketserver.BaseServer) -> None:
		super().__init__(request, client_address, server)

		print(f'Received request from: {self.client_address}')
		# printe(f'Request: {self.request}')

	def _set_headers(self,status_code, content_type_value="text/html"):
		print(f'content_type_value: {content_type_value} ')
		self.send_response(status_code)
		self.send_header("Content-type", content_type_value)
		self.send_header("Server", "My Simple HTTP server ")
		self.end_headers()

	def _get_request_headers(self):
		print(self.headers)

	def do_GET(self):
		# Make response body:
		print(f'******* Path:{self.path}')
		if self.path =="/":
			# file = httpd_root+self.path+'index.html'
			file = os.path.join(httpd_root,'index.html')
		else:
			# get query params, if any
			rgex = re.compile(r'\?(.*)$')
			m = rgex.search(self.path)
			if m:
				query = m.group(1)
				print(f'QUERY: {query}')
				# do something with query

			# get file
			file = httpd_root+self.path

		try:
			# ./MyWebSite/index.html

			body = open(file, 'rb').read()
			status_code = 200
		except:
			# return 404 if file did not exists
			body = f'no such file: {file}'.encode('utf-8')
			status_code = 404

		# setup response
		# check if image is requested:
		# /images/submit_icon.png
		rgex = re.compile(r'\.(.*)$')
		m = rgex.search(self.path)

		ctv = ''
		if m:
			extention = m.group(1)

			if extention=='png':
				ctv = 'image/png'



		self._set_headers(status_code, ctv)

		# send responce body
		self.wfile.write(body)

	def do_HEAD(self):
		self._set_headers(200)

	def do_POST(self):
		self._set_headers(200)
		content_length = int(self.headers.get('content-length', 0))
		post_body = self.rfile.read(content_length)
		print(f'post_body:{post_body}')
		self.wfile.write(f'received post request:<br>{post_body}'.encode('utf-8'))

def get_args():
	parser = argparse.ArgumentParser(description="Run a simple HTTP server")
	parser.add_argument(
		"-l",
		"--listen",
		default=SERVER_IP,
		help="IP address on which the server listens",
	)
	parser.add_argument(
		"-p",
		"--port",
		type=int,
		default=SERVER_PORT,
		help="port on which the server listens",
	)
	parser.add_argument(
		"-r",
		"--root",
		default=SERVER_ROOT,
		help="server root path",
	)

	args = parser.parse_args()
	print(args)
	return args

if __name__ == "__main__":
	args = get_args()

	addr,port,httpd_root = args.listen, args.port, args.root
	# HTTPD_PATH=os.path.join(SERVER_ROOT_PATH,root)

	server_address = (addr, port)

	httpd = HTTPServer(server_address, RequestHandler)

	try:
		print(f"Starting httpd server on {addr}:{port}.Serving from {httpd_root}")
		httpd.serve_forever()

	except KeyboardInterrupt:
		pass

	httpd.server_close()
	print('Stopping httpd...\n')
	exit()