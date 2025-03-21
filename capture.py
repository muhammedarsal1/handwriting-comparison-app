import cv2
import os

def capture_handwriting(main_image=False, save_dir="dataset/"):
    cap = cv2.VideoCapture(0)  # Open webcam
    count = 0

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    while True:
        ret, frame = cap.read()
        
        if not ret or frame is None:  # 🔴 Fix: Check if frame is empty
            print("⚠️ Failed to capture image! Check your webcam connection.")
            continue  # Skip this loop iteration if frame is invalid

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
        cv2.imshow("Capture Handwriting", gray)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):  # Press 's' to save
            if main_image:
                img_path = os.path.join(save_dir, "main_handwriting.jpg")
                cv2.imwrite(img_path, gray)
                print(f"✅ Main Image saved at {img_path}")
                break
            else:
                img_path = os.path.join(save_dir, f"compare_{count}.jpg")
                cv2.imwrite(img_path, gray)
                print(f"✅ Comparison Image {count} saved at {img_path}")
                count += 1

        elif key == ord('q'):  # Press 'q' to exit
            break

    cap.release()
    cv2.destroyAllWindows()

# Capture Main Image (Reference Handwriting)
def capture_main_image():
    capture_handwriting(main_image=True)

# Capture Multiple Comparison Images
def capture_comparison_images():
    capture_handwriting(main_image=False)
