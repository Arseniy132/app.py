from PIL import Image
import streamlit as st
import pygame
from pyChatGPT import ChatGPT
session_token = 'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..sOFPof0Q50xKBc-5.wa9V4nheY3GcjxaOQdoW1e3Av5yy8i9TZbv5QrBwQMqATQn4_x7T_XyHoVkagPE7_AaDQZeOxJdwIKz1ghXXUxM4cs7Gaguav7KLrlbdx4TKaQhHdDCZNRq_jHyvis4l3J5TptzTGDqZTSTDri1ruYjBsHjBYua6OgKD_5_lGUptWSxzu8LBcIPStE2yPNJG4qLLsReeofODf1pCPYLCYo2LY5W4psS9jHWQ9-qNJDE1L4RUO9i1lplA-oZB4uD9p_h7osLVOymn8W6eSKUFunvM6TJnz-rTQkF70b_5FdiiKZJ3lsvIRM6TitZheRZ-Lo0MAk9xpKgHu5OxqaRMNn45yYJpdD7QwUn-vUv0J2wt00kxlHkkpkbfnhoLSv8k9cT7TaOyLo_VVQGH-63Zwb9n-Up2AWuQg6TMBZxF8OKKjm5g1Fo0X14LNy1InrQ4e-9bbj7sHQpmRSgfH9YePEF0K9jn4uX1m5kLXYdie4zVaP3pFla78TPqjNm9ltIJy_dEQmQLvShCprkrBBo-ADo9ByojZTKfX0y8OwUQoeEaDxRgxSLOp1wCGCcyfxfCponF8FY-Lms56w44CDu6_JBUPpVDWDr7_mTLTGvCEx0u83wpB7O5yi4mu9VffBF80sgX9R8ONvjYe5finLyBTn3n24y0fLTm64o3GJOWR_AfW8vXIJLSw_1n4NHpNkMTWp9Xe2HeFzDQni_GKbbDg46wZ2w6dBREl5qZmbttcgTvr1uQQYB0lBdE0D_P9uGr7Rv00HpFeLx4B6KnhEHJkl0y3NP1s34Qk9A3425qs7Etxcr6Ob5KhSPFTEaA4YniTr-TP2xjYwbSCsSibHa7W_b0WXPBIZo_9k-A11FC2vr7r4UXG3w2DFHfa40aA09db2Y9j_8kOqYw2BbpXNLX2MGtNz9jmr2lIxeuZuUzGOtgxU0NxmVbUaEzeFey6vy_LYskKEQCt9PxeQDooS5eZ2mxuNn9PN_YDo2n9wgGsO7L0O5u4rBR7xPG60UP884PGzd_kz2Oj7rfc-VZbtVWNdH00VpbFvT3BCcqQUSwdKsPo0wHLW3NXx695WKG19JFTiw6Nhmr65fvvVkJOSXKAeFLeblJQ-yyR7ZnREAh54gZ-54d8Xjwz3QxFNkzDv9Ch4iUnAxnRdV6JV1DbgpJZOEoo8m7TbhePf2PvUhix1zbryamBEvB6ks1H4ifelQEPrS6CdIqjssEdjKWcUzIATbtgCOu8vmqNJCxc664u2BQ32LxWZOsATEqctvb2eCfM0n06BG09f_J-2wgTAK2r0LVceI2-9CvMsYioz9jFYKaKrvhJZ05CpxRm5OABfA_fWSpRMF-6vQE4QY6p61CtC0E4rfKcWWlZsovWvXrvQpYy5dgTBotbrOk2Y77ECh-ilY7K2BUo6VrHgVH4ImRWOOZGLXg8Zzk2LkC1noVbc9DwAIqHNUJqNh1hSx49uZPVlmjx1z16R6rsLVqjvDOMx3B15lEvQKqhHzwRMPKkPecOlR-5gpsoZhG3eBIoBmv9YN8NydZzuxKJ6wVvhmBEZ135I-vvnPgK-e47ArTnFrdNMl_6WY_J-9cP5VS1PspbX_1w3iCjSb6N8ewfYYGYOHx0O6834ombk3eazilKZnsXp6mlsRq3laMjsgxTkYtmylZ5Qp8vZQrcKHxkP52ezB1Ctr0Q1WO0bJiN6XxLONuYvD1wReIp2dVGR9sXtYBE3J8n7c9p8IqsP8-YxVBrOBwm2PT8Fn_ubsVbtNa8C3Hu_GcmtHNA0JpcA9ZIGWL5_5JZW_5YzNxJb1BmXAXDB7zcCvefz7VthDp6sAEXu57jXhGBYr0OQA6FDjs7LpnEguxcjHHqbGHXelfO2go152RQRfxYesYZbaYTO7WksaJ5peROX0AAX2x_txja_J2lyD4jl1S8_CGS7baEclNbUsam0PoJq9kjsSYc7p_5YUnv7IwvJ_vzd7uPXC4c_YoDvVVPc0s_m9BAOT09pDHNesPaUOBgrQSlxTooG6fah2pvp8Udcb3DQEZhToATqcmJGsrgWGMIwBhMBAvkWUQgjPM9a1pqd2nq4JDF2Mt1SFGqu-awnlOMlLo9F9lZ3lqWXBVkw0rDTLPp_7N4NgHMw9oxDErHFA1QIAqX6M8y4oiuZ0GAqNn73EIwCybwiQjmRnlTszBfxVrlJPuF3QqDHBxgG-i7_0O38R5XWwIQ6UUTiltzfyQURpJOuU-WyhFGB9Z3UIEFxrhh-WXv_tu2_9J_aarQfbOJAN58ZCwK3FafS4nXLDXkYb6u-1KokZktgwnk9R7Qcru6nbmQwtPPPfuY9_SanH5UqubTsFU-1zPBjFrJ0MCt4fpzLMmpvKzeQ8Is-u4uNa9QM_zQ8cIOAh1Cm-9zqeS8mkabC765GeOs0cz1RMnW7UXnFabTZowZ85aInI1MDXe4Xv35Sb6PlBiRUQU0qFGe5lblQAqpokAPIkWyhrDUrnUQK0ZRXq1rtTdczGOxKOuCao9jvYAD3N_BUffRf0msHzhyoFXS29NdWro-xJCRM41IzHbi8tsKK8UJ3L9NTxDoPhZBy0SCGNJj2Xj0gl2YvDtZgD606MCIzmJ_fh4hSC0AJUc4NuItPR7MEH0LahEl0fRam1Hd1PH_70MFNRoFiyAqCZz3r9g-lRHMLrRtyIV9z0tQjEQeBDDmCd4qCbmqQvQGZI-BvM5ZFyfvjoC--BEF1jRDfV2ilFy9nusHXpzfWj9a1LZhrp9bnHuaN4G-0SafbMyTI0uEytpHRfz2zpeKQRHTxgauB4s79KtQqUgpsAhYiRgQa8Y-_M7d8s6rW-UsBii8bP5ZYc3TIs-hb4R3C7RpDLC81aypEF2-yIlNFmr8GltjQ.Q_bVZ1NWrbbKtUry--5oGw'

api = ChatGPT(session_token)

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
        text_contents = ''''''
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

send_ = st.text_input('Movie title', 'Life of Brian')

message = ChatGPT.send_message(send_)

st.write(message)