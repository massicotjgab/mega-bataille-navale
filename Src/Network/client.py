import socket
# import time

sock = None
send_tabl_to_serveur = bytearray(3)
send_tabl_to_serveur[0] = 2
send_tabl_to_serveur[1] = 8
send_tabl_to_serveur[2] = 7


def start_client(host, port):
    global sock
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))


def shutdown_client():
    if sock is not None:
        sock.close()


def recieve_from_serveur():
    return sock.recv(1024)


def send_to_serveur(send_tabl_to_serveur):
    sock.sendall(send_tabl_to_serveur)


if __name__ == "__main__":
    start_client("localhost", 9999)
    print("Sent:     {}".format(send_tabl_to_serveur))
    # time.sleep(3)
    send_to_serveur(send_tabl_to_serveur)
    print(f"Recieve  {recieve_from_serveur()}")
    shutdown_client()
