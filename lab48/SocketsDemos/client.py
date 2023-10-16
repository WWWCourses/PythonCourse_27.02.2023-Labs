import socket
from socket import AF_INET, SOCK_STREAM,SOCK_DGRAM

SERVER_NAME = 'localhost'
SERVER_IP = socket.gethostbyname(SERVER_NAME)
SERVER_PORT=9999

def UDP_client():
	client = socket.socket(family=AF_INET, type=SOCK_DGRAM)

	client.sendto(b'Hello Server',(SERVER_IP, SERVER_PORT))


def TCP_client():
	client = socket.socket(AF_INET, SOCK_STREAM)

	client.connect((SERVER_IP, SERVER_PORT))
	print(f'Client is connected to {(SERVER_IP, SERVER_PORT)} ')

	while True:
		msg = input("Enter a message:")
		client.send(msg.encode())

if __name__ == '__main__':
	TCP_client()