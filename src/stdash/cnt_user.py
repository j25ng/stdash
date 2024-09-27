import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import numpy as np
import requests

st.title('요청/처리 건수(사용자)')

def load_data():
    url = 'http://43.202.66.118:8016/all'
    #url = 'http://127.0.0.1:8016/all'
    r = requests.get(url).json()
    return r

data = load_data()
df = pd.DataFrame(data)

req_cnt = df.groupby('request_user').size().reset_index(name='req_cnt')
req_cnt.set_index('request_user', inplace=True)
req_cnt.rename_axis('user', inplace=True)
prd_cnt = df.groupby('prediction_model').size().reset_index(name='prd_cnt')
prd_cnt.set_index('prediction_model', inplace=True)
prd_cnt.rename_axis('user', inplace=True)

merge_df = req_cnt.join(prd_cnt, how='left')

index = np.arange(len(merge_df.index))
bar_width = 0.4
b1 = plt.bar(index, merge_df['req_cnt'], bar_width, alpha=0.4, color='red', label='Req')
b2 = plt.bar(index + bar_width, merge_df['prd_cnt'], bar_width, alpha=0.4, color='blue', label='Prd')

plt.xlabel('User')
plt.ylabel('Counts')
plt.title('Request Count and Predict Count by User')
plt.xticks(index, merge_df.index)
plt.legend(loc='upper left')

st.pyplot(plt)
