import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pingouin as pg
import streamlit as st
import koreanize_matplotlib



url = "https://raw.githubusercontent.com/moksu27/midproject/main/healthcare-dataset-stroke-data.csv"
df = pd.read_csv(url)

fill_list = df["bmi"].dropna()
df1 = df["bmi"].fillna(pd.Series(np.random.choice(fill_list, size=len(df.index))))
df["bmi"] = df1

st.title('BMI에 따른 뇌졸중 환자 분포')
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(data = df , x = "bmi" , hue = "stroke")
st.pyplot(fig)