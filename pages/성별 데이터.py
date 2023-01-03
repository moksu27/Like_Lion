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

# 성별 "Other" 행 제거 및 인덱스 리셋
df = df.drop(index = 3116)
df = df.reset_index()
# 인덱스 칼럼 제거
df = df.drop(columns = "index")


st.title('남 여 뇌졸중 환자 비율🏥')
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data = df, x = "gender", y = "stroke", palette="YlOrRd")
st.pyplot(fig)

