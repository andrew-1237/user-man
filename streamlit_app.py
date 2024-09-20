import streamlit as st
import pandas as pd
import datetime

st.title("User Management")

def login():
    ename = st.text_input("Enter username")
    epass = st.text_input("Enter password", type="password")
   
    if st.button("Check user"):
        # Open the userlist.csv file and read through its contents
        file = open("userlist.csv", "r", encoding="utf-8-sig")
        user_found = False
        for line in file:
            lines = line.strip().split(",")

            username = lines[0]
            password = lines[1]
            if ename == username and epass == password:
                # Log the successful login attempt
                with open("userlog.csv", "a", newline='') as file_log:
                    file_log.write(username + "," + str(datetime.datetime.now().replace(microsecond=0)) + "\n")
                st.session_state.logged_in = True
                st.success("Login successful")
                user_found = True
                break
        if not user_found:
            st.error("Invalid username or password")
        file.close()

def dashboard():
    st.write("Welcome Admin")
   
    if st.button("Sign out"):
        st.session_state.logged_in = False
   
    st.title("User Management and Login Record")
    choice = st.sidebar.radio("Select Add, Remove or View", ["Add", "Remove", "View"])
   
    if choice == "Add":
        username = st.text_input("Enter a username to add")
        password = st.text_input("Enter a password to add", type="password")
       
        if st.button("Add user"):
            with open("userlist.csv", "a", newline='') as file:
                file.write(username + "," + password + "\n")
            st.success(f"User {username} added successfully.")
   
    elif choice == "Remove":
        username = st.text_input("Enter a username to remove")
       
        if st.button("Remove user"):
            df = pd.read_csv("userlist.csv")
            if username in df["username"].values:
                df = df[df["username"] != username]
                df.to_csv("userlist.csv", index=False)
                st.success(f"User {username} removed successfully.")
            else:
                st.error(f"User {username} not found in the database.")
   
    else:
        st.write("User List:")
        df = pd.read_csv("userlist.csv", names=["username", "password"])
        st.dataframe(df)
       
        st.write("Login Records:")
        df_log = pd.read_csv("userlog.csv", names=["username", "timestamp"])
        st.dataframe(df_log)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in:
    dashboard()
else:
    login()
