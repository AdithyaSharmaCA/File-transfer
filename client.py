import socket
from scapy.all import *

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

SERVER_IP = ""
PORT = 5001
client.connect((SERVER_IP,PORT))

#request = input('Enter the name of the image that you are looking for, from the server contents')

file = open("cn_lab.jpg",'rb')

image_data = file.read(2048)

i = 0
while image_data:
    print("sending image chunk ",i)
    client.send(image_data)
    #print(image_data)
    image_data = file.read(2048)
    i = i+1
print("Image sent")
file.close()
client.close()
