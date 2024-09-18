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
def register():
  surname = st.text_input("enter your surname").lower()
  forename = st.text_input("enter your forename").lower()
  birthday = st.num_input("enter your birthday like this 24031988 for someone born on 24 March 1988")
  password = st.text_input("enter a password")
  username = forename[0] + surname[1] + surname[2] + birthday
  st.write("your user name is " + username)
  st.write("your password is " + password)
  file=open("userlist.txt","a")
  file.write("\n" + username + "," + password + "," + forename + "," + birthday + "," + surname + "," + "no" + "," + "1" + ",")
  file.close()
  menu()






menu()
