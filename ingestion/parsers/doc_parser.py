from unstructured.partition.docx import partition_docx
import docx
from ingestion.raw_data import RawData


def parse_doc(file: str) -> RawData:
    """Parse a DOC file and return its text content and metadata."""
    elements = partition_docx(file=file)
    text = "\n".join([el.text for el in elements if el.text])
    #improve metadata extraction later
    metadata = {
        "title": file,
        "author": "",
        "creation_date": "",
        "modification_date": "",
        "number_of_pages": len(elements),
    }
    return RawData(text=text, metadata=metadata)

#image extraction from doc later