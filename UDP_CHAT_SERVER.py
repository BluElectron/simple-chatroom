# Alison Hart
# UDP Chat Server
# Receives information from the associated client and executes instructions based on string contents 

import time
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Create new chatfile on server-side to store chats
try:
    myChats = open('myChats.txt', 'w+')
    myChats.close()
except:
    print("ERROR__cannot open file for writing")
    
# Timestamp + message

serverSocket.bind(('', serverPort)) # bind to port

# Welcome message contents
welcome = welcome = "******************************************************\n* Welcome to...                                      *\n*         The CHAT ROOM OF DOOM AND GLOOM!!          *\n*                                                    *\n*                                                    *\n*                                                    *\n* Disclaimer - The CHAT ROOM OF DOOM AND GLOOM       *\n*              is not responsible for any trolls,    *\n*                dragons, mad portal-gun wielding    *\n*              scientists, power-hungry AIs, or      *\n*              ethereal-space creatures that         *\n*              may be using this platform.           *\n******************************************************"


# While server is running, continue:
while True:
    
    message, clientAddress = serverSocket.recvfrom(2048) # Receive message from client and decode
    message = message.decode()

    if message.startswith("WRITE__"):   # WRITE__ indicates to write new chat to file
        message = message[7:]           # Clean string, prepare for writing
        print("Preparing to write...")
        
        try:
            myChats = open('myChats.txt', 'a')      # open chatfile, add timestamp
            myChats.write(time.ctime()+"  : "+message+"\n")
            myChats.close()
            
            serverSocket.sendto(("OKAY").encode(), clientAddress)   # OKAY response to client
        except:
            serverSocket.sendto(("ERROR__cannot append to file").encode(), clientAddress)

    elif message == "GET":              # GET indicates to return contents of chatfile
        try:
            with open('myChats.txt', 'r') as newfile:
                chats = "FILE__"+newfile.read()
                serverSocket.sendto((chats).encode(), clientAddress)
        except:
            serverSocket.sendto(("ERROR__cannot read file").encode(), clientAddress)
            
    elif message == "JOIN":             # JOIN indicates to get initial greeting message
        serverSocket.sendto(welcome.encode(), clientAddress)

    else:
        serverSocket.sendto(("ERROR__you entered something invalid").encode(), clientAddress)

serverSocket.close()                    # close connection

