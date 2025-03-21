import streamlit as st
import os
from compare import compare_handwriting, clear_dataset
from capture import capture_main_image, capture_comparison_images

st.title("📝 Handwriting Comparison App")

st.write("Capture a main handwriting image and compare it with multiple samples.")

# Capture Main Handwriting Image
if st.button("📸 Capture Main Handwriting Image"):
    capture_main_image()
    st.success("✅ Main handwriting image captured!")

# Capture Multiple Comparison Images
if st.button("📸 Capture Comparison Images"):
    capture_comparison_images()
    st.success("✅ Comparison images captured!")

# Compare Button
if st.button("🔍 Compare"):
    results = compare_handwriting("dataset/")

    if isinstance(results, str):
        st.warning(results)
    else:
        st.write("### 🏆 Handwriting Similarity Results:")
        for res in results:
            st.write(f"📌 **{res['image']}** → **{res['similarity']}% similarity**")

# Clear Data Button
if st.button("🗑️ Clear"):
    message = clear_dataset("dataset/")
    st.success(message)
