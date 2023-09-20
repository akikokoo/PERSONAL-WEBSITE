import streamlit as st
import os

html:str = []

def read_html(file_name):
    with open(f'html/{file_name}',"r") as f:
        return f.read()


def get_files():
    dir_path = r'html'
    for path in os.scandir(dir_path):
        if path.is_file():
            html.append(path.name)

def main():
    
    st.set_page_config(
        page_title="Akif's Personal Web Site",
        page_icon="💻",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': None,
            'Report a bug': None,
            'About': "Bu benim kişisel web sitem!"
        }

    )

    get_files() #retrieve html files

    #SIDEBAR
    with st.sidebar:
        st.header("Is that a JoJo Reference!?!?")
        selected = st.selectbox(label="Menu",options=["About", "Contacts", "CV"], index=0)

    #SELECT CONDITION
    if selected == "About":
        file = "about.html"
        st.markdown(f'''
            {read_html(file)}
        ''',
        unsafe_allow_html=True
        )
    elif selected == "Contacts":
        file = "contacts.html"
        st.markdown(f'''
            {read_html(file)}
        ''',
        unsafe_allow_html=True
        )
    elif selected == "CV":
        file = "cv.html"
        st.markdown(f'''
            {read_html(file)}
        ''',
        unsafe_allow_html=True
        )
    

if __name__ == "__main__":
    main()