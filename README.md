# Chatbot with RAG (Retrieval-Augmented Generation)

![Demo](https://img.shields.io/badge/Demo-Video-blue)  


https://github.com/user-attachments/assets/a9e619be-f96d-45ba-a81b-957f0e66f51d



## 📝 Description  
This project is a **Chatbot with RAG (Retrieval-Augmented Generation)** that uses the **FAISS RAG method** and **LangChain** to provide intelligent and context-aware responses. The chatbot is designed to:  
- Understand your queries in **Portuguese**.  
- Read and process **PDF documents** uploaded by users.  
- Allow users to interact with their documents using **AI-powered conversational capabilities**.  

The chatbot leverages advanced NLP techniques to retrieve relevant information from the uploaded documents and generate accurate responses based on the context.  

---

## 🚀 Features  
- **Document Upload**: Users can upload their PDF documents for the chatbot to process.  
- **FAISS RAG**: Utilizes FAISS for efficient similarity search and retrieval of relevant document chunks.  
- **LangChain Integration**: Enhances the chatbot's ability to handle complex queries and generate context-aware responses.  
- **Portuguese Language Support**: The chatbot understands and responds to queries in Portuguese.  
- **Interactive Interface**: A user-friendly interface for seamless interaction with the chatbot.  

---

## 📂 How to Install  

### Prerequisites  
- Python 3.8 or higher  
- pip (Python package manager)  

### Installation Steps  
1. Clone the repository:  
   ```bash
   git clone https://github.com/Jpzinn654/chatbot-documents
   ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    Set up the environment variables:
    Create a .env file in the root directory.
    ```


3. Run the application:
    ```bash
    cd src
    streamlit run main.py
    ```

- Open your browser and navigate to http://localhost:8501 to access the chatbot interface.

## 🛠️ How to Use
Upload a PDF Document:

- Click on the "Carregue PDF" button and select your document, after this click on "Processar", and wait to process

- Type your question in Portuguese in the chat input box, The chatbot will retrieve relevant information from the document and provide a response.

- Continue asking questions or request summaries, explanations, or specific details from the document.

## 📄 Technologies Used
- FAISS: For efficient similarity search and document retrieval.

- LangChain: For building the conversational AI pipeline.

- Streamlit: For the user-friendly web interface.

- Google/Flan-T5-Large: For advanced natural language understanding and generation.

## 🤝 Contributing
- Contributions are welcome! If you'd like to contribute, please follow these steps:

- Fork the repository, Create a new branch for your feature or bug fix, Commit your changes. Submit a pull request.

## 📜 License
- This project is licensed under the MIT License. See the LICENSE file for details.
