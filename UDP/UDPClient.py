from socket import *
import time

message = raw_input("Input lowercase sentence:")

start = time.time()
serverName = '192.168.43.160'
serverPort = 80
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.sendto(message,(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)


time_match = time.time()-start

print modifiedMessage
clientSocket.close()

print 'It took', time_match, 'seconds to finish ObjectMatching.'

