import pymupdf
from ingestion.raw_data import RawData
from ingestion.utils.metadata import normalize_datetime

def parse_pdf(file: str) -> RawData:
    """Parse a PDF file and return its text content and metadata."""
    doc = pymupdf.open(file)
    text = ""
    for page in doc:
        text += page.get_text()
    metadata = {
        "title": doc.metadata.get("title", ""),
        "author": doc.metadata.get("author", ""),
        "creation_date": normalize_datetime(doc.metadata.get("creationDate", "")),
        "modification_date": normalize_datetime(doc.metadata.get("modDate", "")),
        "number_of_pages": len(doc),
    }

    #get images from pdf later

    return RawData(text=text, metadata=metadata)