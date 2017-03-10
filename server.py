import socket
import time
import sys
import threading

# Specify server address and port
host = '130.159.123.8' 
port = 5000
print('Host: ' + host + '\nPort: ' + str(port))

clients = []
print('Client list created')

# Establish TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

# Bind server address and port
try:
        s.bind((host,port))
except socket.error as msg:
        print('Bind failed. Error code: ' + str(msg[0]) + ' Message' + msg[1])
        sys.exit()
print('Socket bind complete')

# Listen for x number of requests
s.listen(5)
print('Socket now listening')

# Function for handling connections.  This will be used to create threads
def clientthread(connect):
        # sending message to connected client
        connect.send(('Welcome to the server!\n').encode('utf-8'))

        # infinite loop so that function do not terminate and thread do not end
        while True:

                # Typically fork at this point
     
                # Specify max bytes to be received
                resp = (connect.recv(2048)).strip()
                # Add clients to address book
                if connect not in clients:
                        clients.append(connect)

                # Send answer
                decoded_resp = resp.decode("utf-8")
                print(time.ctime()+": "+decoded_resp)
                for conn in clients:
                        conn.send(resp)

                
        # Close connection when finished
        connect.close()
        print("\ndone"+address)

# now keep talking with the client
while 1:
        # wait to accept a connection - blocking call
        connect, address = s.accept()
        alias = ((connect.recv(512)).strip()).decode('utf-8')
        print(time.ctime()+ ': ' + address[0] + ' (' + alias + ')' + ' has connected.')
        #start new thread takes 1st argument as a function name to be run,
        #second is the tuple of arguments to the function.
        threading.Thread(target=clientthread,args=(connect, )).start()
        
s.close
