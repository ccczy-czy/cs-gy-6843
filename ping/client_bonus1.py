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
            resps.append((seq, reply, rtt))
        except timeout:
            resps.append((seq, 'Request timed out', 0))

    clientSocket.close()
    validRTTs = [rtt for _, reply, rtt in resps if reply != "Request timed out"]
    print(f'--- {host} ping statistics ---')
    print(f'{len(resps)} packets transmitted, {len(validRTTs)} packets received, {(len(resps) - len(validRTTs)) / len(resps) * 100}% packet loss')
    if len(validRTTs) > 0:
        print(f'round-trip min/avg/max/ = {min(validRTTs)}/{sum(validRTTs) / len(validRTTs)}/{max(validRTTs)} s')
        # Fill in end

    return resps

if __name__ == '__main__':
    resps = ping('127.0.0.1', 12000)
    print(resps)