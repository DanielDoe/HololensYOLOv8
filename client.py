import cv2
import socket 
import pickle
import os
import numpy as np
import time
import struct

MTU_BUF_SIZE = 185


# s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# s.setsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF,100000000)
server_ip = "192.168.137.204"
server_port = 8000

client_socket.connect((server_ip, server_port))
data = b""

# cap = cv2.VideoCapture("https://danieldoe:Doe@7176@192.168.137.26/api/holographic/stream/live_high.mp4?holo=false&pv=true&mic=true&loopback=true&RenderFromCamera=true")
while True:
	# ret,photo = cap.read()
	# #cv2.imshow('streaming',photo)
	# ret,buffer = cv2.imencode(".jpg",photo,[int(cv2.IMWRITE_JPEG_QUALITY),30])
	# x_as_bytes = pickle.dumps(buffer)
	# s.sendto((x_as_bytes),(server_ip,server_port))
	# if cv2.waitKey(10)==13:
	# 	break
 
    if client_socket:
            # vid = cv2.VideoCapture("https://danieldoe:Doe@7176@192.168.137.26/api/holographic/stream/live_high.mp4?holo=false&pv=true&mic=true&loopback=true&RenderFromCamera=true")
            vid = cv2.VideoCapture("local_video.mp4")
            while (vid.isOpened()):
                time.sleep(0.1)
                success, frame = vid.read()

                if success:
                    a = pickle.dumps(frame)
                    message = struct.pack("Q", len(a)) + a
                    client_socket.sendall(message)

                    cv2.imshow("sending...", frame)
                    key = cv2.waitKey(10)
                    if key == 13:
                        client_socket.close()
                        
                        
cv2.destroyAllWindows()
# cap.release()

