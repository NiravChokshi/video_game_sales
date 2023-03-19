import streamlit as st
from streamlit_extras.let_it_rain import rain


st.set_page_config(page_title='Video Game Sales Analysis',
                   page_icon=':wave:',
                   layout='wide')

st.markdown("<h1 style='text-align: center; color: green;'>Video Game Sales</h1>", unsafe_allow_html=True)

rain(
    emoji="🎈",
    font_size=54,
    falling_speed=5,
    animation_length="infinite",
)

st.markdown(
    ''' 
Background : I have always played video games growing up and I still do. This interest of mine has led me to use my
knowledge of Python to perform data analysis on video game sales to explore various aspects of the video
game industry. The dataset available on Kaggle is very detail-oriented which can help to perform the required
data analysis and gain the required insights. These insights can further be used to make data-driven decisions
in the video game industry.


Research Problem : Companies spend a lot of money to develop games and market them. “On what metrics should the
companies take accurate decisions for game development and marketing strategies?”


Research Question : After devising game development and marketing strategies, companies can answer the question “What genre
of games for which region should they develop to increase profit?”


Data : The Video Game Sales dataset contains data on video game sales from North America, Europe, Japan, and
other regions. The dataset contains information on the video game's name, platform, year of release, genre,
publisher, and global sales. The dataset contains ~16,500 rows and 11 columns. This data can be sufficient to
gain the required insights.


Reference : https://www.kaggle.com/datasets/gregorut/videogamesales


Analysis : I will use Pandas to perform analysis to derive the frequency of sales for the top 10 and bottom 10 years, the
frequency of games by genre, platform, and publisher, the top 10 and bottom 10 games, the top 10 and bottom
10 platforms, and region-specific publisher sales and Matplotlib to plot the insights generated.


The following findings can be obtained:
1. Increase in sales through the years
2. The largest market for video games
3. The most popular game
4. The most popular genre
5. The most popular publisher''')