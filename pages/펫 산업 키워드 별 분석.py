import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import koreanize_matplotlib
import streamlit as st
import tableauserverclient as TSC

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
        server.workbooks.populate_views(workbooks[2])

 # Get image & CSV for first view of first workbook.
        item1 = workbooks[2].views[0]
        server.views.populate_image(item1)
        img1 = item1.image
        
        item2 = workbooks[2].views[1]
        server.views.populate_image(item2)
        img2 = item2.image
        
        item3 = workbooks[2].views[2]
        server.views.populate_image(item3)
        img3 = item3.image
        
        item4 = workbooks[2].views[3]
        server.views.populate_image(item4)
        img4 = item4.image
        
        item5 = workbooks[2].views[4]
        server.views.populate_image(item5)
        img5 = item5.image
        
        item6 = workbooks[2].views[5]
        server.views.populate_image(item6)
        img6 = item6.image
        
        item7 = workbooks[2].views[6]
        server.views.populate_image(item7)
        img7 = item7.image
        
        item8 = workbooks[2].views[7]
        server.views.populate_image(item8)
        img8 = item8.image
        
        item9 = workbooks[2].views[8]
        server.views.populate_image(item9)
        img9 = item9.image
        
        item10 = workbooks[3].views[0]
        server.views.populate_image(item10)
        img10 = item10.image
        
        return workbooks_names, img1, img2, img3, img4, img5, img6, img7, img8, img9, img10

workbooks_names, img1, img2, img3, img4, img5, img6, img7, img8, img9, img10= run_query()

word = st.selectbox('펫 산업 키워드',['반려동물 용품','펫케어','펫푸드', '종합'])

st.subheader(workbooks_names[2])
st.write("Found the following workbooks:", ", ".join(workbooks_names))

if word == '반려동물 용품':
    st.subheader("반려동물 용품")
    st.image(img1, width=800)
    st.image(img5, width=800)
    
elif word == '펫케어':
    st.subheader("반려동물 용품")
    st.image(img2, width=800)
    st.image(img6, width=800)
elif word == '펫푸드':
    st.subheader("반려동물 용품")
    st.image(img3, width=800)
    st.image(img7, width=800)

elif word == '종합':
    st.subheader("종합")
    st.image(img10, width=800)
    st.image(img9, width=800)