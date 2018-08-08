__author__ = "Narwhale"
import socket

obj = socket.socket()
obj.connect(("localhost",8080))

ret = str(obj.recv(1024),encoding="utf-8")
print(ret)

obj.close()