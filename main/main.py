import streamlit as st


def main():
     
    st.set_page_config(
        page_title="Akif's Personal Web Site",
        page_icon="💻",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': 'akifemre611@hotmail.com',
            'Report a bug': "akifemre611@hotmail.com",
            'About': "Bu benim kişisel web sitem!"
        }

    )

    with st.sidebar:
        st.header("Menü")
    
    

if __name__ == "__main__":
    main()