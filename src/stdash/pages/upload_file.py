import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import requests

st.title('Upload File')

def load_data():
    url = 'http://43.202.66.118:8016/all'
    #url = 'http://127.0.0.1:8016/all'
    r = requests.get(url).json()
    return r
