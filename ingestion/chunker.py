from langchain_text_splitters import RecursiveCharacterTextSplitter

#Prose (PDF, DOCX, TXT)
#RecursiveCharacterTextSplitter. Size 512 tokens, overlap 64. Overlap ensures a sentence split at a boundary keeps its context in the next chunk.


PROSE_SPLITTER = RecursiveCharacterTextSplitter(
    chunk_size=512,
    chunk_overlap=64,
    separators=["\n\n", "\n", " ", ""]
)


OCR_SPLITTER = RecursiveCharacterTextSplitter(
    chunk_size=256,
    chunk_overlap=32
)


def chunk_text (text:str, file_type:str) -> list[str]:
    """Chunk the text based on the file type."""
    if file_type in ["csv","json"]:
        return [text] # for structured data, we can keep it as one chunk and let the model handle it
    elif file_type in ["pdf", "docx", "txt"]:
        return PROSE_SPLITTER.split_text(text)
    elif file_type in ["image"]:
        return OCR_SPLITTER.split_text(text)
    
    else:
        raise ValueError(f"Unsupported file type: {file_type}")