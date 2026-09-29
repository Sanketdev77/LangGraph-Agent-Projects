#state.py usually contains the shared state/data structure that stores information 
# passed between different agents or nodes in a LangGraph workflow

from typing_extensions import TypedDict

class AgentState(TypedDict):
    requirement: str
    generated_code: str
    review_feedback: str
    qa_feedback: str
    final_report: str
    needs_fix: bool
    iteration_count: int


