# Employee AI Agent

## Overview

This project is an AI-powered employee automation application built using Python, LangChain, and OpenAI.

The application accepts a natural language prompt, uses an LLM to understand the request, and automatically calls the required tools to complete the task.

The current workflow can:

- Generate sample employee data
- Save the data as a CSV file
- Import the CSV into Microsoft Excel
- Upload the same data to Google Sheets

---

## Technologies

- Python
- LangChain
- OpenAI GPT-4.1
- Pandas
- Faker
- pywin32
- Google Sheets API
- gspread
- python-dotenv

---

## Project Structure

```text
employee-ai-agent/

├── tools/
│   ├── csv_tool.py
│   ├── excel_tool.py
│   ├── sheets_tool.py
│   └── agent_tools.py
│
├── output/
├── main.py
├── requirements.txt
├── README.md
├── .env.example
└── credentials.json
```

---

## How it works

The user enters a prompt.

The LangChain agent sends the request to OpenAI.

Based on the prompt, the LLM decides which tool(s) should be executed.

The available tools are:

- Generate Employee CSV
- Import CSV into Excel
- Upload CSV to Google Sheets

Finally, the agent returns the result to the user.

---

## Setup

Install the required packages.

```bash
pip install -r requirements.txt
```

Create a `.env` file.

```env
OPENAI_API_KEY=your_openai_api_key
```

Download your Google Service Account credentials and save them as:

```text
credentials.json
```

Share your Google Sheet with the service account email.

---

## Run

```bash
python main.py
```

---

## Example Prompt

```text
Create a sample employee CSV and import it into Excel and Google Sheets.
```

---

## Output

The application will:

- Generate employee data
- Create a CSV file
- Create an Excel workbook
- Upload the data to Google Sheets
- Display the final result

---

## Future Improvements

- Add more tools
- Support more spreadsheet operations
- Add conversation memory
- Build a multi-agent workflow using LangGraph

---

## Author

Chirag Pareta