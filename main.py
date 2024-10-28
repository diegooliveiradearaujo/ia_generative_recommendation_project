import streamlit as st
import recommendation as r
import movies as m

st.set_page_config(
        page_title="MRS - Movie Recommendation System",
        page_icon="🖥️",  # Você pode usar um emoji ou um URL para uma imagem de ícone
        layout="wide"
    )

st.sidebar.title("Welcome to the MRS")

choice = st.sidebar.selectbox('Menu',['MRS','Movies and details'])
if choice=='MRS':
    r.start_rec()
elif choice == 'Movies and details':
    m.start_mov()
    

