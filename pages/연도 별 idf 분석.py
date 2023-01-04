import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import koreanize_matplotlib
import streamlit as st


url_20 = "https://raw.githubusercontent.com/moksu27/Pet_industry_prediction_streamlit/main/data/news20_%EB%8B%A8%EC%96%B4%EB%B3%84%EB%B9%88%EB%8F%84%EC%88%98.csv"
url_21 = "https://raw.githubusercontent.com/moksu27/Pet_industry_prediction_streamlit/main/data/news21_%EB%8B%A8%EC%96%B4%EB%B3%84%EB%B9%88%EB%8F%84%EC%88%98.csv"
url_22 = "https://raw.githubusercontent.com/moksu27/Pet_industry_prediction_streamlit/main/data/news22_%EB%8B%A8%EC%96%B4%EB%B3%84%EB%B9%88%EB%8F%84%EC%88%98.csv"

news20 = pd.read_csv(url_20)
news21 = pd.read_csv(url_21)
news22 = pd.read_csv(url_22)

