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
        
        view_item2 = workbooks[2].views[4]
        server.views.populate_image(view_item2)
        view_image2 = view_item2.image
        
        return workbooks_names, view_image1, view_image2

workbooks_names, view_image1, view_image2 = run_query()


# Print results.
st.subheader(workbooks_names[2])
st.write("Found the following workbooks:", ", ".join(workbooks_names))

st.subheader("반려동물 용품")
st.image(view_image1, width=800)
st.image(view_image2, width=800)

# st.image(view_image5, width=1000, height = 500)