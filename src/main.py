import streamlit as st
from utils import chatbot, text
from streamlit_chat import message

def main():

    st.set_page_config(page_title='LLM', page_icon="books")

    st.header('Interaja com Seus Documentos Usando IA')
    user_question = st.chat_input("Faça uma pergunta")

    if ('conversation' not in st.session_state):
        st.session_state.conversation = None

    if (user_question):
        response = st.session_state.conversation(user_question)['chat_history']

        for i, text_message in enumerate(response):
            if (i % 2 == 0): 
                message(text_message.content, is_user=True, key=f'{i}' + '_user')
            else:
                message(text_message.content, is_user=False, key=f'{i}' + '_bot')

    with st.sidebar: 

        st.subheader('Arquivos')
        pdf_docs = st.file_uploader("Carregue PDF", accept_multiple_files=True)
        
        if st.button("Processar"):
            all_files_text = text.processor_files(pdf_docs)
            chunks = text.create_text_chunkc(all_files_text)
            vectorstore = chatbot.create_vectorstore(chunks)
            st.session_state.conversation = chatbot.create_conversation_chain(vectorstore)

if __name__ == "__main__":
    main()