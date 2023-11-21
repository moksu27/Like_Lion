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

st.title('고혈압-뇌졸중🏥')
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(data = df, x = "hypertension", y = "stroke")
st.pyplot(fig)

