from PIL import Image
import streamlit as st

st.set_page_config(page_title="My website", page_icon=":upside_down_face:", layout="wide")

st.subheader("Привіт :wave:, це початковий веб")
st.title("Я пробую зробити мій власний веб сайт")
st.write("Мені подобаєця знавати нові речі наприклад як працює самальот і програмуваня з пайтон")
st.write("[Як я цей сайт зробив >>](https://www.youtube.com/watch?v=VqgUkExPvLY)")


#-----------assets---------------
an225 = Image.open("images/an225.png")
Py = Image.open("images/Py.png")


#----------containers------------
with st.container():
    image_column, image_column2 = st.columns((1, 2))
    with image_column:
        st.image(Py)
    with image_column2:
        st.image(an225)

with st.container():
    text_column, download_column = st.columns((1, 2))
    with text_column:
        st.write("Поміняйте розшириня від .txt до .py")
        text_contents = '''
from PIL import Image
import streamlit as st

st.set_page_config(page_title="My website", page_icon=":upside_down_face:", layout="wide")

st.subheader("Привіт :wave:, це початковий веб")
st.title("Я пробую зробити мій власний веб сайт")
st.write("Мені подобаєця знавати нові речі наприклад як працює самальот і програмуваня з пайтон")
st.write("[Як я цей сайт зробив >>](https://www.youtube.com/watch?v=VqgUkExPvLY)")


#-----------assets---------------
an225 = Image.open("images/an225.png")
Py = Image.open("images/Py.png")


#----------containers------------
with st.container():
    image_column, image_column2 = st.columns((1, 2))
    with image_column:
        st.image(Py)
    with image_column2:
        st.image(an225)

with st.container():
    text_column, download_column = st.columns((1, 2))
    with text_column:
        text_contents = '''from PIL import Image
import streamlit as st

st.set_page_config(page_title="My website", page_icon=":upside_down_face:", layout="wide")

st.subheader("Привіт :wave:, це початковий веб")
st.title("Я пробую зробити мій власний веб сайт")
st.write("Мені подобаєця знавати нові речі наприклад як працює самальот і програмуваня з пайтон")
st.write("[Як я цей сайт зробив >>](https://www.youtube.com/watch?v=VqgUkExPvLY)")


#-----------assets---------------
an225 = Image.open("images/an225.png")
Py = Image.open("images/Py.png")


#----------containers------------
with st.container():
    image_column, image_column2 = st.columns((1, 2))
    with image_column:
        st.image(Py)
    with image_column2:
        st.image(an225)

with st.container():
    text_column, download_column = st.columns((1, 2))
    with text_column:
        st.write("Поміняйте розшириня від .txt до .py")
        text_contents = ''''''
    with download_column:
        st.download_button('app.py', text_contents)


with st.container():
    text, download_images = st.columns((1, 2))
    with text:
        st.write("Створіть папку з ім'ям images, і там поставте фотки мрії і Python.")
    with download_images:
        with open("images/an225.png", "rb") as file:
            btn = st.download_button(
                    label="Мрія",
                    data=file,
                    file_name="an225.png",
                    mime="image/png"
                  )
        with open("images/Py.png", "rb") as file:
            btn = st.download_button(
                label="Python",
                data=file,
                file_name="Py.png",
                mime="image/png"
            )

with st.container():
    text_toml, download_toml = st.columns((1, 2))
    with text_toml:
        st.write("Поміняти розширеня файлу від .txt до .toml і створити папку .streamlit")
    with download_toml:
        text_contents = '''[theme]

# Primary accent for interactive elements
primaryColor = '#E694FF'

# Background color for the main content area
backgroundColor = '#318500'

# Background color for sidebar and most interactive widgets
secondaryBackgroundColor = '#0083B8'

# Color used for almost all text
textColor = '#000000'

# Font family for all text in the app, except code blocks
# Accepted values (serif | sans serif | monospace)
# Default: "sans serif"
font = "sans serif"'''
        st.download_button('config.toml', text_contents)


st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
if st.button("Музика", type="primary"):
    st.audio("audio/Four-Seasons-Vivaldi.ogg")'''

    with download_column:
        st.download_button('app.py', text_contents)'''
    with download_column:
        st.download_button('app.py', text_contents)


with st.container():
    text, download_images = st.columns((1, 2))
    with text:
        st.write("Створіть папку з ім'ям images, і там поставте фотки мрії і Python.")
    with download_images:
        with open("images/an225.png", "rb") as file:
            btn = st.download_button(
                    label="Мрія",
                    data=file,
                    file_name="an225.png",
                    mime="image/png"
                  )
        with open("images/Py.png", "rb") as file:
            btn = st.download_button(
                label="Python",
                data=file,
                file_name="Py.png",
                mime="image/png"
            )

with st.container():
    text_toml, download_toml = st.columns((1, 2))
    with text_toml:
        st.write("Поміняти розширеня файлу від .txt до .toml і створити папку .streamlit")
    with download_toml:
        text_contents = '''[theme]

# Primary accent for interactive elements
primaryColor = '#E694FF'

# Background color for the main content area
backgroundColor = '#318500'

# Background color for sidebar and most interactive widgets
secondaryBackgroundColor = '#0083B8'

# Color used for almost all text
textColor = '#000000'

# Font family for all text in the app, except code blocks
# Accepted values (serif | sans serif | monospace)
# Default: "sans serif"
font = "sans serif"'''
        st.download_button('config.toml', text_contents)


st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
if st.button("Музика", type="primary"):
    st.audio("audio/Four-Seasons-Vivaldi.ogg")
