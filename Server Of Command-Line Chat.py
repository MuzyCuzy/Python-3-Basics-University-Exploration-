#server
import socket
server=socket.socket()
host=socket.gethostname()
port=2000
server.bind((host,port))
server.listen(5)
client,add=server.accept()
while (True):
    totalmsg=''
    msg=input("Server : Enter your message\t")
    msg=msg+'EOD'
    client.send(msg.encode("ASCII"))
    if ('Bye!' in msg[0:-3] or 'BYE!' in msg[0:-3]):
        server.close()
        break
    else:
        server.listen(5)
        while (True):
            msg=client.recv(1024)
            msg=msg.decode("ASCII")
            totalmsg+=msg
            if (totalmsg[-3:]=='EOD'):
                break
        totalmsg=totalmsg[0:-3]
        print("Client : ",totalmsg)
