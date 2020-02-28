import socket
import threading
import queue

message = bytearray(3)
message[0] = 3
message[1] = 3
message[2] = 3

addr_client = None
sock = None

queue_recieve_from_gui = queue.Queue()
queue_send_to_gui = queue.Queue()
queue_close_server = queue.Queue()


def _get_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def start_server(host, port):
    global sock
    global addr_client
    sock = _get_socket()
    sock.bind((host, port))
    sock.listen(1)
    addr_client, _ = sock.accept()


def serveur_send_to_client(message):
    if addr_client is None:
        print("Pas d'adresse client")
    else:
        addr_client.sendall(message)


def serveur_recieve_from_client():
    return addr_client.recv(1024)


def shutdown_server():
    addr_client.close()
    sock.close()


def gui_shutdown():
    queue_close_server.put("stop")


def gui_send(data):
    queue_recieve_from_gui.put(data)


def gui_recieve():
    return queue_send_to_gui.get()


def thread(host, port):
    start_server(host, port)
    while queue_close_server.empty():
        queue_send_to_gui.put(serveur_recieve_from_client())
        serveur_send_to_client(queue_recieve_from_gui.get())
    shutdown_server()


if __name__ == "__main__":
    start_thread = threading.Thread(target=thread,
                                    args=("localhost", 9999))
    start_thread.start()
    print(gui_recieve())
    gui_send(message)
    gui_shutdown()
