from typing import TypedDict, List


class AgentState(TypedDict):
    user_request: str
    messages: List
    csv_path: str
    excel_path: str
    sheet_url: str
    status: List[str]