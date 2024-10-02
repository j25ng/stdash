from rightnow.time import now
from transformers import pipeline
from PIL import Image
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import requests
import io

st.title('HOTDOG?')

img = st.file_uploader('', type=['png', 'jpg', 'jpeg'])

if img is not None:
    st.image(img, width=300)
    model = pipeline("image-classification", model="julien-c/hotdog-not-hotdog")
    img = Image.open(img)
    p = model(img)
    score = p[0]['score']
    label = "🙅‍♀️ NOT HOT DOG 🙅‍♂️" if score < 0.8 else "🙆‍♀️ HOTDOG 🙆‍♂️"
    st.markdown(f"## {label}")


