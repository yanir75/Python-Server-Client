import time
from socket import *
target_port = 10000  # create a socket object
client = socket(AF_INET, SOCK_STREAM)
host = gethostname()
# connect the client
client.connect((host, target_port))

# send some data
request = f'GET /helloworld.html'
client.send(request.encode())

# receive some data
try:
    time.sleep(2)
    response = client.recv(4096).decode()
    print(response)
except:
    print("error")

# display the response

