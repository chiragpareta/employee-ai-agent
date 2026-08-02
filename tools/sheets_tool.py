import gspread
import pandas as pd
from google.oauth2.service_account import Credentials


class GoogleSheetsTool:

    def __init__(self, credentials_path="credentials.json"):

        scopes = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive",
        ]

        creds = Credentials.from_service_account_file(
            credentials_path,
            scopes=scopes,
        )

        self.client = gspread.authorize(creds)

    def upload_csv(self, csv_path):

        try:

            SHEET_ID = "1aLVsbWwPDD5T4GQaWu9upCnA-I63GJCkRV067Hv4hk4"

            spreadsheet = self.client.open_by_key(SHEET_ID)

            worksheet = spreadsheet.sheet1

            df = pd.read_csv(csv_path)

            worksheet.clear()

            worksheet.update(
                [df.columns.values.tolist()] + df.values.tolist()
            )

            return {
                "success": True,
                "sheet_url": spreadsheet.url,
            }

        except Exception as e:
            import traceback

            traceback.print_exc()

            return {
                "success": False,
                "error": repr(e)
    }