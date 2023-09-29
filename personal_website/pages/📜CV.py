import streamlit as st
import base64

def displayPDF(file):
    # Opening file from file path
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="1100" height="1000" type="application/pdf"></iframe>'
    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)

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

    displayPDF("files/cv/cv.pdf")
    

    
    

if __name__ == "__main__":
    main()