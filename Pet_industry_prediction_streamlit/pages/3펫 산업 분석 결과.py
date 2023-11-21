import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image
import tableauserverclient as TSC


st.title('펫 산업 동향 분석 결과')

# Set up connection.
tableau_auth = TSC.PersonalAccessTokenAuth(
    st.secrets["tableau"]["token_name"],
    st.secrets["tableau"]["personal_access_token"],
    st.secrets["tableau"]["site_id"],
)
server = TSC.Server(st.secrets["tableau"]["server_url"], use_server_version=True)


# Get various data.
# Explore the tableauserverclient library for more options.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def run_query():
    with server.auth.sign_in(tableau_auth):

        # Get all workbooks.
        workbooks, pagination_item = server.workbooks.get()
        workbooks_names = [w.name for w in workbooks]

        # Get views for first workbook.
        server.workbooks.populate_views(workbooks[6])
        server.workbooks.populate_views(workbooks[7])

 # Get image of workbook.
        item1 = workbooks[6].views[0]
        server.views.populate_image(item1)
        img1 = item1.image
        
        item2 = workbooks[7].views[0]
        server.views.populate_image(item2)
        img2 = item2.image
        
        return workbooks_names, img1, img2
workbooks_names, img1, img2 = run_query()
    
image1 = Image.open('data/연도별 tf-idf 합계 비중.png')
image2 = Image.open('data/스타사업.png')
image3 = Image.open('data/word2vec.png')
image4 = Image.open('data/tfidf.png')

st.header("연도별 Tf-idf 합계 비중 (특허 기준)")
st.image(image4, width = 800)
st.image(img2, width = 400)

st.header("연도별 Tf-idf 합계 비중 (뉴스기사 기준)")
st.image(image1, width = 800)
st.image(img1, width = 400)

st.image(image2, width = 800)

st.image(image3, width = 800)

