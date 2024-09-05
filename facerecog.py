import streamlit as st
import pandas as pd
import time 
from datetime import datetime
#from streamlit_autorefresh import st_autorefresh
from streamlit_navigation_bar import st_navbar

ts=time.time()
date=datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
timestamp=datetime.fromtimestamp(ts).strftime("%H:%M-%S")
    
st.set_page_config(initial_sidebar_state="collapsed")
with st.sidebar:
    st.subheader("PUP Biometrics Attendance System")
    st.button("Home")
    st.button("Dashboard")
    st.button("Sign Out")




PUPSIDE = "pup.svg"
PUPMAIN = "pup.svg"

st.logo(
    PUPMAIN,
    icon_image=PUPSIDE,
)


page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://i.imgur.com/E6EeiTk.jpeg");
background-size: 180%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}

</style>
"""
st.subheader("PUP Biometrics Attendance System")
st.markdown(page_bg_img, unsafe_allow_html=True)
left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image("1x1.jpg", width=230)

col1, col2, col3 , col4, col5 = st.columns(5)

with col1:
    pass
with col2:
    pass
with col4:
    pass
with col5:
    pass
with col3 :  
    center_button = st.button("Recognize Face", type="primary")
st.text("Don't have an account yet? Sign up here.")
    




footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
height: 5%;
bottom: 0;
width: 100%;
background-color: maroon;
color: white;
text-align: center;
}

</style>
<div class="footer">
<p>Polytechnic University of The Philippines Biometric Attendance system | OJT</p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)