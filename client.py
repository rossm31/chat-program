import time
import socket
import threading

# Create thread lock (ask Ross Milligan)
tLock = threading.Lock()

# Set up a TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect as client to selected server
# on a specified port
s.connect(('130.159.123.25',5000))

# Create alias for client
alias = input("Name: ")

# Tell server client has connected
s.send((alias + " has connected.").encode("utf-8"))

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

        
# Close the connection when completed
s.close()
print("\ndone")
