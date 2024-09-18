import streamlit as st

st.title("🎈 My new app")
st.write("my first app")
name = st.text_input("enter your name")
st.write("welcome", name)

def menu():
  slect = st.text_input("enter L to log in or R to register").lower()
  if slect == "l":
    login()
  elif slect == "r":
    register()
  else:
    menu()







menu()
