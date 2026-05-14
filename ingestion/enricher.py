import hashlib,re

from ingestion.utils import metadata

RELATIONAL_PATTERNS = re.compile(
    r'\b(reports to|manages|owned by|part of|located in|'
    r'subsidiary of|acquired by|founded by)\b',
    re.IGNORECASE
)

PROPER_NOUN_PATTERN = re.compile(r'\b[A-Z][a-zA-Z0-9&.,\- ]{2,}\b')


def enrich(chunk_text: str,metadata: dict, chunk_index: int) -> dict:

    chunk_id = hashlib.md5(f"{metadata['source']}-{metadata.get('page',0)}-{chunk_index}"
              .encode()
            ).hexdigest()[:12]
    
    proper_nouns = PROPER_NOUN_PATTERN.findall(chunk_text)
    has_relations = bool(RELATIONAL_PATTERNS.search(chunk_text))
    needs_graph = has_relations or len(set(proper_nouns)) >= 3

    return {
        "chunk_id": chunk_id,
        "text": chunk_text,
        "source": metadata["source"],
        "page": metadata.get("page", 0),
        "file_type": metadata["file_type"],
        "chunk_index": chunk_index,
        "token_count": len(chunk_text) // 4,  # rough approx
        "needs_graph": needs_graph,
    }


