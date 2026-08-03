import pandas as pd
import gspread

from google.oauth2.service_account import Credentials
from tools.csv_tool import CSV_PATH

SHEET_ID = "1aLVsbWwPDD5T4GQaWu9upCnA-I63GJCkRV067Hv4hk4"

def upload_google_sheet():

    creds = Credentials.from_service_account_file(
        "credentials.json",
        scopes=[
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive",
        ],
    )

    client = gspread.authorize(creds)

    sheet = client.open_by_key(SHEET_ID).sheet1

    df = pd.read_csv(CSV_PATH)

    sheet.clear()

    sheet.update([df.columns.tolist()] + df.values.tolist())

    return "Uploaded successfully."