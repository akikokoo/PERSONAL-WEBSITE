import streamlit as st
from PIL import Image
import pandas as pd


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
        page_icon="💻",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': None,
            'Report a bug': None,
            'About': "Bu benim kişisel web sitem!"
        }
    )
    
    get_project_data("./files/projects/excel/project_descriptions.xlsx")

    for i in range(len(data)):
        open_project_image(data.iloc[i,1])
        st.markdown(f'''
        <p align="center">{data.iloc[i,0]}</p>
        ''',unsafe_allow_html=True)
        

if __name__ == "__main__":
    main()