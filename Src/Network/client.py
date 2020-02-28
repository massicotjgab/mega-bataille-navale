import socket
import threading
import queue

send_tabl_to_serveur = bytearray(3)
send_tabl_to_serveur[0] = 2
send_tabl_to_serveur[1] = 8
send_tabl_to_serveur[2] = 7

sock = None

queue_recieve_from_gui = queue.Queue()
queue_send_to_gui = queue.Queue()
queue_close_client = queue.Queue()


def start_client(host, port):
    global sock
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))


def shutdown_client():
    if sock is not None:
        sock.close()


def client_recieve_from_serveur():
    return sock.recv(1024)


def client_send_to_serveur(send_tabl_to_serveur):
    sock.sendall(send_tabl_to_serveur)


def gui_shutdown():
    queue_close_client.put("stop")


def gui_send(data):
    queue_recieve_from_gui.put(data)


def gui_recieve():
    return queue_send_to_gui.get()


def thread(host, port):
    start_client(host, port)
    while queue_close_client.empty():
        try:
            client_send_to_serveur(queue_recieve_from_gui.get(block=False))
            queue_send_to_gui.put(client_recieve_from_serveur())
        except queue.Empty:
            pass
    shutdown_client()


def start_thread(host, port):
    run_thread = threading.Thread(target=thread,
                                  args=(host, port))
    run_thread.start()


if __name__ == "__main__":
    start_thread("localhost", 9999)
    gui_send(send_tabl_to_serveur)
    print(gui_recieve())
    gui_shutdown()
