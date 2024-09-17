import streamlit as st

st.title("🎈 My new app")
st.write(
    "my first app [docs.streamlit.io](https://docs.streamlit.io/)."
)
name = st.text_input("enter your name")
st.write("welcome", name)
