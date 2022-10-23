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

df1 = df.copy()
df1['smoking_status'] = df1['smoking_status'].replace('Unknown',np.nan)
fill_list = df["smoking_status"].dropna()
df1["smoking_status"] = df1["smoking_status"].fillna(pd.Series(np.random.choice(fill_list, size = len(df.index))))



# streamlit 구현
st.title('흡연 여부 별 뇌졸중 환자 데이터🏥')
fig, ax = plt.subplots(figsize=(10, 6))
sns.countplot(data = df1, x = "smoking_status",palette='PuBuGn')
st.pyplot(fig)