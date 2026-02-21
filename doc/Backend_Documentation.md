# 💚 MedAgent AI - Backend Documentation

## Overview

The backend (`RAGBackend`) handles:

- **Compression of user input** using the ScaleDown API
- Optional **semantic similarity** calculations
- Returns compressed text, compression ratio, and API latency to frontend

---

## Core Components

### Initialization
- Loads the **ScaleDown API key** from `.env`
- Loads **sentence-transformers model** for future similarity scoring

### Methods

1. **compress_health_info(text)**
   - Sends input to ScaleDown API
   - Returns:
     - `compressed_prompt` → optimized text
     - `compression_ratio` → percentage of tokens saved
     - `latency_ms` → API response time

2. **calculate_similarity(doc_text, user_text)** (Optional)
   - Computes semantic similarity (0-100%) between any document and user input
   - Uses **SentenceTransformers embeddings** (`all-MiniLM-L6-v2`)

---

## Error Handling

- Missing API key → returns `{"successful": False, "error": "API Key missing in .env"}`
- Connection errors → returns descriptive error messages
- No content from API → fallback to original user input
