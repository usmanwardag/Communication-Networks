from socket import *

serverPort = 12003

# Create TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Associating serverPort with socket, this serverSocket
# is the welcome socket
serverSocket.bind(("", serverPort))

# Wait for client to send data
serverSocket.listen(1)

print 'The server is ready to receive'

while 1:

    # When client sends data, .accept() method is
    # invoked and connectionSocket is created
    connectionSocket, addr = serverSocket.accept()
    print 'connectionSocket is created'

    sentence = connectionSocket.recv(1024)
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence)
    connectionSocket.close()

print "Done"