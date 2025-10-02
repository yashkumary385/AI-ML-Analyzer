import streamlit as st
import requests
st.title("Sentiment Analyzer 😊😐😢 ")
question = st.text_input("Enter Your Sentence")
url = "http://127.0.0.1:8000/predict"
text = {"text": question}
if st.button("Predict"):
    response = requests.post(url,json=text)
    response_data = response.json()
    if response.status_code == 200:
        st.success(response_data["sentiment"])
    else:
                st.error(f"POST request failed with status code: {response.status_code}")
                st.write(response.text)
    



