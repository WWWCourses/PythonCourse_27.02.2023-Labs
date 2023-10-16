import socket

BUF_SIZE = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER_IP = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER_IP, PORT)

def send(msg):
    message = msg.encode(FORMAT)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


# create an INET (i.e. IPv4), STREAMing (i.e. TCP) socket:
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# now connect to the server given with ADDR tupple:
client.connect(ADDR)
print(f'Client is connected to {ADDR} ')

# send some messages
while True:
	msg = input('Enter a message: ')
	if msg:
		send(msg)
	else:
		send(DISCONNECT_MESSAGE)
		break
# close the socketclient
client.close()