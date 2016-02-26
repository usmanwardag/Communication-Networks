from socket import *
import time

serverIP = '192.168.43.160'

sentence = raw_input('Input lowercase sentence:')
start = time.time()

serverPort = 80

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverIP,serverPort))

clientSocket.send(sentence)
modifiedSentence = clientSocket.recv(1024)
time_match = time.time()-start

print 'From Server:', modifiedSentence
clientSocket.close()

print 'It took', time_match, 'seconds to finish ObjectMatching.'

