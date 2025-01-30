import streamlit as st
import pandas as pd

# Load dataset
#@st.cache
def load_data():
    url = 'https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv'
    data = pd.read_csv(url)
    return data

# Function to convert DataFrame to Excel and return as a downloadable file
def to_excel(df):
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')
        writer.save()
    processed_data = output.getvalue()
    return processed_data


data = load_data()
df = data

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

if st.button('Download Excel'):
    excel_data = to_excel(df)
    st.download_button(label='Download Excel file',
                       data=excel_data,
                       file_name='dataframe.xlsx',
                       mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')


# Display filtered data
st.write('Filtered Dataset')
st.write(filtered_data)