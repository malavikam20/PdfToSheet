import os
from openai import OpenAI
from dotenv import load_dotenv
from openai._exceptions import RateLimitError


# Load .env
load_dotenv()

# Initialize client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def gpt_map_key(pdf_key, schema):
    prompt = f"""
PDF key: "{pdf_key}"

Google Sheet schema options:
{', '.join(schema)}

Respond with only the best matching schema term (case-sensitive).
"""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        return response.choices[0].message.content.strip()
    except RateLimitError:
        print(f"[⚠️ MOCK] Mapping '{pdf_key}' → using fallback due to quota issue.")
        return schema[0] if schema else "Unknown"

def map_keys_to_sheet_schema(extracted_data, sheet_schema):
    mapped = {}
    for key in extracted_data:
        best_match = gpt_map_key(key, sheet_schema)
        if best_match:  # Only add if a valid match is returned
            mapped[best_match] = extracted_data[key]
    return mapped