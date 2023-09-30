import streamlit as st
from PIL import Image
import pandas as pd
import os

def get_project_data(file):
    global data
    data = pd.read_excel(file)
    

def open_project_image(file):
    image = Image.open(file)
    col1, col2, col3 = st.columns([1,100,100])

    with col1:
        st.write("")

    with col2:
        st.image(image, width=800)

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
    
    personal_projects_path = os.path.join("files", "projects", "excel", "project_descriptions.XLSX")
    get_project_data(personal_projects_path)

    for i in range(len(data)):
        st.markdown(f'''
        <h1 align="center">{data.iloc[i,0]}</h1>
        ''',unsafe_allow_html=True)
        st.markdown(f'''
        <a href={data.iloc[i,3]} align="center"><h4 align="center">App Link</h4></a>
        ''',unsafe_allow_html=True)
        open_project_image(data.iloc[i,2])
        st.markdown(f'''
        <p align="center">{data.iloc[i,1]}</p>
        ''',unsafe_allow_html=True)
        

if __name__ == "__main__":
    main()