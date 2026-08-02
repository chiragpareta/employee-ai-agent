from tools.csv_tool import CSVTool
from tools.excel_tool import ExcelTool
from tools.sheets_tool import GoogleSheetsTool

csv_tool = CSVTool()
excel_tool = ExcelTool()
sheet_tool = GoogleSheetsTool()

def generate_csv():
    return csv_tool.generate_employee_csv(20)

def import_excel(csv_path):
    return excel_tool.import_csv_to_excel(csv_path)

def upload_google_sheet(csv_path):
    return sheet_tool.upload_csv(csv_path)