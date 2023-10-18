import threading
import socket

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

def login(conn):
	user_name = conn.recv(BUF_SIZE).decode()
	return user_name

def broadcast(msg, conn):
	for client_conn in clients:
		if client_conn!=conn:
			client_conn.send(msg.encode())


def handle_client(conn, addr):
	print(f"[NEW CONNECTION] {addr} connected.")

	### check user login
	user_name = login(conn)

	### add client to clients:
	clients[conn] = user_name

	### send wellcome message
	conn.send(f'Welcome to the chat, {user_name}'.encode())

	connected = True
	while connected:
		msg = conn.recv(BUF_SIZE).decode(FORMAT)
		if msg == DISCONNECT_MESSAGE:
			connected = False

		msg_to_broadcast = f'<{clients[conn]}>: {msg}'
		print(f"{msg_to_broadcast}")

		broadcast(msg_to_broadcast, conn)



		# conn.send("Msg received".encode(FORMAT))

	conn.close()


def start():
	server.listen()
	print(f"[LISTENING] Server is listening on {SERVER_IP}")
	while True:
		conn, addr = server.accept()

		thread = threading.Thread(target=handle_client, args=(conn, addr))
		thread.start()
		print(f"[ACTIVE CLIENTS] {threading.activeCount() - 1}")


if __name__=="__main__":
	clients = {}
	print("[STARTING] server is starting...")
	start()