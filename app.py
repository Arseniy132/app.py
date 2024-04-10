from PIL import Image
import streamlit as st
from streamlit_option_menu import option_menu

im = Image.open("Python.png")

st.set_page_config(page_title="Бульба", page_icon=im)











with st.sidebar:
    selected = option_menu(
        menu_title="Selection Menu",
        options=["Українська", "Español", "English", "Projects", "Youtube"],
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





if selected == "Youtube":
    if 'status' not in st.session_state:
        st.session_state['status'] = 'submitted'

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'ffmpeg-location': './',
        'outtmpl': "./%(id)s.%(ext)s",
    }

    transcript_endpoint = "https://api.assemblyai.com/v2/transcript"
    upload_endpoint = 'https://api.assemblyai.com/v2/upload'

    headers_auth_only = {'authorization': auth_key}
    headers = {
        "authorization": auth_key,
        "content-type": "application/json"
    }
    CHUNK_SIZE = 5242880


    @st.cache
    def transcribe_from_link(link, categories: bool):
        _id = link.strip()

        def get_vid(_id):
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                return ydl.extract_info(_id)

        # download the audio of the YouTube video locally
        meta = get_vid(_id)
        save_location = meta['id'] + ".mp3"

        print('Saved mp3 to', save_location)

        def read_file(filename):
            with open(filename, 'rb') as _file:
                while True:
                    data = _file.read(CHUNK_SIZE)
                    if not data:
                        break
                    yield data

        # upload audio file to AssemblyAI
        upload_response = requests.post(
            upload_endpoint,
            headers=headers_auth_only, data=read_file(save_location)
        )

        audio_url = upload_response.json()['upload_url']
        print('Uploaded to', audio_url)

        # start the transcription of the audio file
        transcript_request = {
            'audio_url': audio_url,
            'iab_categories': 'True' if categories else 'False',
        }

        transcript_response = requests.post(transcript_endpoint, json=transcript_request, headers=headers)

        # this is the id of the file that is being transcribed in the AssemblyAI servers
        # we will use this id to access the completed transcription
        transcript_id = transcript_response.json()['id']
        polling_endpoint = transcript_endpoint + "/" + transcript_id

        print("Transcribing at", polling_endpoint)

        return polling_endpoint


    def get_status(polling_endpoint):
        polling_response = requests.get(polling_endpoint, headers=headers)
        st.session_state['status'] = polling_response.json()['status']


    def refresh_state():
        st.session_state['status'] = 'submitted'


    st.title('Easily transcribe YouTube videos')

    link = st.text_input('Enter your YouTube video link', 'https://youtu.be/dccdadl90vs', on_change=refresh_state)
    st.video(link)

    st.text("The transcription is " + st.session_state['status'])

    polling_endpoint = transcribe_from_link(link, False)

    st.button('check_status', on_click=get_status, args=(polling_endpoint,))

    transcript = ''
    if st.session_state['status'] == 'completed':
        polling_response = requests.get(polling_endpoint, headers=headers)
        transcript = polling_response.json()['text']

    st.markdown(transcript)
