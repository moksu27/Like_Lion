import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pingouin as pg
import streamlit as st
from wordcloud import WordCloud


st.set_page_config(
    page_title="펫 산업 동향 분석",
    page_icon="🐶",
    layout="wide",
)
# 데이터 불러오기
url_20 = "https://raw.githubusercontent.com/moksu27/Pet_industry_prediction_streamlit/main/data/news20_%EC%A0%84%EC%B2%98%EB%A6%AC.csv"
url_21 = "https://raw.githubusercontent.com/moksu27/Pet_industry_prediction_streamlit/main/data/news21_%EC%A0%84%EC%B2%98%EB%A6%AC.csv"
url_22 = "https://raw.githubusercontent.com/moksu27/Pet_industry_prediction_streamlit/main/data/news22_%EC%A0%84%EC%B2%98%EB%A6%AC.csv"

news20 = pd.read_csv(url_20)
news21 = pd.read_csv(url_21)
news22 = pd.read_csv(url_22)


st.title('기사 주요 키워드')


def main():
    st.header('2020~2022년도 펫산업 관련 키워드')
        
    word_draw = WordCloud(
        font_path="System/Library/Fonts/AppleSDGothicNeo.ttc",
        width=1000, height=1000,
        background_color="white",
        stopwords=["반려동물","위한","개최","출시","일","반려동물과","에","로","월","반려동물용"],
        random_state=42
    )
    word_draw.generate(news20)
    fig = plt.figure(figsize=(15, 7))
    plt.imshow(word_draw)
    plt.axis("off")
    plt.show()
    st.pyplot(fig)