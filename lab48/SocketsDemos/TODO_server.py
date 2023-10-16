import socket
from socket import AF_INET, SOCK_STREAM,SOCK_DGRAM



SERVER_NAME = 'localhost'
SERVER_IP = socket.gethostbyname(SERVER_NAME)
SERVER_PORT=9999
BUFF_SIZE=4096

def UDP_server():
	server = socket.socket(family=AF_INET, type=SOCK_DGRAM)
	server.bind((SERVER_IP, SERVER_PORT))

	msg,address = server.recvfrom(1024)

	print(f'recieved: {msg.decode()}')

def handle_client(conn, addr):
	print(f'addr: {addr}')
	msg = conn.recv(BUFF_SIZE)
	print(msg.decode())

def TCP_server():
	server = socket.socket(AF_INET, SOCK_STREAM)

	# bind the socket to the host
	server.bind((SERVER_IP, SERVER_PORT))

	print(f"Server is listening on {SERVER_IP}:{SERVER_PORT}")


	server.listen()


	while True:
		conn, addr = server.accept()
		# better to do with threading
		handle_client(conn, addr)





if __name__ == '__main__':
	TCP_server()