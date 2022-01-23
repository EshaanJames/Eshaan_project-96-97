import streamlit as st
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)
def app(census_df):
    st.header('Columns Description. .')

    col_name, col_dtype, col_display, col_sum = st.columns(4)
    if col_name.checkbox('View All columns'):
        st.table(census_df.columns)
    if col_dtype.checkbox('View column data-type'):
        st.write(list(census_df.dtypes))
    if col_display.checkbox('View column data'):
        column = st.selectbox('Select column', census_df.columns)
        st.table(census_df[column])
    if col_sum.checkbox('Show summary'):
        st.table(census_df.describe())

    plot_list = ['Income-group', 'Gender', 'Hours-per-week / Income', 'Hours-per-week / Gender', 'Workclass / Income']
    plot = st.multiselect('Select Plots to show', plot_list)
    if 'Income-group' in plot:
        st.write('Income-group')
        fig, ax = plt.subplots()
        ax.hist(census_df['income'])
        st.pyplot(fig)

    if 'Gender' in plot:
        st.write('Gender')
        fig, ax = plt.subplots()
        ax.pie(census_df['gender'].value_counts(), labels=['Male', 'Female'])
        ax.legend()
        st.pyplot(fig)
    if 'Hours-per-week / Income' in plot:
        st.write('Hours-per-week / Income')
        fig, ax = plt.subplots()
        ax.bar(census_df['income'], census_df['hours-per-week'])
        st.pyplot(fig)
    if 'Hours-per-week / Gender' in plot:
        st.write('Hours-per-week / Gender')
        fig, ax = plt.subplots()
        ax.scatter(census_df['gender'], census_df['hours-per-week'])
        st.pyplot(fig)
    if 'Workclass / Income' in plot:
        st.write('Workclass / Income')
        st.write('Hours-per-week / Gender')
        fig, ax = plt.subplots()
        ax.scatter( census_df['workclass'],census_df['gender'])
        st.pyplot(fig)