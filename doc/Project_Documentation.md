```markdown
# 💚 MedAgent AI - Project Documentation

## Overview

MedAgent AI is a preventive healthcare assistant designed to **help users track and optimize their lifestyle habits**. Users provide personal and health data, which is compressed using the **ScaleDown API** to reduce AI processing cost. The system calculates a basic **risk score** and provides preventive recommendations based on the input.

---

## Frontend (Streamlit)

- **Purpose:** Provides an interface for users to input health data.
- **Inputs:**
  - Age
  - Average Sleep Hours
  - Stress Level
  - Fatigue Level
  - Medical History / Symptoms
- **Outputs:**
  - Original user input
  - Compressed input optimized for AI
  - Risk score
  - Preventive recommendations
  - Compression statistics

- **Implementation Notes:**
  - The frontend dynamically loads the backend module.
  - Form submission triggers the compression process.
  - Risk score is calculated based on keywords like "stress", "fatigue", and "dehydration".
  - Recommendations are generated according to detected keywords.

---

## Backend (RAGBackend)

- **Purpose:** Handles **compression of health and lifestyle data** via ScaleDown API and provides optional semantic similarity calculations.
- **Key Components:**
  1. **Initialization**
     - Loads **ScaleDown API key** from `.env`.
     - Loads a **sentence-transformers model** for future similarity scoring.
  2. **Compression (`compress_health_info`)**
     - Sends user input to ScaleDown API.
     - Returns:
       - `compressed_prompt` → optimized text
       - `compression_ratio` → effectiveness of compression
       - `latency_ms` → API response time
  3. **Optional similarity (`calculate_similarity`)**
     - Computes semantic similarity (0-100%) between documents and user input.
  
- **Notes:**
  - Currently, AI-generated recommendations are **not included**.
  - Future upgrades can integrate **LLM-based preventive tips**.

---

## Technology Stack

- **Python 3.10+**
- **Streamlit** for frontend
- **requests** for API calls
- **python-dotenv** for environment variables
- **sentence-transformers** for optional semantic similarity

---

## How It Works

1. User submits health and lifestyle information via frontend.
2. Backend compresses the input using ScaleDown API.
3. Compressed data is returned along with metadata (compression ratio, latency).
4. Frontend calculates a basic risk score and displays preventive recommendations.
5. User sees:
   - Original input
   - Compressed input
   - Risk score
   - Recommendations
   - Compression stats

---

## Future Enhancements

- **AI-generated preventive recommendations** based on compressed input.
- Advanced **risk scoring algorithms**.
- Integration with **personal health dashboards**.
- Optional **LLM-based lifestyle analysis**.

---
