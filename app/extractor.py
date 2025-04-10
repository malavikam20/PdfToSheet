from PyPDF2 import PdfReader
import re

def safe_float(value):
    try:
        return float(value.replace(',', '').strip())
    except (ValueError, AttributeError):
        print(f"Skipping non-numeric value: {value}")
        return None

def extract_key_value_pairs(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()

    pattern = re.findall(r'([A-Za-z \(\)\-&]+):?\s+([\d,.\-]+)', text)
    
    result = {}
    for key, value in pattern:
        clean_value = safe_float(value)
        if key.strip() and clean_value is not None:
            result[key.strip()] = clean_value

    return result
