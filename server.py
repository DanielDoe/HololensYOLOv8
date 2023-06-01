import cv2
import socket
import numpy
import pickle
import struct
from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor

MTU_BUF_SIZE = 100000000

# Load the model
model = YOLO("yolov8x.pt")

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set the buffer size to the maximum allowed value
#max_buffer_size = sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
#sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, max_buffer_size)
#print(max_buffer_size)
# Receive data
#data, addr = sock.recvfrom(max_buffer_size)

server_ip="192.168.137.204"
server_port= 8000
sock.bind((server_ip,server_port))
sock.listen()

data = b""
payload_size = struct.calcsize("Q")

while True:
    client_socket, addr = sock.accept()
    print("Connection from:", addr)
    
    if client_socket:
        while (len(data)) < payload_size:
            packet = client_socket.recv(4*1024)
            if packet: 
                data += packet
            else:
                break
        
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("Q", packed_msg_size)[0]

        while len(data) < msg_size:
            data += client_socket.recv(4*1024)
        
        frame_data = data[:msg_size]
        data = data[msg_size:]

        frame = pickle.loads(frame_data)
        # frame_img = cv2.imdecode(frame, cv2.IMREAD_COLOR)
        # model.predict(source=frame_img, show=True)
        # cv2.imshow("receiving...", frame_img)
        # key = cv2.waitKey(10)
        frame = pickle.loads(frame_data)
        cv2.imshow("receiving...", frame)
        key = cv2.waitKey(10)
        if key == 13:
            break

        client_socket.close()
        
    # datagram, addr = sock.recvfrom(1000000000)
    # data=pickle.loads(datagram)
    # #print(type(data))
    # data = cv2.imdecode(data, cv2.IMREAD_COLOR)
    # model.predict(source=data, show=True)
    # #cv2.imshow('server', data) #to open image
    # # Press 'q' to exit
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break


# Release the resources
# cap.release()
cv2.destroyAllWindows()