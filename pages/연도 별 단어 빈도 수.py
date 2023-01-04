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

# Tokenizer
vocab_size = 1000
oov_tok = ""
tokenizer20 = Tokenizer(num_words = vocab_size, oov_token = oov_tok)
tokenizer21 = Tokenizer(num_words = vocab_size, oov_token = oov_tok)
tokenizer22 = Tokenizer(num_words = vocab_size, oov_token = oov_tok)

news20_token = tokenizer20.fit_on_texts(news20["기사 제목"])
news21_token = tokenizer21.fit_on_texts(news21["기사 제목"])
news22_token = tokenizer22.fit_on_texts(news22["기사 제목"])

# top 20 단어 별 빈도 수 확인 함수
def top_20_words(tokens):
    word_counts = Counter(tokens)
    return word_counts.most_common(20)

wc20 = tokenizer20.word_counts
df_wc20 = pd.DataFrame(wc20.items()).set_index(0).sort_values(by =1,ascending=False).T
df_wc20 = pd.DataFrame(df_wc20.iloc[0,:50])
df_wc20["word"] = df_wc20.index
df_wc20["빈도"] = df_wc20[1]
df_wc20 = df_wc20.drop(columns=1)
df_wc20 = df_wc20.reset_index()
df_wc20 = df_wc20.drop(columns = 0)

wc21 = tokenizer21.word_counts
df_wc21 = pd.DataFrame(wc21.items()).set_index(0).sort_values(by =1,ascending=False).T
df_wc21 = pd.DataFrame(df_wc21.iloc[0,:50])
df_wc21["word"] = df_wc21.index
df_wc21["빈도"] = df_wc21[1]
df_wc21 = df_wc21.drop(columns=1)
df_wc21 = df_wc21.reset_index()
df_wc21 = df_wc21.drop(columns = 0)

wc22 = tokenizer22.word_counts
df_wc22 = pd.DataFrame(wc22.items()).set_index(0).sort_values(by =1,ascending=False).T
df_wc22 = pd.DataFrame(df_wc22.iloc[0,:50])
df_wc22["word"] = df_wc22.index
df_wc22["빈도"] = df_wc22[1]
df_wc22 = df_wc22.drop(columns=1)
df_wc22 = df_wc22.reset_index()
df_wc22 = df_wc22.drop(columns = 0)


st.title('년도 별 단어 빈도 수')

st.bar_chart(df_wc20)