from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
openai_api_base = os.getenv("OPENAI_API_BASE")

output_dir = os.getenv("OUTPUT_DIR", "output")

OUTPUT_DIR = "output"
LOG_DIR = "logs"