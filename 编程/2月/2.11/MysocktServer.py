__author__ = "Narwhale"

import socketserver

class Mysocketserver(socketserver.BaseRequestHandler):

    def handle(self):
        try:
            while True:
                self.data = self.request.recv(1024).strip()
                print("{} wrote:".format(self.client_address[0]))
                print(self.data)
                self.request.sendall(self.data.upper())

        except ConnectionResetError as e:
            print(e)

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    #server = socketserver.TCPServer((HOST,PORT),Mysocketserver)           #单线程
    server = socketserver.ThreadingTCPServer((HOST,PORT),Mysocketserver)    #多线程

    server.serve_forever()