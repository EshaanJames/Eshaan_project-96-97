import numpy as np
import pandas as pd
import streamlit as st
import census_home
import census_plot
@st.cache()
def load_data():

	df = pd.read_csv('E:/Python codes/Project 97/Adult.csv', header=None)
	df.head()
	column_name =['age', 'workclass', 'fnlwgt', 'education', 'education-years', 'marital-status', 'occupation', 'relationship', 'race','gender','capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']

	for i in range(df.shape[1]):
	  df.rename(columns={i:column_name[i]},inplace=True)

	df['native-country'] = df['native-country'].replace(' ?',np.nan)
	df['workclass'] = df['workclass'].replace(' ?',np.nan)
	df['occupation'] = df['occupation'].replace(' ?',np.nan)
	df.dropna(inplace=True)

	df.drop(columns='fnlwgt',axis=1,inplace=True)

	return df

census_df = load_data()

pages_dict = {"Home": census_home, "Visualise Data": census_plot}

st.sidebar.title('Navigation')
user_choice = st.sidebar.radio(label='Go to', options=('Home', 'Visualise Data'))
selected_page = pages_dict[user_choice]
selected_page.app(census_df)