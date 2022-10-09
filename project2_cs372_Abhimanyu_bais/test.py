import socket
test = "www.example.com"
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("www.example.com", 80))
sock.send(b"GET / HTTP/1.1\r\nHost:test\r\n\r\n")
response = sock.recv(4096)
sock.close()
print(response.decode())