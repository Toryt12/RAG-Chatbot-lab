import streamlit as st
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import FAISS  # Swap with OracleVectorStore if available
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
import os

# 🔐 Load your API key securely
openai_api_key = os.getenv("OPENAI_API_KEY")

# 🧠 Initialize LLM
llm = ChatOpenAI(temperature=0.3, openai_api_key=openai_api_key)

# 📚 Load and embed documents
def load_vector_store():
    try:
        loader = TextLoader("data/sample_docs/context.txt")
        documents = loader.load()
        splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = splitter.split_documents(documents)
        embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
        vectorstore = FAISS.from_documents(chunks, embeddings)
        return vectorstore
    except Exception as e:
        st.error(f"Vector store failed to load: {e}")
        return None

# 🧠 Build RAG chain with fallback
def build_chain(vectorstore):
    if vectorstore:
        retriever = vectorstore.as_retriever(search_type="similarity", k=3)
        return RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    else:
        return None

# 🖼️ Streamlit UI
st.title("🧠 RAG Chatbot Lab")
st.markdown("Ask a question based on your custom context!")

query = st.text_input("Enter your question:")

if query:
    vectorstore = load_vector_store()
    qa_chain = build_chain(vectorstore)

    if qa_chain:
        try:
            response = qa_chain.run(query)
            st.success(response)
        except Exception as e:
            st.warning(f"Fallback triggered: {e}")
            # Basic LLM response without retrieval
            fallback_response = llm.predict(query)
            st.info(f"LLM fallback response: {fallback_response}")
    else:
        st.error("Retriever not available. Please check vector store setup.")
