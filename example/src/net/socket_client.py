import socket
import sys

HOST, PORT = "localhost", 8080
data = " ".join(sys.argv[1:])

print "Sent:     {}".format(data)

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    print "Connect to {0}:{1}".format(HOST, PORT)
    for i in range(100):
        sock.sendall(data + str(i) + "\n")
        # Receive data from the server and shut down
        received = sock.recv(1024)
        print "Received: {}".format(received)
finally:
    sock.close()



