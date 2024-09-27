import streamlit as st

rp_page = st.Page("req_prd.py", title="Request/Prediction time", icon=":material/dashboard:")
test_page = st.Page("page_1.py", title="test", icon=":material/dashboard:")

pg = st.navigation([rp_page, test_page])
st.set_page_config(page_title="Data manager", page_icon=":material/edit:")
pg.run()

