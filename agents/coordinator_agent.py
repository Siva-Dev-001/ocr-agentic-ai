from agents.ocr_agent import OCRAgent
from agents.extraction_agent import ExtractionAgent
from agents.summary_agent import SummaryAgent


class CoordinatorAgent:

    def __init__(self):

        self.ocr_agent = OCRAgent()

        self.extraction_agent = ExtractionAgent()

        self.summary_agent = SummaryAgent()

    def execute(self, file_path):

        text = self.ocr_agent.run(file_path)

        extracted = self.extraction_agent.run(text)

        summary = self.summary_agent.run(text)

        return {
            "extracted": extracted,
            "summary": summary
        }