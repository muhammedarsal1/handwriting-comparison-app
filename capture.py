import cv2
import numpy as np

def capture_handwriting():
    cap = cv2.VideoCapture(0)  # Open webcam

    if not cap.isOpened():
        print("❌ Error: Could not open webcam")
        return None

    while True:
        ret, frame = cap.read()
        if not ret or frame is None:
            print("⚠️ Failed to capture image! Try again.")
            continue

        cv2.imshow("Capture Handwriting", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):  # Press 's' to capture image
            break

    cap.release()
    cv2.destroyAllWindows()
    return frame  # Return captured image
