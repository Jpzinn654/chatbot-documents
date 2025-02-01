import streamlit as st
from utils import embeddings, text

def main():

    st.set_page_config(page_title='LLM', page_icon="books")

    with st.sidebar:

        st.subheader('Arquivos')
        pdf_docs = st.file_uploader("Carregue PDF", accept_multiple_files=True)
        
        if st.button("Processar"):
            all_files_text = text.processor_files(pdf_docs)
            chunks = text.create_text_chunkc(all_files_text)
            vectorstore = embeddings.create_vectorstore(chunks)
            print(vectorstore)
if __name__ == "__main__":
    main()