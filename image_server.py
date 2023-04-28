import socket
import os
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #this is the api that is provided by the socket library.
#this is the server

#AF_INET REPRESENTS IPV4 IN GENERAL
#TCP USES SOCK_STREAM
SERVER_HOST = "localhost" #this should be changed to create a multiuser system
server.bind((SERVER_HOST,5001)) #this is where we need to set up source ip address
#I can use local-host for now. ie... 127.0.0.1

server.listen()
current_path = os.path.abspath(os.path.dirname(__file__))
print(current_path)
images = os.listdir(current_path)

for _ in images:
    if _.endswith('.jpg'):
        print(_)

print('The server is listening and is ready!')
#now to accept incoming connections we need to make sure our server listens to requests

client_socket, client_address = server.accept()
file = open('server_image.jpg',"wb")
#file opens us a stream
#we can our manipulations here right after we have recieved the image.

image_chunk = client_socket.recv(2048) #I can receive 2MB of data at once, 
#this is like setting the stream buffer size

while image_chunk:
    file.write(image_chunk)
    image_chunk = client_socket.recv(2048)
# as we cannot send the image at onc e over the socket we send it chunk by chunk
print('image received')
file.close()
client_socket.close()