import json
from dotenv import load_dotenv
from openai import OpenAI

from tools.csv_tool import CSVTool
from tools.excel_tool import ExcelTool
from tools.sheets_tool import GoogleSheetsTool

load_dotenv()

# -----------------------------
# Initialize OpenAI
# -----------------------------

client = OpenAI()

# -----------------------------
# Initialize Tools
# -----------------------------

csv_tool = CSVTool()
excel_tool = ExcelTool()
sheet_tool = GoogleSheetsTool()

# -----------------------------
# Available Workflows
# -----------------------------

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "employee_workflow",
            "description": "Generate employee CSV, import into Excel, then upload the same data into Google Sheets.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    }
]

# -----------------------------
# User Prompt
# -----------------------------

prompt = input("\nEnter your request:\n\n> ")

# -----------------------------
# Ask OpenAI what to do
# -----------------------------

response = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {
            "role": "system",
            "content": """
You are an autonomous AI assistant.

If the user asks to:

- create employee csv
- generate employee data
- import into excel
- upload to google sheets

then call employee_workflow.

Otherwise answer normally.
"""
        },
        {
            "role": "user",
            "content": prompt
        }
    ],
    tools=TOOLS,
    tool_choice="auto"
)

message = response.choices[0].message

# -----------------------------
# Execute Workflow
# -----------------------------

if message.tool_calls:

    print("\nAI selected workflow:")
    print(message.tool_calls[0].function.name)

    print("\nGenerating CSV...")
    csv_path = csv_tool.generate_employee_csv(20)

    print("CSV:", csv_path)

    print("\nImporting into Excel...")
    excel_result = excel_tool.import_csv_to_excel(csv_path)

    print(excel_result)

    print("\nUploading to Google Sheets...")
    sheet_result = sheet_tool.upload_csv(csv_path)

    print(sheet_result)

    final_report = f"""
Workflow Completed

CSV:
{csv_path}

Excel:
{excel_result}

Google Sheets:
{sheet_result}
"""

    # Send tool result back to the model
    final = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {
                "role": "system",
                "content": "Summarize the completed workflow."
            },
            {
                "role": "user",
                "content": prompt
            },
            message,
            {
                "role": "tool",
                "tool_call_id": message.tool_calls[0].id,
                "content": final_report
            }
        ]
    )

    print("\n" + "=" * 60)
    print("FINAL RESPONSE")
    print("=" * 60)
    print(final.choices[0].message.content)

else:

    print("\n")
    print(message.content)