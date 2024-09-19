import streamlit as st
import pandas as pd 
import datetime 
st.title("login or register")

'''def login():
  enterdusername = st.text_input("enter user name")
  enterdpassword = st.text_input("enter password")
  if st.button("check user"):
    file = open("userlist.csv", "r", encoding="utf-8-sig")
    user_found = False 
    for line in file:
      lines = line.strip().split(",")

      username = lines[0]
      password = lines[1]
      if enterdusername == username and enterdpassword == password:
        with open("userlog.csv", "a", newline='') as file: 
          file.write(username + "," + str(datetime.datetime.now().replace(microsecond=0)) + "\n")
          st.session_state.logged_in = true
          st.success("login successful")
          user_found = True 
          break 
    if not user_found:
      st.error("invaled user name or password")
    file.close()''

def dashboard():
  st.write("wecome admin")
  if st.button("sign out"):
    st.session_state.logged_in = false 
  st.title("user mangmet and logine recored")
  choice = st.sidebar.radio("slect add, remove or view",
  [":rainbow[Add]", ":rainbow[Remove]", ":rainbow[View]"])
  if choice ==":rainbow[Add]": 
    username = st.text_input("enter a user name to add")
    password = st.text_input("enter a password to add") 
    if st.button("add user"):
      with open("userlist.csv", "a", newline='') as file:
        file.write(username + "," + password+ "/n")
  elif choice ==  ":rainbow[Remove]":
    username = st.text_input("enter a username to remove")
    if st.button("remove user"):
      df = pd.read_csv("userlist.csv")
      if username in df["username"].values:
        df = df[df["username"] != username]
        df.to_csv("userlist.csv", index=false)
        st.success(f"user{username} removed successfully.")
    else:  
      st.error (f"user{username} not found in dater.")
  else:
    df = pd.read_csv("userlist.csv")
    st.dataframe(df)
    df = pd.read_csv("userlog.csv")
    st.dataframe(df)
    
if "logged_in" not in st.session_state:
  st.session_state.logged_in=False

if st.session_state.logged_in: 
  dashboard()
else:
  login()
    
dasboard()
