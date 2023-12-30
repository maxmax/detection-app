import cv2
import numpy as np
import time
import json

class DetectionTraffic:
    def __init__(self, video_path, time_seconds = 10, contour = 500):
        self.video_path = video_path
        self.detection_completed = False
        self.num_objects = 0
        self.time_seconds = time_seconds
        self.contour = contour

    def detect_traffic(self):
        if self.detection_completed:  # Check if detection has already been performed
            return {"num_objects": self.num_objects}  # Return the number of objects

        cap = cv2.VideoCapture(self.video_path)
        if not cap.isOpened():
            print("Error opening video file.")
            return

        # Create a background subtractor object
        bg_subtractor = cv2.createBackgroundSubtractorMOG2()

        # Initialize variables to keep track of the number of objects and time
        start_time = time.time()

        while True:
            # Read a frame from the video
            ret, frame = cap.read()
            if not ret:
                break

            # Resize the frame for better performance
            frame = cv2.resize(frame, (640, 480))

            # Apply background subtraction to detect moving objects
            mask = bg_subtractor.apply(frame)

            # Apply a threshold to the mask to remove noise
            thresh = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)[1]

            # Find contours of the moving objects
            contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # Filter out small contours that are likely noise
            filtered_contours = [contour for contour in contours if cv2.contourArea(contour) > self.contour]

            # Count the number of objects
            self.num_objects = len(filtered_contours)

            # Update the time
            current_time = time.time()
            if current_time - start_time >= self.time_seconds:
                break

        # Set the detection flag to completed
        self.detection_completed = True

        # Release the video capture object
        cap.release()

        # Return the number of objects in JSON format
        return {"num_objects": self.num_objects}
