import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('127.0.0.1', 7777)
s.bind(addr)
s.listen(5)

print("Server Listening on: " + str(addr[0]) + " at port: " + str(addr[1]))


while True:
    client, addr = s.accept()
    print("Accepted connection from: " + str(addr))
    print("Waiting for client to send message...")
    response = client.recv(4500).decode('utf-8')

    if response == "/q":
        client.close()
        s.close()
        sock.close()
        break

    print(response)
    x = response
    y = 4600
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((f"{response}", 80))
    sock.sendall(bytes(f"GET / HTTP/1.1\r\nHost:{response}\r\n\r\n", "utf-8"))
    info = sock.recv(4500)
    client.sendall(info)
    client.close()
    sock.close()

print("Connection closed")
