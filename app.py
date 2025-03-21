import streamlit as st
import cv2
import numpy as np
from PIL import Image
from compare import compare_handwriting

st.title("📝 Real-Time Handwriting Comparison App")

# Choose input method
input_method = st.radio("Choose Input Method:", ["📸 Capture from Camera", "📂 Upload Image"])

# Initialize session states
if "main_image" not in st.session_state:
    st.session_state["main_image"] = None

# 📸 Capture or Upload Main Handwriting Sample
if input_method == "📸 Capture from Camera":
    main_image = st.camera_input("Take a photo of the main handwriting sample")
    if main_image is not None:
        st.session_state["main_image"] = Image.open(main_image)
        st.success("✅ Main handwriting sample captured!")

elif input_method == "📂 Upload Image":
    uploaded_file = st.file_uploader("Upload Main Handwriting Sample", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        st.session_state["main_image"] = Image.open(uploaded_file)
        st.success("✅ Main handwriting sample uploaded!")

# Display Main Handwriting Image
if st.session_state["main_image"] is not None:
    st.image(st.session_state["main_image"], caption="Main Handwriting", use_column_width=True)

# 📷 Capture or Upload Comparison Image
if input_method == "📸 Capture from Camera":
    compare_image = st.camera_input("Take a photo of the comparison handwriting sample")
    if compare_image is not None:
        compare_image = Image.open(compare_image)
        similarity = compare_handwriting(st.session_state["main_image"], compare_image)
        st.image(compare_image, caption="Comparison Handwriting", use_column_width=True)
        st.write(f"🔍 **Similarity Score:** {similarity}%")

elif input_method == "📂 Upload Image":
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
