from PIL import Image
import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My website", page_icon=":upside_down_face:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.subheader("Привіт :wave:, це початковий веб")
st.title("Я пробую зробити мій власний веб сайт")
st.write("Мені подобаєця знавати нові речі наприклад як працює самальот і програмуваня з пайтон")
st.write("[Як я цей сайт зробив >>](https://www.youtube.com/watch?v=VqgUkExPvLY)")


#-----------assets---------------
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
an225 = Image.open("images/an225.png")
Py = Image.open("images/Py.png")


#----------containers------------
with st.container():
    image_column, image_column2, code = st.columns((1, 2, 3))
    with image_column:
        st.image(Py)
    with image_column2:
        st.image(an225)
    with code:
        st_lottie(lottie_coding, height=300, key="coding")