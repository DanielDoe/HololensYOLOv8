import cv2
import socket
import pickle

MTU_SIZE = 1500  # Maximum Transmission Unit size
BUFFER_SIZE = MTU_SIZE - 28  # Subtracting IP and UDP headers

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, MTU_SIZE)

server_ip = "192.168.137.204"
server_port = 8000

cap = cv2.VideoCapture("https://danieldoe:Doe@7176@192.168.137.26/api/holographic/stream/live_high.mp4?holo=false&pv=true&mic=true&loopback=true&RenderFromCamera=true")

while True:
    ret, photo = cap.read()
    ret, buffer = cv2.imencode(".jpg", photo, [int(cv2.IMWRITE_JPEG_QUALITY), 30])
    x_as_bytes = pickle.dumps(buffer)
    
    # Split the data into chunks and send to the server
    for i in range(0, len(x_as_bytes), BUFFER_SIZE):
        chunk = x_as_bytes[i:i+BUFFER_SIZE]
        s.sendto(chunk, (server_ip, server_port))

    if cv2.waitKey(10) == 13:
        break

cv2.destroyAllWindows()
cap.release()