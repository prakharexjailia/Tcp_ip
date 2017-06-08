import socket

host = ''
port = 5560
BUFFER_SIZE = 1024

storedValue = "hello I am server"

def setupServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("socket created")
    try:
        s.bind((host,port))
    except socket.error as msg:
        print(msg)
    print("socket bind complete")
    return s
def setupConnection():
    s.listen(1)  #allow one connection
    conn,address = s.accept()
    print("Connected to : " + str(address))
    return conn

def GET():
    reply = storedValue
    return reply

def REPEAT(dataMessage):
    reply = dataMessage[1]
    return reply 

def dataTransfer(conn):
    #loop send receive  data
    while True:
        #receive the data
        data = conn.recv(1024) #reveive the data
        data = data.decode('utf-8')
        #split data such that you separate the cammand from rest of data 
        dataMessage = data.split(' ',1)
        cammand = dataMessage[0]
        if cammand == 'GET':
            reply = GET()
        elif cammand == 'REPEAT':
            reply = REPEAT(dataMessage)
        elif cammand == 'EXIT':
            print("cilent left")
            break
        elif cammand == 'KILL':
            print ("our server sutting down.")
            s.close()
            break
        else:
            reply = 'Unknown Cammand'

        conn.sendall(str.encode(reply))
        print("data has been sent")
    conn.colse()          


s = setupServer()

while True:
    try:
        conn = setupConnection()
        dataTransfer(conn)
    except socket.error as msg:
        print(msg)
        break

