import os
import win32com.client


class ExcelTool:

    def __init__(self, output_dir="output"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def import_csv_to_excel(self, csv_path):

        excel = None
        workbook = None

        try:
            excel = win32com.client.Dispatch("Excel.Application")
            excel.Visible = True
            excel.DisplayAlerts = False

            workbook = excel.Workbooks.Open(os.path.abspath(csv_path))

            xlsx_path = os.path.abspath(
                os.path.join(self.output_dir, "employees.xlsx")
            )

            workbook.SaveAs(
                xlsx_path,
                FileFormat=51  # Excel Workbook (.xlsx)
            )

            workbook.Close(SaveChanges=True)
            excel.Quit()

            return {
                "success": True,
                "xlsx_path": xlsx_path
            }

        except Exception as e:

            if workbook:
                workbook.Close(False)

            if excel:
                excel.Quit()

            return {
                "success": False,
                "error": str(e)
            }