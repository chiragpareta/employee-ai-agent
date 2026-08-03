import win32com.client
import os

from tools.csv_tool import CSV_PATH

def import_excel():

    excel = win32com.client.Dispatch("Excel.Application")

    wb = excel.Workbooks.Open(os.path.abspath(CSV_PATH))

    wb.SaveAs(
        os.path.abspath("output/employees.xlsx"),
        FileFormat=51,
    )

    wb.Close()
    excel.Quit()

    return "Excel created successfully."