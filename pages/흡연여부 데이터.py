import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pingouin as pg
import streamlit as st
import koreanize_matplotlib

pd.options.display.max_columns = None


url = "https://raw.githubusercontent.com/moksu27/midproject/main/healthcare-dataset-stroke-data.csv"
df = pd.read_csv(url)

N = df[["stroke", "smoking_status"]]
sm = N[(N["smoking_status"] == 'formerly smoked') | (N["smoking_status"] == 'smokes')]
N_unknown = N[(N["smoking_status"] == 'formerly smoked') | (N["smoking_status"] == 'never smoked') | (N["smoking_status"] == 'smokes')]
N_unknown_s = N_unknown[N_unknown["stroke"]==1]

# streamlit 구현
st.title('흡연 여부 별 뇌졸중 환자 분포')
fig, ax = plt.subplots(figsize=(10, 6))
sns.countplot(data= N_unknown, x="stroke", hue="smoking_status", palette="YlOrRd")
st.pyplot(fig)

st.markdown("## 뇌졸중 환자 흡연 여부")
fig, ax = plt.subplots(figsize=(10, 6))
sns.countplot(data= N_unknown_s, x="stroke", hue="smoking_status", palette="summer_r")
st.pyplot(fig)