import cv2

# OpenCV VideoCapture object to read the live stream
cap = cv2.VideoCapture("https://danieldoe:Doe@7176@192.168.137.26/api/holographic/stream/live_high.mp4?holo=false&pv=true&mic=true&loopback=true&RenderFromCamera=true")

# Create a VideoWriter object to save the processed video
output_file = "output.mp4"
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

# Initialize the object detection model (replace with your own implementation)
# ...

while True:
    # Read a frame from the live stream
    ret, frame = cap.read()
    if not ret:
        break

    # Perform object detection on the frame (replace with your own implementation)
    # ...

    # Display the frame with detected objects
    cv2.imshow("Frame", frame)

    # Write the frame to the output video file
    #out.write(frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the resources
cap.release()
out.release()
cv2.destroyAllWindows()
