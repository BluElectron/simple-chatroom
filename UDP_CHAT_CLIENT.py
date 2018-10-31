# Alison Hart
# UDP Chat Client
# Connects to local (or network) server IP for chatting purposes


from socket import *
serverName = '127.0.0.1'
serverPort = 12000


# initialize socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

clientSocket.sendto(("JOIN").encode(), (serverName, serverPort))
message, serverAddress = clientSocket.recvfrom(2048)
print(message.decode())

response = ""


while(response!="0"):       # While user wants to continue:
    
    # Menu
    
    print("\n**************************************")
    print("*                MENU                  *")
    print("* 0. QUIT                              *")
    print("* 1. SEND MESSAGE                      *")
    print("* 2. GET CHAT LOG                      *")
    print("****************************************")

    response = input()

    
    if (response =="1"):    # SEND MESSAGE
        chat = input("Enter message>>>")
        chat = "WRITE__"+chat
        clientSocket.sendto((chat).encode(), (serverName, serverPort))
        message, serverAddress = clientSocket.recvfrom(2048)

    elif (response == "2"):  # GET CHAT LOG
        clientSocket.sendto(("GET").encode(), (serverName, serverPort))
        message, serverAddress = clientSocket.recvfrom(2048)
        message = message[6:]
        print(message.decode())
        
    elif (response=="0"):   # QUIT
        print("Goodbye, thanks for chatting!")

    else:                   # INVALID CHOICE
        print("You entered an invalid option. Try again!")

clientSocket.close()        # Close connection

