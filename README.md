# Employee AI Agent

## Overview

Employee AI Agent is an autonomous AI application that accepts a natural language request and performs spreadsheet automation using reusable tools.

The agent can:

- Generate realistic employee data
- Create a CSV file
- Import the CSV into Microsoft Excel
- Save the workbook as an Excel file
- Upload the same data to Google Sheets
- Report the execution status of each step

---

## Features

- Natural language input
- OpenAI powered decision making
- Modular tool architecture
- CSV generation using Faker
- Microsoft Excel automation using pywin32
- Google Sheets integration using Google Sheets API
- Error handling
- Reusable tools

---

## Project Structure

```text
employee-ai-agent/

│── tools/
│   ├── csv_tool.py
│   ├── excel_tool.py
│   └── sheets_tool.py
│
│── output/
│
│── credentials.json
│── main.py
│── requirements.txt
│── .env.example
│── README.md
```

---

## Technologies Used

- Python
- OpenAI API
- LangChain
- Pandas
- Faker
- Google Sheets API
- pywin32
- python-dotenv

---

## Installation

Clone the repository

```bash
git clone <your-github-repository>
```

Move into the project

```bash
cd employee-ai-agent
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file.

```env
OPENAI_API_KEY=your_openai_api_key
```

---

## Google Sheets Setup

1. Create a Google Cloud Project

2. Enable

- Google Sheets API
- Google Drive API

3. Create a Service Account

4. Download

```
credentials.json
```

5. Place it inside the project root.

6. Share your Google Sheet with the Service Account email.

Example

```
employee-agent@your-project.iam.gserviceaccount.com
```

---

## Run

```bash
python main.py
```

---

## Example Prompt

```
Create a sample employee CSV and import it into Excel and Google Sheets.
```

---

## Workflow

```
User Prompt
      │
      ▼
OpenAI
      │
      ▼
Workflow Decision
      │
      ▼
Generate CSV
      │
      ▼
Import into Excel
      │
      ▼
Upload to Google Sheets
      │
      ▼
Execution Report
```

---

## Sample Output

```
Generating CSV...

CSV created successfully.

Importing into Excel...

Excel workbook saved.

Uploading to Google Sheets...

Upload successful.

Workflow completed successfully.
```

---

## Error Handling

The application handles:

- Invalid API Key
- Missing Google credentials
- Excel automation failures
- Google Sheets upload failures
- CSV generation errors

---

## Future Improvements

- Multi-agent workflow
- LangGraph integration
- Conversation memory
- Support for XLSX and ODS
- Retry mechanism
- Docker deployment
- Unit tests
- Structured logging

---

## Author

Your Name

AI Engineer Assessment