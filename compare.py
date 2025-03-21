import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
from PIL import Image

def compare_handwriting(img1, img2):
    if isinstance(img1, Image.Image):  # Convert PIL image to NumPy array
        img1 = np.array(img1)
    if isinstance(img2, Image.Image):
        img2 = np.array(img2)

    img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # Resize images to the same shape
    img2_gray = cv2.resize(img2_gray, (img1_gray.shape[1], img1_gray.shape[0]))

    similarity_score = ssim(img1_gray, img2_gray)

    return round(similarity_score * 100, 2)  # Convert to percentage
