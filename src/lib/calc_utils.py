# Add basic utilities for interacting with Calc sheets.

def create_new_sheet(doc, name):
    sheets = doc.Sheets
    if not sheets.hasByName(name):
        sheets.insertNewByName(name, len(sheets))
    return sheets.getByName(name)