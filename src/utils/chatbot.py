from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEndpoint, HuggingFaceEmbeddings
from langchain.memory import ConversationBufferMemory
from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain.chains.llm import LLMChain
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain

def create_vectorstore(chunks):
    try:
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        vectorstore = FAISS.from_texts(texts=chunks, embedding=embeddings)
        
        vectorstore.save_local('false_default')

        return vectorstore
    except Exception as e:
        print(f"Error creating embeddings: {e}")
        raise

def create_conversation_chain(vectorstore):
    llm = HuggingFaceEndpoint(
        repo_id="google/flan-t5-large", 
        task='text-generation',
        temperature=0.1,
        model_kwargs={"max_length": 512},
    )

    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)

    question_prompt = PromptTemplate(
        template="Given the following conversation and a follow up question, rephrase the follow up question to be a standalone question.\n\nChat History:\n{chat_history}\n\nFollow Up Input: {question}\n\nStandalone question:",
        input_variables=["chat_history", "question"]
    )

    question_generator_chain = LLMChain(llm=llm, prompt=question_prompt)

    combine_docs_chain = load_qa_chain(llm, chain_type="stuff")

    conversation_chain = ConversationalRetrievalChain(
        combine_docs_chain=combine_docs_chain,
        question_generator=question_generator_chain,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )

    return conversation_chain