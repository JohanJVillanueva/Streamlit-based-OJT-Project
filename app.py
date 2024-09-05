import streamlit as st
import pandas as pd
import time 
from datetime import datetime
#from streamlit_autorefresh import st_autorefresh
from streamlit_navigation_bar import st_navbar

ts=time.time()
date=datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
timestamp=datetime.fromtimestamp(ts).strftime("%H:%M-%S")


st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

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


st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("Attendance List")

df=pd.read_csv("C:\\Users\\liljo\\Documents\\OJT Streamlit\\customers-100.csv")

st.dataframe(df.style.highlight_max(axis=0))

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