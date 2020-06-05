#client
import socket
client=socket.socket()
host=socket.gethostname()
port=1000
client.connect((host,2000))
while (True):
    totalmsg=''
    while (True):
        msg=client.recv(1024)
        msg=msg.decode("ASCII")
        totalmsg+=msg
        if (totalmsg[-3:]=='EOD'):
            break
    totalmsg=totalmsg[0:-3]
    print("Server : ",totalmsg)
    if ('Bye!' in totalmsg or 'BYE!' in totalmsg):
        client.close()
        break
    else:
        msg=input("Client : Enter your message\t")
        msg=msg+'EOD'
        client.send(msg.encode("ASCII"))
