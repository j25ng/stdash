from rightnow.time import now
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import requests

st.title('Upload File')

def upload_file(file):
    url = "http://localhost:8016/uploadfile/" 
    label = file.name.split('_')[0]
    files = {"file": (file.name, file.getvalue(), file.type)}
    data = {"label": int(label)}

    r = requests.post(url, files=files, data=data)
    return r

file = st.file_uploader('', type=['png', 'jpg', 'jpeg'])

if file is not None:
    st.image(file, width=300)
    if st.button("Upload"):
        r = upload_file(file)
        st.write(r.json())


