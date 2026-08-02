import json
from openai import OpenAI

from agent.tools import (
    generate_csv,
    import_excel,
    upload_google_sheet,
)

client = OpenAI()

TOOLS = [
    {
        "type": "function",
        "name": "generate_csv",
        "description": "Generate an employee CSV file.",
        "parameters": {
            "type": "object",
            "properties": {}
        }
    },
    {
        "type": "function",
        "name": "import_excel",
        "description": "Import a CSV file into Microsoft Excel.",
        "parameters": {
            "type": "object",
            "properties": {
                "csv_path": {
                    "type": "string"
                }
            },
            "required": ["csv_path"]
        }
    },
    {
        "type": "function",
        "name": "upload_google_sheet",
        "description": "Upload a CSV file to Google Sheets.",
        "parameters": {
            "type": "object",
            "properties": {
                "csv_path": {
                    "type": "string"
                }
            },
            "required": ["csv_path"]
        }
    }
]


class EmployeeAgent:

    def run(self, prompt):

        messages = [
            {
                "role": "user",
                "content": prompt
            }
        ]

        csv_path = None

        while True:

            response = client.responses.create(
                model="gpt-4.1",
                input=messages,
                tools=TOOLS,
            )

            item = response.output[0]

            if item.type == "message":
                print(item.content[0].text)
                break

            name = item.name
            args = json.loads(item.arguments)

            if name == "generate_csv":
                csv_path = generate_csv()
                result = csv_path

            elif name == "import_excel":
                result = import_excel(csv_path)

            elif name == "upload_google_sheet":
                result = upload_google_sheet(csv_path)

            messages.append(item)

            messages.append(
                {
                    "type": "function_call_output",
                    "call_id": item.call_id,
                    "output": json.dumps(result)
                }
            )