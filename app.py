from PIL import Image
import streamlit as st
from streamlit_option_menu import option_menu


with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Projects"],
    )


if selected == "Home":
    st.set_page_config(page_title="Home", page_icon=":waving_hand:")
    st.subheader("Привіт :wave:, це початковий веб")
    st.title("Я пробую зробити мій власний веб сайт")
    st.write("Мені подобаєця знавати нові речі наприклад як працює самальот і програмуваня з пайтон")
    st.write("[Як я цей сайт зробив >>](https://www.youtube.com/watch?v=VqgUkExPvLY)")

    # -----------assets---------------
    an225 = Image.open("images/an225.png")
    Py = Image.open("images/Py.png")

    # ----------containers------------
    with st.container():
        image_column, image_column2 = st.columns((1, 2))
        with image_column:
            st.image(Py)
        with image_column2:
            st.image(an225)

    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    if st.button("Музика", type="primary"):
        st.audio("audio/Four-Seasons-Vivaldi.ogg")


if selected == "Projects":
    st.set_page_config(page_title="Projects", page_icon=":face_with_monocle:")
    st.title("[thistest312.streamlit.app](https://github.com/Arseniy132/app.py)")