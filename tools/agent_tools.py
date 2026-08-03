from langchain.tools import tool

from tools.csv_tool import generate_csv
from tools.excel_tool import import_excel
from tools.sheets_tool import upload_google_sheet

@tool
def generate_employee_csv():
    """Generate employee CSV."""
    return generate_csv()

@tool
def create_excel():
    """Import CSV into Excel."""
    return import_excel()

@tool
def upload_sheet():
    """Upload CSV to Google Sheets."""
    return upload_google_sheet()

TOOLS = [
    generate_employee_csv,
    create_excel,
    upload_sheet,
]