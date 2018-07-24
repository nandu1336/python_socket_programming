import socket

serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999
serverSocket.bind((host,port))

#listen upto 5 requests from the clients
serverSocket.listen(5)

#accept the request 
clientsocket,addr = serverSocket.accept()      
print("Got a connection from %s" % str(addr))    
msg = str("Thank you for connecting" + "\n")
clientsocket.send(msg.encode('ascii'))

#serverSocket.connect((host,1234))

flag = 1

def sendMsg(flag):
        while flag == 0:
                Msg = input("YOU:")
                clientsocket.send(Msg.encode('ascii'))
                flag = 1
                receiveMsg(flag)

def receiveMsg(flag):
        while flag ==1 :
                gotIt = str(clientsocket.recv(1024))
                print("CLIENT:"+gotIt)
                flag = 0
                sendMsg(flag)

receiveMsg(flag)
