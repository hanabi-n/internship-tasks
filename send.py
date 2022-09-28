import socket
import pickle
import mainClass


def client_program():
    host = socket.gethostname()  # connection in the same computer
    port = 5000  # socket

    client_socket = socket.socket()
    client_socket.connect((host, port))

    message = input(" -> ")  # take input and test connection
    client_socket.send(message.encode())

    while message.lower().strip() != 'bye':  # break loop

        test = mainClass.mainContent()
        client_socket.send(pickle.dumps(test))

        print('pickle sent')
        message = input(" -> ")  # again write smt

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()
