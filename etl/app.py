import streamlit as st
import pandas as pd
import glob
import matplotlib.pyplot as plt

# Streamlit dashboard settings
st.header("Temperature and humidity Dashboard - VIT")
st.markdown("-------------------------------")
# Create a DataFrame to store data
import os
mypath = os.getcwd()
path = mypath+"/output/sensor_*.csv"
csv_files = glob.glob(path)
print(csv_files)

# Read and concatenate all CSV files into a single DataFrame
data_frames = []
for file in csv_files:
    if os.path.isfile(file):
        df = pd.read_csv(file,header=None)
        df.columns = ['topic', 'partition', 'offset','sensor_id','timestamp','temperature','humidity','outcome']
        data_frames.append(df)
    else:
        print(f"File not found: {file}")

# Concatenate all DataFrames into one
combined_df = pd.concat(data_frames, ignore_index=True)

# Transform
data = combined_df
data['timestamp'] = pd.to_datetime(data['timestamp'])

# Display the combined DataFrame
print(combined_df.head())

# Display the data table if checkbox is selected
if st.checkbox('Show Data Table'):
    st.write(data)


# Select a sensor_id if needed
# Dropdown menu to select an outcome or choose 'All'
outcomes = data['sensor_id'].unique()
outcomes = sorted(outcomes)  # Sort outcomes for better UX
outcomes.insert(0, 'All')  # Add 'All' option at the top

selected_outcome = st.selectbox('Select sensor id', options=outcomes)

# Filter data based on selected outcome
if selected_outcome == 'All':
    filtered_data = data
else:
    filtered_data = data[data['sensor_id'] == selected_outcome]


# Optionally, display some statistics
st.subheader("Statistics")
st.write(f"Mean Temperature: {filtered_data['temperature'].mean():.2f} °C")
st.write(f"Max Temperature: {filtered_data['temperature'].max():.2f} °C")
st.write(f"Min Temperature: {filtered_data['temperature'].min():.2f} °C")

# Group by 'outcome' and count occurrences
outcome_counts = filtered_data['outcome'].value_counts()

# Display bar plot
st.subheader("Outcome Counts Bar Plot")

fig, ax = plt.subplots()
outcome_counts.plot(kind='bar', ax=ax)
ax.set_xlabel('Outcome')
ax.set_ylabel('Count')
ax.set_title('Count of Different Outcomes')

st.pyplot(fig)