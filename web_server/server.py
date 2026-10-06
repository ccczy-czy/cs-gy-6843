# import socket module
from socket import *
import sys # In order to terminate the program
from threading import Thread

def handleRequest(connectionSocket):
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]

        f = open(filename[1:])
        outputdata = f.read()
        f.close()

        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())

        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())

        connectionSocket.close()
    except IOError:
        connectionSocket.send('HTTP/1.1 404 Not Found\r\n\r\n'.encode())
        connectionSocket.close()

def webServer(port=6789):
    serverSocket = socket(AF_INET, SOCK_STREAM) # Prepare a server socket

    serverSocket.bind(('', port))

    serverSocket.listen(128)

    try:
        while True:
            # Establish the connection
            print('Ready to serve...')
            connectionSocket, addr = serverSocket.accept()

            clientThread = Thread(target=handleRequest, args=(connectionSocket,), daemon=True)

            clientThread.start()
    except KeyboardInterrupt:
        print("Stopping server...")
        serverSocket.close()
        sys.exit() # Terminate the program after sending the corresponding data

if __name__ == "__main__":
    webServer(6789)