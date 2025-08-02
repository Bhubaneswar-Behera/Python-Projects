from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

def create_qa_chain(pages):
    print("[DEBUG] Creating embeddings...")
    try:
        embeddings = OpenAIEmbeddings()
        print("[DEBUG] Embeddings initialized")
    except Exception as e:
        print(f"[ERROR] Embeddings init failed: {e}")
        raise

    print("[DEBUG] Creating vector store...")
    try:
        print("[DEBUG] Preview of page[0]:", pages[0].page_content[:1000])
        vectorstore = Chroma.from_documents(pages, embedding=embeddings)
        print("[DEBUG] Vector store created.")
    except Exception as e:
        print(f"[ERROR] Vector store creation failed: {e}")
        import traceback
        traceback.print_exc()
        raise

    print("[DEBUG] Creating retriever and QA chain...")
    try:
        retriever = vectorstore.as_retriever()
        qa_chain = RetrievalQA.from_chain_type(
            llm=ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0),
            retriever=retriever
        )
        print("[DEBUG] QA chain constructed.")
        return qa_chain
    except Exception as e:
        print(f"[ERROR] Failed to construct QA chain: {e}")
        raise
