from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
import openai
from secret.openai_credentials import *

openai.api_key = openai_api_key


def create_vectorstore(chunks):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts=chunks, embedding=embeddings)
    return vectorstore