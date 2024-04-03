from PIL import Image
import streamlit as st


st.set_page_config(page_title="My website", page_icon=":upside_down_face:", layout="wide")


st.subheader("Привіт :wave:, це початковий веб")
st.title("Я пробую зробити мій власний веб сайт")
st.write("Мені подобаєця знавати нові речі наприклад як працює самальот і програмуваня з пайтон")
st.write("[Як я цей сайт зробив >>](https://www.youtube.com/watch?v=VqgUkExPvLY)")

an225 = Image.open("images/an225.png")
Py = Image.open("images/Py.png")

with st.container():
    image_column, image_column2 = st.columns((1, 2))
    with image_column:
        st.image(Py)
    with image_column2:
        st.image(an225)