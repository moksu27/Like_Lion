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

df_glucose_level =  df[["avg_glucose_level","stroke","age"]]
df_glucose_level = df_glucose_level.copy()

b = df["avg_glucose_level"]

# 혈당수치 등급 분류 
blood_list= []
for b in b:
    if b <= 50:
        blood_list.append(4)
    elif b > 50 and b <= 80  :
        blood_list.append(5)
    elif b> 80 and b <= 115  :
        blood_list.append(6)
    elif b > 115 and b <= 150  :
        blood_list.append(7)
    elif b > 150 and b <= 180  :
        blood_list.append(8)
    elif b > 180 and b <= 215  :
        blood_list.append(9)
    elif b > 215 and b <= 250  :
        blood_list.append(10)       
    elif b > 250 and b <= 280  :
        blood_list.append(11)
df_glucose_level["blood_level"] = blood_list

# 연령대 분류
age_list=[]
for age in df["age"]:
    if age >= 0 and age <10:
        age_list.append("10대 이전")
    elif age >= 10 and age <20:
        age_list.append("10대")
    elif age >= 20 and age <30:
        age_list.append("20대")
    elif age >= 30 and age <40:
        age_list.append("30대")
    elif age >= 40 and age <50:
        age_list.append("40대")
    elif age >= 50 and age <60:
        age_list.append("50대")
    elif age >= 60 and age <70:
        age_list.append("60대")
    elif age >= 70 and age <80:
        age_list.append("70대")
    elif age >= 80 and age <90:
        age_list.append("80대")
df_glucose_level["age"] = age_list

df1 = df_glucose_level[(df_glucose_level['stroke']==1)]
df0 = df_glucose_level[(df_glucose_level['stroke']==0)]



st.title('당뇨등급 별 뇌졸중 환자 분포')
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(data = df1, x="blood_level")
st.pyplot(fig)


st.markdown('# 당뇨등급 별 뇌졸중 환자가 아닌 사람 분포')
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(data = df0, x="blood_level")
st.pyplot(fig)

