from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
# get the hostname of myserver easier for us to reach and copy
host = gethostname()
# print the host so we would know what it is
print(host)
port = 10000
# create a vector with the hostname and port (random port we chose)
server_address = (host, port)

# binding the socket to the specific address
serverSocket.bind(server_address)
# listen to only 1 connection at a time.
serverSocket.listen(1)
# Prepare a sever socket
# Fill in start
# Fill in end
while True:
    # Establish the connection
    print('Ready to serve...')

    # establishing the connection

    connectionSocket, addr = serverSocket.accept()
    # print("connection established")
    try:
        # receive the message
        message = connectionSocket.recv(1024).decode()
        # your code (gets the request from the message and open a file accordingly then remove the / from the start and opens if the file exists)
        filename = message.split()[1]
        f = open(filename[1:])
        # creating the response according to the message header and html file
        # outputdata = 'HTTP/1.1 200 OK\n'
        # outputdata += 'Content-Type: text/html\n\n'
        outputdata = f.read()
        connectionSocket.send('''HTTP/1.1 200 OK\nContent-Type: text/html\n\n'''.encode())
        # closing the file
        f.close()
        # Fill in start       #Fill in end
        # Send one HTTP header line into socket
        # Fill in start
        # Fill in end
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        # print("message sent")
        connectionSocket.close()
    except IOError:
        # returns not found in case of an error as requested
        outputdata = 'HTTP/1.1 404 Not Found\n'
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()