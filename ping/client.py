from socket import *
import time
import sys

def ping(host, port):
    resps = []
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.settimeout(1) # reference: https://docs.python.org/3/library/socket.html#socket.socket.settimeout

    for seq in range(1,11):
        # Send ping message to server and wait for response back
        # On timeouts, you can use the following to add to resps
        # resps.append((seq, 'Request timed out', 0))
        # On successful responses, you should instead record the server
        # response and the RTT (must compute server_reply and rtt properly)
        # resps.append((seq, server_reply, rtt))

        # Fill in start
        clientTime = time.time()
        message = f'Ping {seq} {clientTime}'
        clientSocket.sendto(message.encode(), (host, port))
        try:
            reply, _ = clientSocket.recvfrom(2048)
            rtt = time.time() - clientTime
            reply = reply.decode()
            print(reply)
            print(rtt)
            resps.append((seq, reply, rtt))
        except timeout:
            print('Request timed out')
            resps.append((seq, 'Request timed out', 0))

    clientSocket.close()
        # Fill in end

    return resps

if __name__ == '__main__':
    resps = ping('127.0.0.1', 12000)
    print(resps)