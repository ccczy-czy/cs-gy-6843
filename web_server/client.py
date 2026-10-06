# import socket module
from socket import *
# for reading arguments from command line
import sys

def httpClient(serverHost, serverPort, filename):
    # create a client socket
    clientSocket = socket(AF_INET, SOCK_STREAM)

    # connect to server using server address and server port number
    clientSocket.connect((serverHost, serverPort))

    # HTTP Reuqest request line
    request = f"GET {filename} HTTP/1.1\r\nHost: {serverHost}\r\n\r\n"
    # sends the request through socket
    clientSocket.send(request.encode())

    # variable for holding response
    response = ""
    while True:
        # while there's still data, read 1024 bytes at a time and decode from bytes into string
        data = clientSocket.recv(1024).decode()
        if not data:
            break
        # append to response
        response += data

    # print our received response
    print(response)
    # close connection
    clientSocket.close()

if __name__ == "__main__":
    # if format is not right, prompt user
    if len(sys.argv) != 4:
        print("Usage: python client.py <server_host> <server_port> <filename>")
        sys.exit(1)

    # get server address
    host = sys.argv[1]
    # get port number
    port = int(sys.argv[2])
    # get file path
    path = sys.argv[3]
    # run http client
    httpClient(host, port, path)