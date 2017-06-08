import socket

host = '127.0.0.1' #ip of your client device.
port = 5560

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

while True:
    cammand = raw_input("enter your cammand : ")
    if cammand == 'EXIT':
        s.send(str.encode(cammand))
        break
    elif cammand == 'KILL':
        s.send(str.encode(cammand))
        break
    s.send(str.encode(cammand))
    reply = s.recv(1024)
    print (reply.decode('utf-8'))
   
    
s.close()
