import cv2
import socket
import numpy
import pickle
from ultralytics import YOLO

# Load the model
model = YOLO("yolov8x.pt")

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set the buffer size to the maximum allowed value
max_buffer_size = sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, max_buffer_size)
print(max_buffer_size)

server_ip = "192.168.137.204"
server_port = 8000
sock.bind((server_ip, server_port))

chunk_size = 1450  # Chunk size for data transfer

received_data = b""  # Accumulate received data

while True:
    datagram, addr = sock.recvfrom(chunk_size)
    received_data += datagram
    
    # Check if a complete frame has been received
    if len(datagram) < chunk_size:
        try:
            data = pickle.loads(received_data)
            img = cv2.imdecode(data, cv2.IMREAD_COLOR)
            
            # Perform model prediction on the received frame
            model.predict(source=img, show=True)
            
            received_data = b""  # Reset the received data
            
        except Exception as e:
            print("Error occurred:", e)
        
    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the resources
cv2.destroyAllWindows()
