# from serveur.client import send_to_serveur, recieve_from_serveur
# from serveur.client import shutdown_client, start_client
# from serveur.serveur import send_to_client, recieve_from_client
# from serveur.serveur import shutdown_servers, start_server
from unittest.mock import Mock

import serveur.client as client
import serveur.serveur as serveur

# -------------------------- Client ---------------------------
send_tabl_to_serveur = bytearray(3)
host = "127.0.0.1"
port = 9999


def test_recieve_from_serveur():
    client.sock = Mock()
    client.recieve_from_serveur()
    client.sock.recv.assert_called_with(1024)


def test_send_to_serveur():
    client.sock = Mock()
    client.send_to_serveur(send_tabl_to_serveur)
    client.sock.sendall.assert_called_with(send_tabl_to_serveur)


def test_start_client():
    client.socket = Mock()
    client.start_client(host, port)
    client.socket.socket.assert_called_with(client.socket.AF_INET,
                                            client.socket.SOCK_STREAM)
    client.sock = Mock()
    client.sock.connect((host, port))


def test_shutdown_client():
    client.sock = Mock()
    client.shutdown_client()
    if client.sock is True:
        client.sock.close()

# -------------------------- Serveur ---------------------------


def test_start_serveur():
    serveur.socket = Mock()
    # serveur.start_server(host, port)
    # serveur.socket.socket.assert_called_with(serveur.socket.AF_INET,
    #                                         serveur.socket.SOCK_STREAM)