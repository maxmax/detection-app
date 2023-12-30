import cv2
import numpy as np
from flask_socketio import SocketIO

# Base functions for demo cv2

def demo_detection():
    data = {
        "message": "This is a demo function",
        "value": 42,
        "status": "success"
    }
    return data

# Generate frames
socketio = SocketIO()

def generate_frames():
    cap = cv2.VideoCapture(0)

    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Use an object detector
        boxes, weights = hog.detectMultiScale(frame, winStride=(8, 8))

        # Draw rectangles around detected objects
        for (x, y, w, h) in boxes:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Convert the frame to JPEG format
        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        # Send the frame via WebSocket
        socketio.emit('video_frame', {'image': frame_bytes})

    cap.release()
