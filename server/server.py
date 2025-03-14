import socket
from _thread import *
import pickle
import numpy as np
from .config_IP import IP, PORT

class Server:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((IP, PORT))
        self.server.listen(2)
        self.player = 0
        self.seed = np.random.randint(10000)
        self.ready = False
        self.events = [None, None]

    def threaded_client(self, conn):
        conn.send(pickle.dumps([self.player, self.seed]))
        player = self.player
        self.player += 1
        if player == 1:
            self.ready = True
        while True:
            try:
                data = pickle.loads(conn.recv(2048))
                if data == "waiting":
                    conn.sendall(pickle.dumps(self.ready))
                elif data == "playing":
                    conn.sendall(pickle.dumps(self.ready))
                elif data == "connected":
                    if self.ready:
                        conn.sendall(pickle.dumps(self.events[player]))
                    else:
                        conn.sendall(pickle.dumps("disconnected"))
                else:
                    if player == 0:
                        self.events[1] = data
                        self.events[0] = None
                    else:
                        self.events[0] = data
                        self.events[1] = None
                    conn.sendall(pickle.dumps(self.ready))
            except:
                break

        print("Lost connection")
        self.player = player
        self.events = [None, None]
        self.ready = False
        conn.close()

server = Server()
print("Waiting for a connection, Server Started")

while True:
    conn, addr = server.server.accept()
    print("Connected to:", addr)
    start_new_thread(server.threaded_client, (conn,))
