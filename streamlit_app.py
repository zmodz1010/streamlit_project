import streamlit as st
import pandas as pd
import numpy as np

# Generate example data
np.random.seed(42)
data = pd.DataFrame({
    'x': np.arange(100),
    'y': np.random.randn(100).cumsum()
})

# Streamlit app
st.title('Line Chart with Slider')

# Sidebar with slider
selected_range = st.sidebar.slider('Select Range', min_value=0, max_value=len(data)-1, value=(0, len(data)-1))

# Filter data based on selected range
filtered_data = data.iloc[selected_range[0]:selected_range[1]+1, :]

# Line chart
st.line_chart(filtered_data.set_index('x'))

# Optional: Display selected range
st.write('Selected Range:', selected_range)

