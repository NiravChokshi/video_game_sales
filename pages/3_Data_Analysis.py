import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
sns.set(font_scale=2)

st.set_page_config(page_title='Data Analysis',
                   page_icon=':wave:',
                   layout='wide')

st.markdown("<h1 style='text-align: center; color: green;'>Data Analysis</h1>", unsafe_allow_html=True)

@st.cache_data
def load_data():
    df = pd.read_csv("./vgsales.csv")
    df['Year'] = df['Year'].astype('int', errors='ignore')
    return df

df = load_data()


option = st.selectbox(
    'Analysis',
    ('Year with highest sales worldwide',
     'Top 20 popular games',
     'Most popular genre',
     'Top 20 popular publisher',
     'Largest market for video games'))

if option == 'Year with highest sales worldwide':

    st.subheader("Year with highest sales worldwide")
    data_year = df.groupby(by=['Year'])['Global_Sales'].sum()
    data_year = data_year.reset_index()
    fig1 = plt.figure(figsize=(20, 10))
    sns.barplot(x="Year", y="Global_Sales", data=data_year)
    plt.xticks(rotation=90)
    st.pyplot(fig1)

if option == 'Top 20 popular games':
    st.subheader("Top 20 popular games")
    top_games = df.groupby(by=['Publisher'])['Year'].count().sort_values(ascending=False).head(20)
    top_games = pd.DataFrame(top_games).reset_index()
    fig2 = plt.figure(figsize=(20, 10))
    sns.countplot(x="Name", data=df, order = df.groupby(by=['Name'])['Year'].count().sort_values(ascending=False).iloc[:20].index)
    plt.xticks(rotation=90)
    st.pyplot(fig2)

if option == 'Most popular genre':
    st.subheader("Most popular genre")
    fig3 = plt.figure(figsize=(20, 10))
    sns.countplot(x="Genre", data=df, order = df['Genre'].value_counts().index)
    plt.xticks(rotation=90)
    st.pyplot(fig3)

if option == 'Top 20 popular publisher':
    st.subheader("Top 20 popular publisher")
    top_publisher = df.groupby(by=['Publisher'])['Year'].count().sort_values(ascending=False).head(20)
    top_publisher = pd.DataFrame(top_publisher).reset_index()
    fig4 = plt.figure(figsize=(20, 10))
    sns.countplot(x="Publisher", data=df, order = df.groupby(by=['Publisher'])['Year'].count().sort_values(ascending=False).iloc[:20].index)
    plt.xticks(rotation=90)
    st.pyplot(fig4)

if option == 'Largest market for video games':
    top_sale_reg = df[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']]
    top_sale_reg = top_sale_reg.sum().reset_index()
    top_sale_reg = top_sale_reg.rename(columns={"index": "region", 0: "sale"})
    fig5 = plt.figure(figsize=(20, 10))
    sns.barplot(x='region', y='sale', data=top_sale_reg)
    st.pyplot(fig5)