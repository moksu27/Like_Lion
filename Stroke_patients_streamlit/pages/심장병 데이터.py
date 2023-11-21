import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import koreanize_matplotlib
import pingouin as pg
import streamlit as st



pd.options.display.max_columns = None


url = "https://raw.githubusercontent.com/moksu27/midproject/main/healthcare-dataset-stroke-data.csv"
df = pd.read_csv(url)


st.title('심장병 여부 별 뇌졸중 환자 분포')
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data = df, x = "heart_disease", y = "stroke", palette="YlOrRd")
st.pyplot(fig)

fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(data = df, x= "heart_disease", y = 'stroke')
st.pyplot(fig)

