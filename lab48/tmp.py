import socket


host_name=socket.gethostname()
host_ip = socket.gethostbyname(host_name)

print(f'host_name: {host_name}')
print(f'host_ip: {host_ip}')