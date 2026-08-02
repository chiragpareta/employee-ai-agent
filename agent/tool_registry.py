from agent.tools import (
    generate_csv,
    import_excel,
    upload_google_sheet,
)


class ToolRegistry:

    def __init__(self):
        self.csv_path = None

    def execute(self, tool_name, arguments):

        if tool_name == "generate_csv":

            self.csv_path = generate_csv()

            return {
                "success": True,
                "csv_path": self.csv_path
            }

        elif tool_name == "import_excel":

            return import_excel(self.csv_path)

        elif tool_name == "upload_google_sheet":

            return upload_google_sheet(self.csv_path)

        else:

            return {
                "success": False,
                "error": f"Unknown tool: {tool_name}"
            }