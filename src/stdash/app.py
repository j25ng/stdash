import streamlit as st

st.title('CNN JOB MONITORING')

rp_page = st.Page("pages/cnt_time.py", title="Count Time", icon="⏱️") 
cnt_page = st.Page("pages/cnt_user.py", title="Count User", icon="😊")
file_page = st.Page("pages/upload_file.py", title="Upload File", icon="🖼️")

pg = st.navigation([rp_page, cnt_page, file_page])

pg.run()

