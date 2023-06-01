# import required libraries
from vidgear.gears import NetGear
import cv2

# Open suitable video stream, such as webcam on first index(i.e. 0)
stream = cv2.VideoCapture("https://danieldoe:Doe@7176@192.168.137.26/api/holographic/stream/live_high.mp4?holo=false&pv=true&mic=true&loopback=true&RenderFromCamera=true")

# define tweak flags
options = {"flag": 0, "copy": False, "track": False}

# Define Netgear Client at given IP address and define parameters 
# !!! change following IP address '192.168.x.xxx' with yours !!!
server = NetGear(
    address="192.168.137.204",
    port="8000",
    protocol="tcp",
    pattern=0,
    logging=True,
    **options
)

prev_frame = []

# loop over until KeyBoard Interrupted
while True:

    try:
        # read frames from stream
        (grabbed, frame) = stream.read()

        # check for frame if not grabbed
        if not grabbed:
            frame = prev_frame
            # continue

        # {do something with the frame here}

        # send frame to server
        server.send(frame)
        prev_frame = frame

    except KeyboardInterrupt:
        break

# safely close video stream
stream.release()

# safely close server
server.close()
