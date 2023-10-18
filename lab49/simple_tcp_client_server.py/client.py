import socket
import threading
import select
import sys

BUF_SIZE = 4096
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER_IP = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER_IP, PORT)

def start_sending(client):
	# send some messages
	while True:
		lock.acquire()
		msg = input('Enter a message: ')
		if msg!='exit':
			client.send(msg.encode())
		else:
			client.send(DISCONNECT_MESSAGE.encode())
			client.close()
			print('Buy!')
			exit()
		lock.release()

def start_listening(client):
	while True:
		lock.acquire()
		msg = client.recv(BUF_SIZE).decode()
		print(msg)
		lock.release()


def start_talking():
	while True:
		input_stream = [sys.stdin, socket]
		read_streams, _, _ = select.select(input_stream, [], [])
		for active in read_streams:
			if active==socket:
				msg = client.recv(BUF_SIZE).decode()
				print(msg)
			else:
				msg = input('Enter a message: ')
				if msg!='exit':
					client.send(msg.encode())
				else:
					client.send(DISCONNECT_MESSAGE.encode())
					client.close()
					print('Buy!')
					exit()




def login():
	name = input('Enter your name: ')
	return name

if __name__=="__main__":
	# create an INET (i.e. IPv4), STREAMing (i.e. TCP) socket:
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# now connect to the server given with ADDR tupple:
	client.connect(ADDR)

	# send login details to the server
	name = login()
	client.send(name.encode())
	welcome_msg = client.recv(BUF_SIZE).decode()

	print(welcome_msg)

	start_talking()


	# lock = threading.Lock()

	# send_thread = threading.Thread(
	# 	target=start_sending,
	# 	args=(client,)
	# )
	# send_thread.start()

	# listen_thread = threading.Thread(
	# 	target=start_listening,
	# 	args=(client,)
	# )
	# listen_thread.start()


