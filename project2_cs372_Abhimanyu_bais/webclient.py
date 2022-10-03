

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('localhost', 7777))
print("Connected to localhost at 7777")

while True:

    message = str(input(">")) 
    s.send(message.encode())

    if message == "/q":
        s.close()
        break

print("Connection closed")