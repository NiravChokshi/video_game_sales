from pandas_profiling import ProfileReport
import streamlit as st
from streamlit_pandas_profiling import st_profile_report
import pandas as pd

st.set_page_config(page_title='Data Profiling',
                   page_icon=':wave:',
                   layout='wide')

@st.cache_data
def load_data():
    return pd.read_csv("./vgsales.csv")

@st.cache_data
def profile_data(df):
    return ProfileReport(df)

st.markdown("<h1 style='text-align: center; color: green;'>Data Profiling</h1>", unsafe_allow_html=True)

if st.button('Generate Data Report'):
    df = load_data()
    profile = profile_data(df)

    st.download_button(
        label='Download report as HTML',
        data=profile.to_html(),
        file_name='Data_Profile_Report.html'
    )

    st_profile_report(profile)