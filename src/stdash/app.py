import streamlit as st


rp_page = st.Page("cnt_time.py", title="Time", icon=":material/dashboard:")
cnt_page = st.Page("cnt_user.py", title="User", icon=":material/dashboard:")

pg = st.navigation(
        {
            "Req-Prd" :[rp_page, cnt_page]
        }
)

pg.run()

