import streamlit as st
import home as h

st.set_page_config(
        page_title="MRS - Movies Recommendation System",
        page_icon="🖥️",
        layout="wide")

def logout():
    st.session_state.logged = False
    st.session_state.login =  False
    st.experimental_rerun()

def check():
    if 'logged' not in st.session_state:
        st.session_state.logged = False

def logged():
    h.menu()

def login():
    st.title("MRS - Movies Recommendation System")
    name = st.text_input('User:')
    password = st.text_input('Password:',type='password')
    
    if st.button('Log in'):
        if name=='admin' and password == 'admin':
            st.session_state.logged = True
            st.experimental_rerun()
            logged()
        else:
            st.write("User/Password incorrect")

check()

if st.session_state.logged:
    logged()
else:
    login()