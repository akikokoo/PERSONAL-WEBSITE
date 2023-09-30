import streamlit as st
from PIL import Image
import os

def open_image(file):
    image = Image.open(file)
    col1, col2, col3 = st.columns([1,1,1])

    with col1:
        st.write("")

    with col2:
        st.image(image, width=350)

    with col3:
        st.write("")

def main():
    
    st.set_page_config(
        page_title="Akif's Personal Web Site",
        page_icon="👨‍💻",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': None,
            'Report a bug': None,
            'About': "Bu benim kişisel web sitem!"
        }

    )

    personal_photo_path = os.path.join("files","personal_photos","akif_photo.jpeg")

    st.markdown("<h1 style='text-align: center; color: black;'>Welcome To My Precious Web Site</h1>", unsafe_allow_html=True)
    open_image(personal_photo_path)
    st.write("Hello stranger, my name is Akif Emre Reis but everybody calls me Akif(Yes i like JoJo references).Currently i am pursuing bachelor's degree on Artificial Intelligence\
             Engineering at TOBB ETÜ and i am the president of the App Development Club of our Computer Science Community.Beyond that i work on a blockchain project on the backend side to develop a REST API.\
             I do care to embrace opportunities that facilitate personal growth.In my free time I like to play video games and do research about specific topics on sociology and history")
    

if __name__ == "__main__":
    main()