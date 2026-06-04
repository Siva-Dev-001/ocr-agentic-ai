from agents.ocr_agent import OCRAgent
from agents.extraction_agent import ExtractionAgent
from agents.summary_agent import SummaryAgent


class DocumentService:

    def __init__(self):
        self.ocr = OCRAgent()
        self.extractor = ExtractionAgent()
        self.summarizer = SummaryAgent()

    def process_document(self, file_path):

        text = self.ocr.run(file_path)

        extracted_data = self.extractor.run(text)

        summary = self.summarizer.run(text)

        return {
            "text": text,
            "extracted_data": extracted_data,
            "summary": summary
        }