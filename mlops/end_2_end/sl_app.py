import streamlit as st
import requests
import json

# Streamlit UI Title
st.title("Movie Review Sentiment Analysis")

# API endpoint
api_url = "http://localhost:8000/predict"

# Session state to store reviews
if "reviews" not in st.session_state:
    st.session_state.reviews = []

# Text input for user review
review_text = st.text_area("Enter your movie review:")

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

                # Save the review and sentiment
                st.session_state.reviews.append({"review": review_text, "sentiment": sentiment})

                # Display the result
                st.write(f"Predicted Sentiment: **{sentiment}**")
            else:
                st.write(f"Error: {response.status_code}, {response.text}")
        except requests.exceptions.RequestException as e:
            st.write(f"Request failed: {e}")
    else:
        st.write("Please enter a review before analyzing.")

# Display Review Count
if st.session_state.reviews:
    st.subheader("Review Statistics")

    # Count positive and negative reviews
    pos_count = sum(1 for r in st.session_state.reviews if r["sentiment"] == "Positive")
    neg_count = sum(1 for r in st.session_state.reviews if r["sentiment"] == "Negative")

    st.write(f"📈 **Total Reviews:** {len(st.session_state.reviews)}")
    st.write(f"✅ **Positive Reviews:** {pos_count}")
    st.write(f"❌ **Negative Reviews:** {neg_count}")

    # Show stored reviews
    st.subheader("Recent Reviews")
    for r in st.session_state.reviews[-5:]:  # Display last 5 reviews
        st.write(f"📌 **Review:** {r['review']}")
        st.write(f"🔍 **Sentiment:** {r['sentiment']}")
        st.write("---")
