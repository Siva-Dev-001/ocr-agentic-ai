from services.ocr_service import extract_text


class OCRAgent:

    def run(self, file_path):

        return extract_text(file_path)