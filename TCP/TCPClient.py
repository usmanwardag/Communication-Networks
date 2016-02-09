from socket import *

serverName = '192.168.1.4'
serverPort = 12003

# Create client's socket. AF_INET indicates IPV4 network.
# SOCK_STREAM that TCP socket is being created.
clientSocket = socket(AF_INET, SOCK_STREAM)

# Initiates connection between client and server
clientSocket.connect((serverName, serverPort))
print 'Connection established!'

sentence = raw_input('Input lowercase sentence:')
clientSocket.send(sentence)

# Wait for bytes from server
modifiedSentence = clientSocket.recv(1024)

print 'From Server:', modifiedSentence
clientSocket.close()

