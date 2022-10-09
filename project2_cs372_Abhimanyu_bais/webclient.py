import socket
import sys
print(sys.argv)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('127.0.0.1', 7777))
print("Connected to localhost at 7777")
s.send(sys.argv[1].encode())
print("Waiting for server to send message...")

response = ''
while True:
    msg = s.recv(32)
    if len(msg) <= 0:
        break
    response += msg.decode("ISO-8859-1")

print(response)
s.close()
print("Connection closed")