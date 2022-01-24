import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
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

    plot_list = ['Income-group', 'Gender', 'Workclass / Income', 'boxplot']
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

    if 'Workclass / Income' in plot:
        st.write('Workclass / Income')
        st.write('Hours-per-week / Gender')
        fig, ax = plt.subplots()
        sns.countplot( x=census_df['workclass'],hue=census_df['income'])
        st.pyplot(fig)
    if 'boxplot' in plot:
        hue_cols = st.multiselect('Select the column', ('income', 'gender'))
        for i in hue_cols:
            fig, ax = plt.subplots()
            sns.boxplot(x=census_df['hours-per-week'], y = census_df[i])
            st.pyplot(fig)
