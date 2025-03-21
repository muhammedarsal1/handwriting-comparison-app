import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
from PIL import Image

def compare_handwriting(img1, img2):
    # Convert PIL images to NumPy arrays
    img1 = np.array(img1.convert("L"))
    img2 = np.array(img2.convert("L"))

    # Resize images to the same shape
    img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

    similarity_score = ssim(img1, img2)

    return round(similarity_score * 100, 2)  # Convert to percentage
