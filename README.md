# Real Time Fire & Smoke Detection Using Surveillance Footage

## Project Overview

- This project implements a real-time fire and smoke detection system using surveillance footage captured from an IP webcam. It leverages state-of-the-art Deep Learning models (YOLOv8) and OpenCV for video processing to detect significant fire and smoke incidents, while intelligently filtering out false positives from small, harmless sources such as gas stoves, lighters, and candles.

- The system is designed to trigger timely alerts upon detecting critical fire or smoke events, making it suitable for enhancing safety in homes, offices, warehouses, and public spaces.

## Features

- **Real-time detection** of fire and smoke from live surveillance footage.
- **False positive filtering** to ignore small, non-hazardous fire/smoke sources.
- **Alert mechanism** with sound notifications on Windows systems.
- Utilizes **YOLOv8** for accurate and fast object detection.
- Easy integration with any IP webcam streaming snapshot images.

## Technology Stack

- Python 3.x
- Ultralytics YOLOv8 for object detection
- OpenCV for video frame processing and display
- Requests library to fetch frames from IP camera
- NumPy for image array manipulations
- winsound (Windows only) for audio alerts

## Getting Started

### Prerequisites

- Python 3.7 or higher installed

- An IP Webcam app or IP camera that streams snapshot images via HTTP

- Windows OS (for sound alert support; for other OS, modify alert part)

### Installation

1. Clone the repository
2. Create and activate a virtual environment (optional)
3. Install the required packages
4. Download or place your trained YOLOv8 weights file (`fire_smoke_yolov8s.pt`) into the project folder.

### Configuration

- Update the IP camera URL in the script (`fire-smoke-detection-live.py`):
  `URL = "http://<your-ip-address>:8080/shot.jpg"`
- Adjust detection confidence thresholds and filtering parameters (if needed).

### Running the Project

- Run the main detection script: `python fire_smoke_detection.py`
- Press `ESC` to exit the real-time detection window.

## How It Works

- The script fetches snapshot images from the IP camera feed continuously.
- Each frame is processed using the YOLOv8 model to detect fire and smoke.
- Small or low-confidence detections are filtered out to reduce false alarms.
- If fire or smoke is detected with high confidence, a sound alert is played and a message is printed.
- The annotated frames with bounding boxes are displayed in a window in real-time.

## Future Improvements

- Add email or SMS notifications for alerts.
- Implement cross-platform sound alert support.
- Integrate video recording on fire/smoke detection events.
- Improve false positive filtering using temporal analysis across frames.
