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
        view_item1 = workbooks[2].views[0]
        server.views.populate_image(view_item1)
        view_image1 = view_item1.image
        
        view_item2 = workbooks[2].views[1]
        server.views.populate_image(view_item2)
        view_image2 = view_item2.image
        
        view_item3 = workbooks[2].views[2]
        server.views.populate_image(view_item3)
        view_image3 = view_item3.image
        
        view_item4 = workbooks[2].views[3]
        server.views.populate_image(view_item4)
        view_image4 = view_item4.image
        
        view_item5 = workbooks[2].views[4]
        server.views.populate_image(view_item5)
        view_image5 = view_item5.image
        
        view_item6 = workbooks[2].views[5]
        server.views.populate_image(view_item6)
        view_image6 = view_item6.image
        
        view_item7 = workbooks[2].views[6]
        server.views.populate_image(view_item7)
        view_image7 = view_item7.image
        
        view_item8 = workbooks[2].views[7]
        server.views.populate_image(view_item8)
        view_image8 = view_item8.image
        
        view_item9 = workbooks[2].views[8]
        server.views.populate_image(view_item9)
        view_image9 = view_item9.image
        
        return workbooks_names, view_image1, view_image2, view_image3, view_image4, view_image5, view_image6, view_image7, view_image8, view_image9

workbooks_names, view_image1, view_image2, view_image3, view_image4, view_image5, view_image6, view_image7, view_image8, view_image9 = run_query1()

word = st.selectbox('펫 산업 키워드',['반려동물 용품','펫케어','펫푸드', '종합'])

st.subheader(workbooks_names[2])
st.write("Found the following workbooks:", ", ".join(workbooks_names))

if word == '반려동물 용품':
    st.subheader("반려동물 용품")
    st.image(view_image1, width=800)
    st.image(view_image5, width=800)
    
elif word == '펫케어':
    st.subheader("반려동물 용품")
    st.image(view_image2, width=800)
    st.image(view_image6, width=800)
elif word == '펫푸드':
    st.subheader("반려동물 용품")
    st.image(view_image3, width=800)
    st.image(view_image7, width=800)

elif word == '종합':
    st.subheader("종합")
    st.image(view_image4, width=800)
    st.image(view_image9, width=800)