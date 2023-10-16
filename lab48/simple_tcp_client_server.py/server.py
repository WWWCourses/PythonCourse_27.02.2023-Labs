import socket
import threading

BUF_SIZE = 64
PORT = 5050
SERVER_IP = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER_IP, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

# create an INET (i.e. IPv4), STREAMing (i.e. TCP) socket:
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# reuse address
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# bind the socket to the host
server.bind(ADDR)

def handle_client(conn, addr):
	print(f"[NEW CONNECTION] {addr} connected.")

	connected = True
	while connected:
		# msg_length = conn.recv(BUF_SIZE).decode(FORMAT)
		# print(msg_length)


		# msg_length = int(msg_length)
		msg = conn.recv(BUF_SIZE).decode(FORMAT)
		if msg == DISCONNECT_MESSAGE:
			connected = False

		print(f"[{addr}] {msg}")
		conn.send("Msg received".encode(FORMAT))

	conn.close()


def start():
	server.listen()
	print(f"[LISTENING] Server is listening on {SERVER_IP}")
	while True:
		conn, addr = server.accept()
		thread = threading.Thread(target=handle_client, args=(conn, addr))
		thread.start()
		print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()