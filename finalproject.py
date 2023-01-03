import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pingouin as pg
import streamlit as st

st.set_page_config(
    page_title="펫 산업 동향 분석",
    page_icon="🐶",
    layout="wide",
)
# 데이터 불러오기
url_20 = "https://raw.githubusercontent.com/moksu27/Pet_industry_prediction_streamlit/main/data/news20_%EC%A0%84%EC%B2%98%EB%A6%AC.csv"
url_21 = "https://raw.githubusercontent.com/moksu27/Pet_industry_prediction_streamlit/main/data/news21_%EC%A0%84%EC%B2%98%EB%A6%AC.csv"
url_22 = "https://raw.githubusercontent.com/moksu27/Pet_industry_prediction_streamlit/main/data/news22_%EC%A0%84%EC%B2%98%EB%A6%AC.csv"

df_20 = pd.read_csv(url_20)
df_21 = pd.read_csv(url_21)
df_22 = pd.read_csv(url_22)


# 데이터 출력
st.title('펫 산업 관련 기사 데이터')
st.dataframe(df_20)