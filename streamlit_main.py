import streamlit as st
import pandas as pd

# Load dataset
#@st.cache
def load_data():
    url = 'https://healthdata.gov/resource/ektz-upmg.csv'
    data = pd.read_csv(url)
    return data

data = load_data()

# Title of the app
st.title('Dataset Filter App')

# Display the dataframe
st.write('Original Dataset')
st.write(data)

# Sidebar for filters
st.sidebar.header('Filters')

# Example filters
columns = data.columns.tolist()
selected_columns = st.sidebar.multiselect('Select columns to display', columns, default=columns)

unique_values = {col: data[col].unique().tolist() for col in selected_columns}
filters = {col: st.sidebar.multiselect(f'Select values for {col}', unique_values[col], default=unique_values[col]) for col in selected_columns}

# Apply filters
filtered_data = data.copy()
for col, values in filters.items():
    filtered_data = filtered_data[filtered_data[col].isin(values)]

# Display filtered data
st.write('Filtered Dataset')
st.write(filtered_data)