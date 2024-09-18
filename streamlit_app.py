import streamlit as st

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
  birthday = st.number_input("enter your birthday like this 24031988 for someone born on 24 March 1988")
  password = st.text_input("enter a password")
  username = forename[0] + surname[1] + surname[2] + birthday
  st.write("your user name is " + username)
  st.write("your password is " + password)
  file=open("userlist.txt","a")
  file.write("\n" + username + "," + password + "," + forename + "," + birthday + "," + surname + "," + "no" + "," + "1" + ",")
  file.close()
  menu()

def adminf():
  st.write("Line 14")


def login():
  enterdusername = st.text_input("enter user name")
  enterdpassword = st.text_input("enter password")
  file=open("userlist.txt","r")
  for line in file:
    lines = line.split(",")
    username = lines[0]
    password = lines[1]
    forename = lines[2]
    birthday = lines[3]
    surname = lines[4]
    admin = lines[5]
    
    if enterdusername == username and enterdpassword == password:
      if admin == "N":
        print( "welcome " + forename + " " + surname + " your birthday is " + birthday )
        menu()
      else:
        print ("welcome admin")
        adminf()




menu()
