import zmq
context = zmq.Context()
#subscribing
data_socket = context.socket(zmq.SUB)
data_socket.subscribe("")
#Connecting to specified Nimble Port
data_socket.connect("tcp://localhost:22960")
data_socket.setsockopt_string(zmq.SUBSCRIBE,'')
print("connected")
#Receiving data from specified Nimble port 
message = data_socket.recv()
while data_socket.getsockopt(zmq.RCVMORE):
   message+=data_socket.recv()
#printing the data received from Nimble port   
print(message)
print("Data Received")

