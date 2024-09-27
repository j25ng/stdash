import streamlit as st

rp_page = st.Page("req_prd.py", title="Req/Prd Time", icon=":material/dashboard:")
cnt_page = st.Page("cnt_user.py", title="Count User", icon=":material/dashboard:")

pg = st.navigation([rp_page, cnt_page])
pg.run()

