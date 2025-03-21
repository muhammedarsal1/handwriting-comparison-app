import cv2
import numpy as np
import os
from skimage.feature import hog
from sklearn.metrics.pairwise import cosine_similarity

def extract_hog_features(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    resized_img = cv2.resize(image, (128, 128))
    features, _ = hog(resized_img, orientations=9, pixels_per_cell=(8,8),
                      cells_per_block=(2,2), visualize=True)
    return features

def compare_handwriting(folder_path="dataset/"):
    main_image_path = os.path.join(folder_path, "main_handwriting.jpg")

    if not os.path.exists(main_image_path):
        return "⚠️ Main handwriting image not found! Please capture it first."

    main_features = extract_hog_features(main_image_path)
    images = sorted([f for f in os.listdir(folder_path) if f.startswith("compare_")])
    
    results = []
    for img in images:
        img_path = os.path.join(folder_path, img)
        img_features = extract_hog_features(img_path)
        
        similarity = cosine_similarity([main_features], [img_features])[0][0] * 100
        results.append({
            "image": img,
            "similarity": round(similarity, 2),
        })

    return results

def clear_dataset(folder_path="dataset/"):
    """Deletes all handwriting images in the dataset folder."""
    if os.path.exists(folder_path):
        for file in os.listdir(folder_path):
            os.remove(os.path.join(folder_path, file))
        return "Dataset cleared successfully!"
    return "No images found to clear."
