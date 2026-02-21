```markdown
# 💚 MedAgent AI - Project Architecture

## Components

1. **Frontend (Streamlit)**
   - User input
   - Display results
   - Dynamic backend import

2. **Backend (RAGBackend)**
   - Compression API integration
   - Optional similarity computation
   - Returns results to frontend

3. **ScaleDown API**
   - Compresses prompts
   - Returns optimized text and metadata

---

## Data Flow


User Input → Backend (RAGBackend) → ScaleDown API → Backend returns compressed data → Frontend displays results


---

## Risk Scoring

- Keyword-based risk calculation
- Keywords: `fatigue`, `stress`, `dehydration`, `sleep`, `pain`
- Score shown in frontend
