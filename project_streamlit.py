import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from glob import glob
import koreanize_matplotlib
import pingouin as pg
import streamlit as st

st.set_page_config(
    page_title="삼삼오오 미드프로젝트",
    page_icon="💻",
    layout="wide",
)


url = "https://raw.githubusercontent.com/moksu27/midproject/main/healthcare-dataset-stroke-data.csv"

df = pd.read_csv(url)

# 성별 "Other" 행 제거 및 인덱스 리셋
df = df.drop(index = 3116)
df = df.reset_index()
# 인덱스 칼럼 제거
df = df.drop(columns = "index")

#age_group 칼럼 추가
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
df["age_group"] = age_list

# 나이 순으로 정렬
df= df.sort_values(by = "age")

# 성별 번호 칼럼 추가
gender_list = []
for i in df["gender"]:
    if i == "Male":
        gender_list.append(0)
    elif i == "Female":
        gender_list.append(1)
df["gender_number"] = gender_list

df