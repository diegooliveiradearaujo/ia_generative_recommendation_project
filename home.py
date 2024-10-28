import streamlit as st
import recommendation as r
import movies as m
import main as ma

def menu():
    st.sidebar.title("Welcome to the MRS")
    
    choice = st.sidebar.selectbox('Menu',['MRS','Movies and details'])
    if choice=='MRS':
        r.start_rec()
    elif choice == 'Movies and details':
        m.start_mov()

    if st.sidebar.button('Logout'):
        ma.logout()

    

