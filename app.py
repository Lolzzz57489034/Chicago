import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title and description of the app
st.title("Crime Data Analysis App")
st.write("Upload your crime dataset (CSV) and explore insights.")

# File uploader widget
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# If a file is uploaded, proceed with data loading and analysis
if uploaded_file is not None:
    # Load the CSV data into a DataFrame
    crime_data = pd.read_csv(uploaded_file)

    # Display the first few rows of the dataset
    st.subheader("Dataset Preview")
    st.write(crime_data.head())

    # Check for missing values
    st.subheader("Missing Values Check")
    missing_values = crime_data.isnull().sum()
    st.write(missing_values[missing_values > 0])  # Only show columns with missing values

    # Data cleaning options
    if st.checkbox("Drop rows with missing values"):
        crime_data.dropna(inplace=True)
        st.write("Dropped rows with missing values.")

    if st.checkbox("Remove duplicate rows"):
        crime_data.drop_duplicates(inplace=True)
        st.write("Removed duplicate rows.")

    # Crime count analysis
    st.subheader("Crime Type Distribution")
    crime_counts = crime_data['Primary Type'].value_counts()

    # Display the results as a table
    st.write(crime_counts)

    # Plot the crime type distribution
    st.subheader("Crime Type Distribution (Bar Plot)")
    fig, ax = plt.subplots()
    crime_counts.plot(kind='bar', ax=ax, color='skyblue')
    ax.set_title("Number of Crimes by Type")
    ax.set_xlabel("Crime Type")
    ax.set_ylabel("Count")
    st.pyplot(fig)

else:
    st.write("Upload a CSV file to start analysis.")
