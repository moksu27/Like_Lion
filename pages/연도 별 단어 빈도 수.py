import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pingouin as pg
import streamlit as st
import koreanize_matplotlib
from tensorflow.keras.preprocessing.text import Tokenizer
from collections import Counter





url_20 = "https://raw.githubusercontent.com/moksu27/Pet_industry_prediction_streamlit/main/data/news20_%EC%A0%84%EC%B2%98%EB%A6%AC.csv"
url_21 = "https://raw.githubusercontent.com/moksu27/Pet_industry_prediction_streamlit/main/data/news21_%EC%A0%84%EC%B2%98%EB%A6%AC.csv"
url_22 = "https://raw.githubusercontent.com/moksu27/Pet_industry_prediction_streamlit/main/data/news22_%EC%A0%84%EC%B2%98%EB%A6%AC.csv"

news20 = pd.read_csv(url_20)
news21 = pd.read_csv(url_21)
news22 = pd.read_csv(url_22)


st.title('년도 별 단어 빈도 수')

st.bar_chart(df_wc20)