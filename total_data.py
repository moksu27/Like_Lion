import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pingouin as pg
import streamlit as st

st.set_page_config(
    page_title="삼삼오오 미드프로젝트",
    page_icon="💻",
    layout="wide",
)
# 데이터 불러오기
url = "https://raw.githubusercontent.com/moksu27/midproject/main/healthcare-dataset-stroke-data.csv"

df = pd.read_csv(url)


# 데이터 출력
st.title('뇌졸중 환자 전체 데이터🏥')
st.dataframe(df)