from app.extractor import extract_key_value_pairs
from app.mapper import map_keys_to_sheet_schema
from app.sheets_api import read_sheet_data, write_to_sheet

def get_sheet_schema(sheet_id, range_name):
    values = read_sheet_data(sheet_id, range_name)
    return [row[0].strip().lower() for row in values if row]

def fill_sheet_from_pdf(pdf_path, sheet_id, schema_range, value_range):
    extracted_data = extract_key_value_pairs(pdf_path)
    schema = get_sheet_schema(sheet_id, schema_range)
    mapped = map_keys_to_sheet_schema(extracted_data, schema)

    sheet_rows = [[key.capitalize(), value] for key, value in mapped.items()]
    write_to_sheet(sheet_id, value_range, sheet_rows)
    print("Sheet successfully updated.")
