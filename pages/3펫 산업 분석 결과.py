import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image

st.title('펫 산업 동향 분석 결과')

image1 = Image.open('data/연도별 tf-idf 합계 비중.png')
image2 = Image.open('data/스타사업.png')
image3 = Image.open('data/word2vec.png')


st.image(image3, width = 800)



st.image(image1, width = 800)



st.image(image2, width = 800)

