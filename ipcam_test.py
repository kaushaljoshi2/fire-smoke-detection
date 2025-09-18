import cv2
import requests
import numpy as np
import time

URL = "http://192.168.1.3:8080/shot.jpg"  # snapshot endpoint

while True:
    # Get one frame from the phone
    img_resp = requests.get(URL)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    frame = cv2.imdecode(img_arr, -1)

    # Show it in OpenCV
    cv2.imshow("IP Webcam Snapshot Stream", frame)

    # Break on ESC key
    if cv2.waitKey(1) == 27:
        break

    time.sleep(0.05)  # ~20 fps

cv2.destroyAllWindows()
