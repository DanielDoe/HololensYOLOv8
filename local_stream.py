import cv2
from ultralytics import YOLO
import tempfile
import os

# Load the model
model = YOLO("yolov8x.pt")

# OpenCV VideoCapture object to read the live stream
cap = cv2.VideoCapture("local_video.mp4")

# Get video width, height and frames per second
width  = cap.get(cv2.CAP_PROP_FRAME_WIDTH) 
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = cap.get(cv2.CAP_PROP_FPS)

# Define codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

# Create a temporary file to store the video
temp_video = tempfile.NamedTemporaryFile(suffix=".mp4", delete=False)
out = cv2.VideoWriter(temp_video.name, fourcc, fps, (int(width), int(height)))

while True:
    # Read a frame from the live stream
    ret, frame = cap.read()
    if not ret:
        break

    # Write the frame to temporary video file
    out.write(frame)

    # Predict
    model.predict(source=temp_video.name, show=True)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the resources
cap.release()
out.release()
cv2.destroyAllWindows()

# Delete the temporary file
os.unlink(temp_video.name)
