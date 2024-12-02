import streamlit as st

rp_page = st.Page("pages/cnt_time.py", title="STEP1", icon="⏱️") 
cnt_page = st.Page("pages/cnt_user.py", title="STEP2", icon="😊")
file_page = st.Page("pages/upload_file.py", title="STEP3", icon="🖼️")
hotdog_page = st.Page("pages/hotdog.py", title="STEP4", icon="🌭")
pg = st.navigation([rp_page, cnt_page, file_page, hotdog_page])

pg.run()

