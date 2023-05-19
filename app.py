from dotenv import load_dotenv
import os
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback


def main():
    load_dotenv()
    st.set_page_config(page_title='Ask your pdf')
    st.header('Ask your pdf')

    # upload the file
    pdf = st.file_uploader('Please upload your pdf', type='pdf')

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
        # st.write(chunks)

        # We will use FAISS to search for the most similar chunks. This is the Facebook AI Similarity Search library.
        embeddings = OpenAIEmbeddings()
        knowledge_base = FAISS.from_texts(chunks, embeddings)

        user_question = st.text_input('Ask your question about your pdf')

        if user_question:
            docs = knowledge_base.similarity_search(user_question)
            # st.write(docs)

            llm = OpenAI()
            chain = load_qa_chain(llm, chain_type="stuff")
            chain.run(input_documents=docs, question=user_question)
            with get_openai_callback() as cb:
                response = chain.run(input_documents=docs,
                                     question=user_question)
                print(cb)
            st.write(response)


if __name__ == '__main__':
    main()
