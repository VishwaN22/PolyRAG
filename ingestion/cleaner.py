from ingestion.raw_data import RawData
import ftfy, re


def clean( data: RawData) -> RawData:
    """Clean the raw data by removing extra whitespace and normalizing text."""
    cleaned_text = ftfy.fix_text(data.text)
    cleaned_text = re.sub(r'\n{3,}', '\n\n', cleaned_text)  # collapse blank lines
    cleaned_text = re.sub(r'[ \t]{2,}', ' ', cleaned_text)  # collapse extra whitespace
    cleaned_text = cleaned_text.strip() # remove leading and trailing whitespace

    if(data.metadata.get("file_type") == "pdf"):
        cleaned_text = strip_headers_footers(cleaned_text)
    
    
    return RawData(text=cleaned_text, metadata=data.metadata)


def strip_headers_footers(text: str) -> str:
    """Strip headers and footers from the text."""
    lines = text.splitlines()
    # Simple heuristic: remove lines that are too short or contain certain keywords
     # lines appearing 3+ times are likely headers/footers
    from collections import Counter
    freq = Counter(l.strip() for l in lines if l.strip())
    boilerplate = {l for l, c in freq.items() if c >= 3}
    return "\n".join(l for l in lines if l.strip() not in boilerplate)