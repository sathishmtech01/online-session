import streamlit as st
import requests
import json

# Streamlit UI
st.title("Movie Review Sentiment Analysis")

# Text input for user review
review_text = st.text_area("Enter your movie review:")

# API endpoint
api_url = "http://localhost:8000/predict"

if st.button("Analyze Sentiment"):
    if review_text.strip():
        # Prepare the payload
        payload = {"review": review_text}

        try:
            # Make a POST request to the API
            response = requests.post(api_url, json=payload)

            # Check if request was successful
            if response.status_code == 200:
                result = response.json()
                sentiment = result.get("prediction", "Unknown")
                st.write(f"Predicted Sentiment: {sentiment}")
            else:
                st.write(f"Error: {response.status_code}, {response.text}")
        except requests.exceptions.RequestException as e:
            st.write(f"Request failed: {e}")
    else:
        st.write("Please enter a review before analyzing.")
