# 💚 MedAgent AI - Frontend Documentation

## Overview

The frontend is built using **Streamlit**, providing a **user-friendly interface** for entering health information.

---

## User Input Form

- **Age:** Number input (1-120)
- **Average Sleep Hours:** Slider (0-12)
- **Stress Level:** Slider (0-10)
- **Fatigue Level:** Slider (0-10)
- **Medical History / Symptoms:** Multi-line text area

**Form Submission:**  
User clicks "Analyze My Health" → sends data to backend for processing.

---

## Output Display

1. **Original Input:** Displays the raw information entered by the user.
2. **Compressed Input:** Shows the optimized version of the input returned by ScaleDown API.
3. **Risk Score:** Calculates a numeric score based on keywords (`stress`, `fatigue`, `dehydration`, `sleep`, `pain`).
4. **Preventive Recommendations:** Simple suggestions based on detected keywords.
5. **Compression Stats:** Shows metrics like compression ratio, latency, and tokens saved.

---

## Implementation Details

- **Dynamic Backend Import:** Uses `importlib.util` to dynamically load the `RAGBackend`.
- **Form Handling:** Streamlit `form` ensures proper submission workflow.
- **Data Flow:**
  1. User input → Backend compression
  2. Backend returns compressed text and metadata
  3. Frontend calculates risk score and shows recommendations
