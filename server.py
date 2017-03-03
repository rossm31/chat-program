import socket
import time

# Specify server address and port
host = '130.159.123.25'
port = 5000

print ("Server Started.")

clients = []

# Establish TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind server address and port
s.bind((host,port))

# Listen for x number of requests
s.listen(5)

# Servers are constant loops handling requests
connected = True
while connected:

    # Wait for a connection
    connect, address = s.accept()

    # Typically fork at this point
 
    # Specify max bytes to be received
    resp = (connect.recv(2048)).strip()
    # Add clients to address book
    if address not in clients:
        clients.append(address)

    # Send answer
    decoded_resp = resp.decode("utf-8")
    print(time.ctime()+": "+decoded_resp)
    

# Close connection when finished
connect.close()
print("\ndone"),address


 


