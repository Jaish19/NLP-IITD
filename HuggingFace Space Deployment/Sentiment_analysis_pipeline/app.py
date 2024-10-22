import streamlit as st
from transformers import pipeline

pipe = pipeline('sentiment-analysis')
# pipe = pipeline("text-classification", model="ProsusAI/finbert")

text = st.text_area("Enter your input:")

if text:
    out = pipe(text)
    st.json(out)
