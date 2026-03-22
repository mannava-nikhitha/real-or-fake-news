import streamlit as st
from model import predict_news

st.set_page_config(page_title="Fake News Detection", layout="centered")

st.title("📰 Fake News Detection App")

st.write("Enter a news article below to check whether it is Fake or Real.")

# User input only
news_input = st.text_area("Enter News Text:")

# No threshold shown to user
THRESHOLD = 0.8  # fixed internally

if st.button("Predict"):
    if news_input.strip() == "":
        st.warning("Please enter some news text.")
    else:
        result, fake_prob, real_prob = predict_news(news_input,THRESHOLD)

        st.subheader("Prediction:")
        st.write(result)

        st.subheader("Confidence:")
        st.write(f"Fake Probability: {fake_prob*100:.2f}%")
        st.write(f"Real Probability: {real_prob*100:.2f}%") 
