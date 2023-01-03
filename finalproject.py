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
url = ""

df = pd.read_csv(url)


# 데이터 출력
st.title('')
st.dataframe(df)