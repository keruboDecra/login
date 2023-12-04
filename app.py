# app.py
import streamlit as st

def main():
    st.title("Simple Streamlit App")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "your_username" and password == "your_password":
            st.success("Login successful!")
        else:
            st.error("Invalid username or password")

if __name__ == "__main__":
    main()
