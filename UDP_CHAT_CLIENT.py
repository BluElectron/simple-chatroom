from socket import *
serverName = '127.0.0.1'
serverPort = 12000



clientSocket = socket(AF_INET, SOCK_DGRAM)

clientSocket.sendto(("JOIN").encode(), (serverName, serverPort))
message, serverAddress = clientSocket.recvfrom(2048)
print(message.decode())

response = ""
while(response!="0"):
    print("\n**************************************")
    print("*                MENU                  *")
    print("* 0. QUIT                              *")
    print("* 1. SEND MESSAGE                      *")
    print("* 2. GET CHAT LOG                      *")
    print("****************************************")

    response = input()

    if (response =="1"):
        chat = input("Enter message>>>")
        chat = "WRITE__"+chat
        clientSocket.sendto((chat).encode(), (serverName, serverPort))
        message, serverAddress = clientSocket.recvfrom(2048)

    elif (response == "2"):
        clientSocket.sendto(("GET").encode(), (serverName, serverPort))
        message, serverAddress = clientSocket.recvfrom(2048)
        message = message[6:]
        print(message.decode())
    elif (response=="0"):
        print("Goodbye, thanks for chatting!")

    else:
        print("You entered an invalid option. Try again!")

clientSocket.close()

