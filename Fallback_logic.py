from langchain.chat_models import ChatOpenAI
import os

# 🔐 Load your API key securely
openai_api_key = os.getenv("OPENAI_API_KEY")

# 🧠 Initialize fallback LLM
fallback_llm = ChatOpenAI(temperature=0.5, openai_api_key=openai_api_key)

def handle_empty_retrieval(query):
    """
    Triggered when retriever returns no documents.
    Responds with a generic LLM answer and a helpful message.
    """
    fallback_intro = "I couldn’t find relevant context, but here’s a general response:"
    try:
        response = fallback_llm.predict(query)
        return f"{fallback_intro}\n\n{response}"
    except Exception as e:
        return f"Fallback failed: {e}"

def handle_malformed_query():
    """
    Triggered when the query is empty, too short, or malformed.
    """
    return "Your question seems unclear or incomplete. Try rephrasing it with more detail."

def handle_token_overflow():
    """
    Triggered when input exceeds token limits.
    """
    return "Your input is too long for processing. Try shortening your question or breaking it into parts."

INPORT FALLBACK LOGIC
from fallback_logic import handle_empty_retrieval, handle_malformed_query, handle_token_overflow
if not query.strip():
    st.warning(handle_malformed_query())
else:
    try:
        response = qa_chain.run(query)
        st.success(response)
    except ValueError as ve:
        if "No documents returned" in str(ve):
            st.info(handle_empty_retrieval(query))
        elif "token" in str(ve).lower():
            st.warning(handle_token_overflow())
        else:
            st.error(f"Unhandled error: {ve}")
