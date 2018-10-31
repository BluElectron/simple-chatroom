import time
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)


try:
    myChats = open('myChats.txt', 'w+')
    myChats.close()
except:
    print("ERROR__cannot open file for writing")
# Timestamp + message

serverSocket.bind(('', serverPort))
welcome = welcome = "******************************************************\n* Welcome to...                                      *\n*         The CHAT ROOM OF DOOM AND GLOOM!!          *\n*                                                    *\n*                                                    *\n*                                                    *\n* Disclaimer - The CHAT ROOM OF DOOM AND GLOOM       *\n*              is not responsible for any trolls,    *\n*                dragons, mad portal-gun wielding    *\n*              scientists, power-hungry AIs, or      *\n*              ethereal-space creatures that         *\n*              may be using this platform.           *\n******************************************************"

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    message = message.decode()

    if message.startswith("WRITE__"):
        message = message[7:]
        print("Preparing to write...")
        try:
            myChats = open('myChats.txt', 'a')
            myChats.write(time.ctime()+"  : "+message+"\n")
            myChats.close()
            serverSocket.sendto(("OKAY").encode(), clientAddress)
        except:
            serverSocket.sendto(("ERROR__cannot append to file").encode(), clientAddress)

    elif message == "GET":
        try:
            with open('myChats.txt', 'r') as newfile:
                chats = "FILE__"+newfile.read()
                serverSocket.sendto((chats).encode(), clientAddress)
        except:
            serverSocket.sendto(("ERROR__cannot read file").encode(), clientAddress)
    elif message == "JOIN":
        serverSocket.sendto(welcome.encode(), clientAddress)

    else:
        serverSocket.sendto(("ERROR__you entered something invalid").encode(), clientAddress)

serverSocket.close()

