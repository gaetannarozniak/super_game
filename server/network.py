import socket
import pickle
from .config_IP import IP, PORT

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addr = (IP, PORT)
        connection = self.connect()
        self.player = connection[0]
        self.seed = connection[1]

    def get_player(self):
        return self.player
    
    def get_seed(self):
        return self.seed

    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048))
        except:
            raise Exception("Couldn't connect to server")

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)