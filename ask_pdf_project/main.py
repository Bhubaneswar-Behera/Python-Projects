import os
from dotenv import load_dotenv
from utils.pdf_loader import load_pdf
from utils.qa_chain import create_qa_chain

def debug_log(msg):
    print(f"[DEBUG] {msg}")

# Load API key
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("❌ OPENAI_API_KEY not found in .env")

debug_log("API key loaded")

# Load PDF
pdf_path = "sample.pdf"
debug_log(f"Loading PDF: {pdf_path}")

try:
    pages = load_pdf(pdf_path)
    debug_log(f"Loaded {len(pages)} pages from PDF")
except Exception as e:
    print(f"❌ Error loading PDF: {e}")
    exit()

# Set up QA chain
debug_log("Setting up QA chain...")
try:
    qa_chain = create_qa_chain(pages)
    debug_log("QA chain ready")
except Exception as e:
    print(f"❌ Error creating QA chain: {e}")
    raise

# Start asking
print("\n📘 You can now ask questions about the PDF!")
while True:
    question = input("🧠 Ask a question (or type 'exit'): ")
    if question.lower() == "exit":
        break
    try:
        answer = qa_chain.run(question)
        print("👉 Answer:", answer)
    except Exception as e:
        print(f"❌ Error getting answer: {e}")
