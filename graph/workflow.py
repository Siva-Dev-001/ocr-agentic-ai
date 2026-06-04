from langgraph.graph import StateGraph

from agents.ocr_agent import OCRAgent
from agents.extraction_agent import ExtractionAgent
from agents.summary_agent import SummaryAgent

workflow = StateGraph(dict)

workflow.add_node(
    "ocr",
    OCRAgent().run
)

workflow.add_node(
    "extract",
    ExtractionAgent().run
)

workflow.add_node(
    "summary",
    SummaryAgent().run
)

workflow.add_edge(
    "ocr",
    "extract"
)

workflow.add_edge(
    "extract",
    "summary"
)

workflow.set_entry_point(
    "ocr"
)

graph = workflow.compile()