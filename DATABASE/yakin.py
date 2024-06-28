import json
import openpyxl

def json_to_xlsx(json_file, xlsx_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    wb = openpyxl.Workbook()
    sheet = wb.active
    
    # Tulis header (ambil keys dari data pertama)
    if data:
        header = list(data[0].keys())
        sheet.append(header)
    
    # Tulis data
    for item in data:
        row = [item[key] for key in header]
        sheet.append(row)
    
    # Simpan workbook ke file xlsx
    wb.save(xlsx_file)

# Contoh pemakaian
json_file = 'data.json'  # Ganti dengan nama file JSON yang ada
xlsx_file = 'data.xlsx'  # Nama file XLSX yang akan dihasilkan

json_to_xlsx(json_file, xlsx_file)
