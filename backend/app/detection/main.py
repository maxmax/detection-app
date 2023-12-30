import os
import cv2
import time

# Instead of using machine coordinates as identifiers, you can use machine features,
# such as their HOG features, to more accurately identify unique machines.
# We will use more advanced algorithms in the future,
# but for now, we will keep this method as a template for the constructor.

class DetectionTraffic:
    def __init__(self, video_path, time_seconds):
        self.video_path = video_path
        self.time_seconds = time_seconds
        self.detector = cv2.HOGDescriptor()
        self.detector.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    def extract_features(self, frame, boxes):
        features = []
        for (x, y, w, h) in boxes:
            roi = frame[y:y+h, x:x+w]
            roi_gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
            features.append(self.detector.compute(roi_gray))
        return features

    def count_cars(self):
        cap = cv2.VideoCapture(self.video_path)

        start_time = time.time()
        end_time = start_time + self.time_seconds  # Время в секундах

        tracked_cars = set()

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Convert the frame to gray
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Use an object detector
            boxes, weights = self.detector.detectMultiScale(gray, winStride=(8, 8))

            # Extract features for each car
            features = self.extract_features(frame, boxes)

            # Draw rectangles around detected objects
            for (x, y, w, h), feature in zip(boxes, features):
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                # We identify the car by characteristics
                car_id = hash(feature.tobytes())
                tracked_cars.add(car_id)

            if time.time() > end_time:
                break

        cap.release()
        cv2.destroyAllWindows()

        return len(tracked_cars)
