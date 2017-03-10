import time
import socket
import threading
import sys

# Create alias for client
alias = input("Name: ")

# Create thread lock (ask Ross Milligan)
tLock = threading.Lock()

# Set up a TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect as client to selected server
# on a specified port
s.connect(('130.159.123.8',5000))

# Send server alias
s.send(alias.encode("utf-8"))

# Let client type message
message = input(alias + "->")

# Convert to bytes and display message
while message != "END PROGRAM":
    if message != "":
        s.send((alias + ": " + message).encode("utf-8"))
    tLock.acquire()
    message = input(alias + "->")
    tLock.release()
    time.sleep(0.2)

    #ISSUE WITH 'CONNECT' WHEN TRYING TO RECEIVE DATA AS CLIENT
    resp = (s.recv(2048)).strip()
    decoded_resp = resp.decode("utf-8")
    print(time.ctime()+": "+decoded_resp)
            

        
# Close the connection when completed
s.close()
print("\ndone")
