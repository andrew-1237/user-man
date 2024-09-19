import streamlit as st
import pandas as pd 
import datatime 
st.title("login or register")

def menu():
  slect = st.text_input("enter L to log in or R to register").lower()
  if slect == "l":
    login()
  elif slect == "r":
    register()
  else:
    menu()
def register():
  surname = st.text_input("enter your surname").lower()
  forename = st.text_input("enter your forename").lower()
  birthday = st.text_input("enter your birthday like this 24031988 for someone born on 24 March 1988")
  password = st.text_input("enter a password")
  username = forename[0] + surname[1] + surname[2] + birthday
  st.write("your user name is " + username)
  st.write("your password is " + password)
  file=open("userlist.txt","a")
  file.write("\n" + username + "," + password + "," + forename + "," + birthday + "," + surname + "," + "no" + "," + "1" + ",")
  file.close()
  menu()

def adminf():
  st.write ("welcome admin")
  st.write("Line 14")


def login():
  enterdusername = st.text_input("enter user name")
  enterdpassword = st.text_input("enter password")
  if st.butten("check user"):
    file = open("userlist.csv", "r", encoding="utf-8-sig")
    user_found = False 
    for line in file:
      lines = line.strip().split(",")

  username = lines[0]
  password = lines[1]
  if enterdusername == username and enterdpassword == password:
    with open("userlog.csv", "a" newline='') as file: 
    file.write(username + "," + str(datetime.datetime.now().replace(microsecond=0)) + "\n)
    st.session_state.logged_in = true
    st.success("login successful")
    user_found = true 
    break 
  if not user_found:
    st.error("invaled user name or password")
  file.close()





menu()
