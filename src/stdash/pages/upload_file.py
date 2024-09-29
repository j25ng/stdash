import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import requests
from PIL import Image

st.title('Upload File')
def load_data():
    url = 'http://43.202.66.118:8016/all'
    #url = 'http://127.0.0.1:8016/all'
    r = requests.get(url).json()
    return r

def send_file(file):
    img = Image.open(file)
    st.write(img)

upload_file = st.file_uploader('이미지를 업로드 하세요.', type=['png', 'jpg', 'jpeg'])
st.button("제출", on_click=send_file, args=[upload_file])
