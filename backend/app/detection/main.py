import os
import cv2
import time


class DetectionTraffic:
    def __init__(self, video_path):
        self.video_path = video_path
        self.detector = cv2.HOGDescriptor()
        self.detector.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    def count_cars(self):
        cap = cv2.VideoCapture(self.video_path)

        start_time = time.time()
        end_time = start_time + 10  # Time in seconds

        car_count = 0

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Convert the frame to gray
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Use an object detector
            boxes, weights = self.detector.detectMultiScale(gray, winStride=(8, 8))

            # Draw rectangles around detected objects
            for (x, y, w, h) in boxes:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                car_count += 1

            if time.time() > end_time:
                break

        cap.release()
        cv2.destroyAllWindows()

        return car_count
