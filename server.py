import socket
clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 1234
clientSocket.bind((host,port))

clientSocket.connect((host,9999))

def sendMsg(flag):
    while flag == 0:
        message =input("YOU:")
        clientSocket.send(message.encode('ascii'))
        flag = 1
        receive(flag)

def receive(flag):
    while flag == 1:
        msg = str(clientSocket.recv(1024))
        print("SERVER:"+msg)
        flag = 0
        sendMsg(flag)

msg = str(clientSocket.recv(1024))
print(msg)
flag = 0
sendMsg(flag)
