from typing import TypedDict


class AgentState(TypedDict):

    file_path: str

    text: str

    extracted_data: dict

    summary: str