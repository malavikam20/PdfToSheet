import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from app.agent import fill_sheet_from_pdf

st.title("PDF to Google Sheet AI Agent")

pdf_file = st.file_uploader("Upload PDF", type="pdf")
sheet_id = st.text_input("Enter Google Sheet ID")
schema_range = st.text_input("Enter schema range (e.g., Sheet1!A2:A20)", "Sheet1!A2:A20")
value_range = st.text_input("Enter target value range (e.g., Sheet1!A2:B20)", "Sheet1!A2:B20")

if st.button("Submit and Process") and pdf_file:
    with open("temp.pdf", "wb") as f:
        f.write(pdf_file.read())
    fill_sheet_from_pdf("temp.pdf", sheet_id, schema_range, value_range)
    st.success("Google Sheet updated!")
