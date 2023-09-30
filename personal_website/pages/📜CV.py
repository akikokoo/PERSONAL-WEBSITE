import streamlit as st
from PIL import Image
import os

def open_image(file):
    image = Image.open(file)
    col1, col2, col3 = st.columns([2,1,6])

    with col1:
        st.write("")

    with col2:
        st.image(image, width=600)

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

    personal_cv_path = os.path.join("files","cv","cv.png")

    open_image(personal_cv_path)
    
    

    
    

if __name__ == "__main__":
    main()