# Import necessary libraries
from ultralytics import YOLO # YOLOv8 model for detection
import cv2 # OpenCV for image display
import requests # To fetch frames from IP camera
import numpy as np # To convert image bytes to array
import time # For frame delay
import winsound # For sound alerts on Windows

# Load the trained YOLOv8 model for fire and smoke detection
model = YOLO("weights/fire_smoke_yolov8s.pt")

# IP camera snapshot URL (use IP Webcam app or similar)
URL = "http://10.106.172.91:8080/shot.jpg" # Enter URL displayed in your IP Webcam (displayed in the bottom)

while True:
    try:
        # Fetch a single frame from the IP camera
        img_resp = requests.get(URL, timeout=5)
        
        # Convert the image bytes to a NumPy array
        img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)

        # Decode the image array into an OpenCV frame
        frame = cv2.imdecode(img_arr, -1)

        # If frame is invalid, skip this iteration
        if frame is None:
            print("⚠️ Could not decode frame, skipping...")
            continue

        # Run YOLO model inference on the frame with confidence threshold 0.4
        results = model(frame, conf=0.4)

        # Plot bounding boxes and labels on the frame
        annotated = results[0].plot()

        # Alert if fire or smoke is detected (Loop over detected objects)
        for box in results[0].boxes:
            cls_id = int(box.cls[0])  # Detected class ID (0 = Fire, 1 = Smoke)
            conf = float(box.conf[0]) # Detection confidence score
          
            # Trigger alerts for high-confidence detections
            if conf > 0.6:
                if cls_id == 0:
                    print("🔥 Fire detected!")
                    winsound.Beep(1000, 500) # Beep sound alert for fire
                elif cls_id == 1:
                    print("💨 Smoke detected!")
                    winsound.Beep(600, 500) # Beep sound alert for smoke

        # Display the annotated frame
        cv2.imshow("🔥 Fire & Smoke Detection", annotated)

    except Exception as e:
        # Handle any errors (e.g., connection timeout, decoding failure)
        print("⚠️ Error fetching frame:", e)
        time.sleep(1)
        continue

    # Exit the loop when ESC key is pressed
    if cv2.waitKey(1) == 27:
        break

    # Slight delay to control frame rate (~20 fps)
    time.sleep(0.05)

# Release all OpenCV windows
cv2.destroyAllWindows()
