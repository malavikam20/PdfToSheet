# PDF → Google Sheets AI Agent

## 🚀 Objective
Extracts financial data from PDFs and syncs to Google Sheets using an AI agent with language and schema understanding.

## ⚙️ Features
- Extracts structured data from PDFs
- Maps to correct sheet row using LangChain + embeddings
- Supports multilingual mapping (e.g., Spanish → English)
- Google Sheets API integration
- Streamlit UI for uploading PDFs and linking Sheets

## 📦 How to Run
```bash
pip install -r requirements.txt
python app/agent.py  # or
streamlit run ui/app.py
