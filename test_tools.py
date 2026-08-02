from agent.tools import generate_csv, import_excel, upload_google_sheet

csv = generate_csv()

print(csv)

excel = import_excel(csv["csv_path"])

print(excel)

sheet = upload_google_sheet(csv["csv_path"])

print(sheet)