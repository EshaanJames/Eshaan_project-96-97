import streamlit as st
def app(census_df):
    st.header('View Data')
    with st.expander('View Dataset'):
        st.table(census_df)
    if st.checkbox('Show summary'):
        st.table(census_df.describe())

