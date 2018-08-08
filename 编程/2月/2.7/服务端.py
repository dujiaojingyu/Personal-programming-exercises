__author__ = "Narwhale"
import socket

sk = socket.socket()
sk.bind(("localhost",8080))
sk.listen()

conn,address = sk.accept()
conn.sendall(bytes("Hello world",encoding="utf-8"))