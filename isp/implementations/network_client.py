from interfaces.network_connectable import NetworkConnectable
from interfaces.data_sendable import DataSendable
from interfaces.data_receivable import DataReceivable

class NetworkClient(NetworkConnectable, DataSendable, DataReceivable):

    def connect_to_server(self, ip, port):
        print(f"Connected to {ip}:{port}")

    def send_data(self, data):
        print("Sending data")

    def receive_data(self):
        print("Receiving data")
