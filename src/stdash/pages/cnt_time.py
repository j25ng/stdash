import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import requests

st.title('요청/처리 건수(시간)')

def load_data():
    url = 'http://43.202.66.118:8016/all'
    #url = 'http://127.0.0.1:8016/all'
    r = requests.get(url).json()
    return r

data = load_data()
df = pd.DataFrame(data)

# TODO
# request_time, prediction_time 이용해 '%Y-%m-%d %H' 형식
# 즉 시간별 GROUPBY COUNT 하여 plt 차트 그려보기
df['request_time'] = pd.to_datetime(df['request_time']).dt.strftime('%Y-%m-%d %H')
df['prediction_time'] = pd.to_datetime(df['prediction_time']).dt.strftime('%Y-%m-%d %H')

r_time = df.groupby('request_time').size()
p_time = df.groupby('prediction_time').size()

plt.title('Requests by Date and Time')
plt.bar(r_time.index, r_time.values, label='Req')
plt.plot(p_time.index, p_time.values, marker='o', color='r', label='Prd')
plt.xlabel('Date and Time')  # x축 레이블
plt.ylabel('Count')  # y축 레이블
plt.xticks(rotation = 45)
plt.legend(loc='upper left')

# 화면에 그리기
st.pyplot(plt)
