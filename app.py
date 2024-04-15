from openai import OpenAI
from PIL import Image
import streamlit as st
from streamlit_option_menu import option_menu

im = Image.open("Python.png")

st.set_page_config(page_title="Бульба", page_icon=im)











with st.sidebar:
    selected = option_menu(
        menu_title="Selection Menu",
        options=["Українська", "Español", "English", "Projects", "Bot"],
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









if selected == "Español":
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
    st.write(":)")
















if selected == "Projects":
    st.title("[thistest312.streamlit.app](https://github.com/Arseniy132/app.py)")





if selected == "Bot":
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-3.5-turbo"

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What is up?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            stream = client.chat.completions.create(
                model=st.session_state["openai_model"],
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,
            )
            response = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", "content": response})