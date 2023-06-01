# import required libraries
from vidgear.gears import NetGear
import cv2
from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor
import time

# Load the model
model = YOLO("yolov8x.pt")

# define tweak flags
options = {"flag": 0, "copy": False, "track": False}

# Define Netgear Client at given IP address and define parameters 
# !!! change following IP address '192.168.x.xxx' with yours !!!
client = NetGear(
    address="192.168.137.204",
    port="8000",
    protocol="tcp",
    pattern=0,
    receive_mode=True,
    logging=True,
    **options
)

frame_counter = 0

# loop over
while True:

    # receive frames from network
    frame = client.recv()

    # check for received frame if Nonetype
    if frame is None:
        break

    # {do something with the received frame here}
    frame_counter += 1
    
    if frame_counter == 5:
        results=model.predict(source=frame, show=True,  save=True)
        print("results:", results)
        frame_counter = 0

    # Show output window
    # cv2.imshow("Output Frame", frame)

    # check for 'q' key if pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# close output window
cv2.destroyAllWindows()

# safely close client
client.close()
