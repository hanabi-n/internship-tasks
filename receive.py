import pickle
import socket


def server_program():
    host = socket.gethostname()
    port = 5000
    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))

    message = conn.recv(1024).decode()

    print('Received message from send.py: ', message)  # ------test

    try:
        while True:
            data = conn.recv(1024)
            data = pickle.loads(data)
            print("From sender: ", data)
    except EOFError:
        print('Connection closed')
        conn.close()  # close the connection


if __name__ == '__main__':
    server_program()
