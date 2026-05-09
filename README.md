# PolyRAG

> Compare, benchmark, and deploy three RAG strategies — Standard, Agentic, and Graph — on your own documents. 

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square)
![LLM](https://img.shields.io/badge/LLM-Gemini%201.5%20Flash-orange?style=flat-square)
![Vector DB](https://img.shields.io/badge/VectorDB-ChromaDB-purple?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## What is PolyRAG?

PolyRAG is a hybrid RAG (Retrieval-Augmented Generation) system designed to handle diverse file formats and query complexities. It dynamically routes user queries through three distinct pipelines—Standard, Agentic, or Graph-based—ensuring the most accurate and context-aware response possible.

Upload a PDF, CSV, image, or any mix of files. Ask a question. PolyRAG either recommends the best RAG strategy for your query or lets you pick one manually — then returns the answer with sources, latency, and a plain-English explanation of what the retriever did.

---

## The three strategies

| Strategy | When to use | How it works |
|---|---|---|
| **Standard RAG** | Simple Q&A, single documents | Chunk → Embed → Hybrid (Dense + Sparse) search with Reranking for direct facts→ Generate |
| **Agentic RAG** | Multi-doc queries, reasoning needed | LLM decides when/how to retrieve, can multi-hop |
| **Graph RAG** | Relational data, entity-heavy content | Extracts entities, builds a knowledge graph, traverses it |

All three use the same LLM (Gemini 1.5 Flash) and the same embedding model (Google `text-embedding-004`). Only the retrieval strategy changes.

---

## Features

- **Multi-format ingestion** — PDF, DOCX, CSV, TXT, JSON, PNG/JPG (OCR via Tesseract)
- **Auto-recommender** — heuristic engine suggests the best RAG strategy based on your files and query
- **Transparent responses** — every answer shows which RAG was used, why, and what sources were cited

---

## License

MIT — use it, fork it, build on it.

---

*Built to understand RAG deeply, not just use it.*
