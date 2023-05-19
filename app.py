from dotenv import load_dotenv
import os
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter


def main():
    load_dotenv()
    print(os.getenv("OPENAI_API_KEY"))
    print('Hello World!')
    st.set_page_config(page_title='Ask your pdf')
    st.header('Ask your pdf')

    # upload the file
    pdf = st.file_uploader('upload your pdf', type='pdf')

    # extract the text
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        st.write(len(pdf_reader.pages))
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        # st.write(text)

        # split into chunks

        text_splitter = CharacterTextSplitter(
            separator='\n',
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )

        chunks = text_splitter.split_text(text)

        st.write(chunks)


if __name__ == '__main__':
    main()
