import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests

st.title('CNN JOB MONITORING')

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
time = df.groupby('request_time').size()

plt.title('Requests by Date and Time')
plt.bar(time.index, time.values)
plt.plot(time.index, time.values, marker='o', color='r')
plt.xlabel('Request Time')  # x축 레이블
plt.ylabel('Count')  # y축 레이블
plt.xticks(rotation = 45)

# 화면에 그리기
st.pyplot(plt)
