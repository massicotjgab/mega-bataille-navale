import socket
# import time

message = bytearray(3)
message[0] = 3
message[1] = 3
message[2] = 3

addr_client = None
sock = None
# https://docs.python.org/3/library/queue.html#queue.Queue.join


def start_server(host, port):
    global sock
    global addr_client
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(1)
    addr_client, address = sock.accept()


def send_to_client(message):
    if addr_client is None:
        print("Pas d'addresse client")
    else:
        addr_client.sendall(message)


def recieve_from_client():
    return addr_client.recv(1024)


def shutdown_server():
    addr_client.close()
    sock.close()


if __name__ == "__main__":
    start_server("localhost", 9999)
    print(f"Sent:   {message}")
    send_to_client(message)
    print(f"Recieve: {recieve_from_client()}")
    # time.sleep(2)
    shutdown_server()
