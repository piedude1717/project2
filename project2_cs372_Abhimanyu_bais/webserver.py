import socket

addr = ('localhost', 7777)


s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen()

print("Server Listening on: " + str(addr[0]) + " at port: " + str(addr[1]))

client, addr = s.accept()
print("Accepted connection from: " + str(addr))


while True:
    print("Waiting for client to send message...")
    response = client.recv(4500).decode()
    print(response)

    if str(response) == "/q":
        client.close()
        s.close()
        break

    if str(response) == "www.eample.com":
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((response, 80))
        sock.send(b"GET / HTTP/1.1\r\nHost:www.example.com\r\n\r\n")
        response = sock.recv(4096)
        client.send(response)
        sock.close()


print("Connection closed")
