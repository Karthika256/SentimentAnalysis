import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load('sentiment_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# App UI
st.title("Restaurant Review Sentiment Analyzer 🍽️")
st.markdown("Type in a restaurant review and find out if it's **Good** or **Bad**!")

# Input box
user_input = st.text_area("Write your review here:")

# Predict
if st.button("Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter a review to analyze.")
    else:
        input_vector = vectorizer.transform([user_input])
        prediction = model.predict(input_vector)[0]
        sentiment = "👍 Good Review" if prediction == 1 else "👎 Bad Review"
        st.success(f"Prediction: **{sentiment}**")
