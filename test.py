import cv2
from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor

# Load the model
model = YOLO("yolov8x.pt")

# OpenCV VideoCapture object to read the live stream
cap = cv2.VideoCapture("https://danieldoe:Doe@7176@192.168.137.26/api/holographic/stream/live_high.mp4?holo=false&pv=true&mic=true&loopback=true&RenderFromCamera=true")

while True:
    # Read a frame from the live stream
    ret, frame = cap.read()
    if not ret:
        break
    
    

    # Predict
    results=model.predict(source=frame, show=True,  save=True)
    print("results:", results)
    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the resources
cap.release()
cv2.destroyAllWindows()