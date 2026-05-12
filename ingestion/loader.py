from .parsers import parse_pdf, parse_doc, parse_image, parse_csv
from pathlib import Path

FILE_TYPES = {
    "pdf": "pdf",
    "docx": "docx",
    "txt": "text",
    "csv": "csv",
    "json": "json",
    "png": "image",
    "jpg": "image",
    "jpeg": "image",
}
PARSERS = {
    "pdf": parse_pdf,
    "docx": parse_doc,
    # "text": parse_text,
    "csv": parse_csv,
    # "json": parse_json,
    "image": parse_image,
}

def detect_file_type(ext: str) -> str:
    return FILE_TYPES.get(ext.lower(), "unknown")


def parse_file(file):       
    ext = detect_file_type(Path(file.name).suffix.lower().lstrip("."))

    parser = PARSERS.get(ext)
    print("here", ext, parser)
    if parser:
        return parser(file)
    else:
        raise ValueError(f"Unsupported file type: {ext}")
    
    