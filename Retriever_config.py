from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS  # Swap with OracleVectorStore if needed
import os

# 🔐 Load your API key securely
openai_api_key = os.getenv("OPENAI_API_KEY")

def get_retriever(doc_path="data/sample_docs/context.txt", k=3):
    """
    Loads documents, splits them, embeds them, and returns a retriever.
    Includes basic error handling and fallback logic.
    """
    try:
        # 📄 Load documents
        loader = TextLoader(doc_path)
        documents = loader.load()

        # ✂️ Split into chunks
        splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = splitter.split_documents(documents)

        # 🧠 Embed documents
        embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
        vectorstore = FAISS.from_documents(chunks, embeddings)

        # 🔍 Return retriever
        return vectorstore.as_retriever(search_type="similarity", k=k)

    except Exception as e:
        print(f"[Retriever Config] Failed to initialize retriever: {e}")
        return None
