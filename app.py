import streamlit as st
import cv2
import numpy as np
from PIL import Image
from compare import compare_handwriting
from capture import capture_handwriting

st.title("📝 Real-Time Handwriting Comparison App")

# Choose input method
input_method = st.radio("Choose Input Method:", ["📸 Camera Capture", "📂 Upload Image"])

# Initialize session states
if "main_image" not in st.session_state:
    st.session_state["main_image"] = None

# Capture or Upload Main Handwriting Sample
if st.button("📸 Capture Main Handwriting Image") and input_method == "📸 Camera Capture":
    st.session_state["main_image"] = capture_handwriting()
    if st.session_state["main_image"] is not None:
        st.success("✅ Main handwriting sample captured!")

if input_method == "📂 Upload Image":
    uploaded_file = st.file_uploader("Upload Main Handwriting Sample", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        st.session_state["main_image"] = Image.open(uploaded_file)
        st.success("✅ Main handwriting sample uploaded!")

# Display Main Handwriting Image
if st.session_state["main_image"] is not None:
    st.image(st.session_state["main_image"], caption="Main Handwriting", use_column_width=True)

# Capture or Upload Comparison Image
if st.button("📷 Capture & Compare Handwriting") and input_method == "📸 Camera Capture":
    compare_image = capture_handwriting()
    if compare_image is not None:
        similarity = compare_handwriting(st.session_state["main_image"], compare_image)
        st.image(compare_image, caption="Comparison Handwriting", use_column_width=True)
        st.write(f"🔍 **Similarity Score:** {similarity}%")

if input_method == "📂 Upload Image":
    comparison_file = st.file_uploader("Upload Comparison Handwriting Image", type=["png", "jpg", "jpeg"])
    if comparison_file is not None:
        compare_image = Image.open(comparison_file)
        similarity = compare_handwriting(st.session_state["main_image"], compare_image)
        st.image(compare_image, caption="Comparison Handwriting", use_column_width=True)
        st.write(f"🔍 **Similarity Score:** {similarity}%")

# Clear Data Button
if st.button("🔄 Clear"):
    st.session_state["main_image"] = None
    st.experimental_rerun()
