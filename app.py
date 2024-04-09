from PIL import Image
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Бульба", page_icon=":face_with_monocle:")

with st.sidebar:
    selected = option_menu(
        menu_title="Selection Menu",
        options=["Українська", "Spanish", "English", "Projects"],
    )


if selected == "Українська":
    st.subheader("Привіт :wave:, це початковий веб")
    st.title("Я пробую зробити мій власний веб сайт")
    st.write("Мені подобаєця знавати нові речі наприклад як працює самальот і програмуваня з пайтон")
    st.write("[Як я цей сайт зробив >>](https://www.youtube.com/playlist?list=PL7QI8ORyVSCaejt2LICRQtOTwmPiwKO2n)")

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
    st.title("[thistest312.streamlit.app](https://github.com/Arseniy132/app.py)")

if selected == "Spanish":
    st.subheader("Hola :wave:, esto es un sitio web principal")
    st.title("Estoy intentando crear mi propio sitio web")
    st.write("Me gusta saber nuevas cosas, por ejemplo, como funciona un avion y me gusta la programacion con Python")
    st.write("[Como he hecho este sitio web >>](https://www.youtube.com/playlist?list=PL7QI8ORyVSCaejt2LICRQtOTwmPiwKO2n)")

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
    if st.button("Musica", type="primary"):
        st.audio("audio/Four-Seasons-Vivaldi.ogg")

if selected == "English":
    st.subheader("Hello :wave:, this is a starter web")
    st.title("I'm trying to create my own web site")
    st.write("I like discovering new things, like how a plane works and I also like Python programming")
    st.write("[How I made this web site >>](https://www.youtube.com/playlist?list=PL7QI8ORyVSCaejt2LICRQtOTwmPiwKO2n)")

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
    if st.button("Music", type="primary"):
        st.audio("audio/Four-Seasons-Vivaldi.ogg")

if selected == "Projects":
    st.title("[thistest312.streamlit.app](https://github.com/Arseniy132/app.py)")
