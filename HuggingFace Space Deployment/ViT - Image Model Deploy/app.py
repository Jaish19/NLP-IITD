import streamlit as st
from transformers import pipeline
from PIL import Image

# Load an image classification model pipeline
pipe = pipeline('image-classification')

# Streamlit file uploader for image input
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Open and display the image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Perform image classification
    out = pipe(image)
    
    # Display the results
    st.json(out)