from unittest.mock import Mock

import Src.Network.client as client
import Src.Network.serveur as serveur

# -------------------------- Client ---------------------------
send_tabl_to_serveur = bytearray(3)
host = "127.0.0.1"
port = 9999


def test_recieve_from_serveur():
    client.sock = Mock()
    client.client_recieve_from_serveur()
    client.sock.recv.assert_called_with(1024)


def test_send_to_serveur():
    client.sock = Mock()
    pouet = object()
    client.client_send_to_serveur(pouet)
    client.sock.sendall.assert_called_with(pouet)


def test_start_client():
    client.socket = Mock()
    client.start_client(host, port)
    client.socket.socket.assert_called_with(client.socket.AF_INET,
                                            client.socket.SOCK_STREAM)
    client.sock = Mock()
    client.sock.connect((host, port))


def test_shutdown_client_not_none():
    client.sock = Mock()
    client.shutdown_client()
    client.sock.close.assert_called_with()


def test_shutdown_client_none():
    client.sock = None
    client.shutdown_client()
    # no attribute error

# -------------------------- Serveur ---------------------------


def test_get_socket():
    serveur.socket = Mock()

    serveur._get_socket()

    serveur.socket.socket.assert_called_with(serveur.socket.AF_INET,
                                             serveur.socket.SOCK_STREAM)


def test_start_serveur():
    socket = Mock()
    serveur._get_socket = Mock(return_value=socket)
    val1 = object()
    val2 = object()
    socket.accept = Mock(return_value=(val1, val2)) 

    serveur.start_server(host, port)

    serveur.sock.bind.assert_called_with((host, port))
    serveur.sock.listen.assert_called_with(1)
    assert serveur.addr_client == val1


def test_recieve_from_client():
    serveur.addr_client = Mock()
    serveur.serveur_recieve_from_client()
    serveur.addr_client.recv.assert_called_with(1024)


def test_send_to_client_addr_none(capsys):
    serveur.addr_client = None
    test = "test"
    serveur.serveur_send_to_client(test)
    out, err = capsys.readouterr()
    assert out == "Pas d'adresse client\n"


def test_send_to_client_addr_not_none():
    serveur.addr_client = Mock()
    test = object()
    serveur.serveur_send_to_client(test)
    serveur.addr_client.sendall.assert_called_with(test)


def test_shutdown_serveur():
    serveur.addr_client = Mock()
    serveur.sock = Mock()
    serveur.shutdown_server()
    serveur.addr_client.close.assert_called_with()
    serveur.sock.close.assert_called_with()