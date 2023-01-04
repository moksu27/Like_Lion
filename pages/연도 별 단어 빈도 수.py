import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pingouin as pg
import streamlit as st
import koreanize_matplotlib
from collections import Counter




url_20 = "https://raw.githubusercontent.com/moksu27/Pet_industry_prediction_streamlit/main/data/news20_%EB%8B%A8%EC%96%B4%EB%B3%84%EB%B9%88%EB%8F%84%EC%88%98.csv"
url_21 = "https://raw.githubusercontent.com/moksu27/Pet_industry_prediction_streamlit/main/data/news21_%EB%8B%A8%EC%96%B4%EB%B3%84%EB%B9%88%EB%8F%84%EC%88%98.csv"
url_22 = "https://raw.githubusercontent.com/moksu27/Pet_industry_prediction_streamlit/main/data/news22_%EB%8B%A8%EC%96%B4%EB%B3%84%EB%B9%88%EB%8F%84%EC%88%98.csv"

news20 = pd.read_csv(url_20)
news21 = pd.read_csv(url_21)
news22 = pd.read_csv(url_22)

news20 = news20.sort_values(by = '빈도', ascending = False)
st.dataframe(data=news20)

st.title('연도 별 단어 빈도 수')
year = st.selectbox('기사 년도',['2020년','2021년','2022년'])
if year == '2020년':
    data = news20
elif year == '2021년':
    data = news21
elif year == '2022년':
    data = news22
st.bar_chart(data, x = '빈도', y = 'word')