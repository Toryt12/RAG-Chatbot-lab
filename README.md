# RAG-Chatbot-lab
Retrieval-Augmented Generation chatbot using LangChain, vector search, and fallback logic
# 🤖 RAG Chatbot Lab

This lab builds a Retrieval-Augmented Generation (RAG) chatbot using LangChain, Oracle AI Vector Search, and fallback logic for robust enterprise-grade performance.

## 🧰 Tools & Tech
- LangChain (v0.1+)
- Oracle 23ai Vector Search
- FAISS / Chroma (for local testing)
- Python (3.10+)
- Streamlit (for UI)
- Custom fallback logic for query failures

## 🧪 Lab Objectives
- Build a chatbot that retrieves context from vector store before generating responses
- Handle edge cases like empty retrievals, malformed queries, and token overflows
- Document LangChain import structure changes and troubleshooting steps

## 🐛 Common Errors & Fixes
| Error | Fix |
|------|-----|
| `ImportError: cannot import name 'RetrievalQA'` | LangChain module structure changed—use `from langchain.chains import RetrievalQA` |
| `ValueError: No documents returned from retriever` | Add fallback prompt or default context; validate vector store indexing |
| `TokenLimitExceeded` | Use `tiktoken` to estimate token count; chunk documents before embedding |
| `AttributeError: 'NoneType' object has no attribute 'page_content'` | Check retriever output; add null checks before passing to LLM |
| `ModuleNotFoundError: No module named 'langchain.vectorstores.oracle'` | Confirm Oracle plugin install and correct version; fallback to FAISS for local dev |

## 🧠 Lessons Learned
- LangChain evolves fast—always check version-specific docs
- Fallback logic is essential for enterprise reliability
- Token management and chunking are key for long-context RAG

## 🚀 Next Steps
- Add Streamlit UI for interactive testing
- Integrate OCI logging and monitoring
- Expand to multi-source RAG (PDFs, websites, structured data)

## 👤 Author
**Torian Thurmond**  
QA | Cloud | GenAI | Security  
Oracle AI Certified | CompTIA Security+ (in progress)  
[LinkedIn](https://www.linkedin.com/in/your-profile) | 
