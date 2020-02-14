import socket
# import time

sock = None
message = bytearray(3)
message[0] = 2
message[1] = 8
message[2] = 7


def start_client(host, port):
    global sock
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))


def shutdown_client():
    if sock is not None:
        sock.close()


def recieve_from_serveur():
    return sock.recv(1024)


def send_to_serveur(message):
    sock.sendall(message)


if __name__ == "__main__":
    start_client("localhost", 9999)
    print("Sent:     {}".format(message))
    # time.sleep(3)
    send_to_serveur(message)
    print(f"Recieve  {recieve_from_serveur()}")
    shutdown_client()
