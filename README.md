# 💚 MedAgent AI - Preventive Healthcare Assistant

**MedAgent AI** is a preventive healthcare monitoring system that allows users to input lifestyle and medical information, compresses it using the **ScaleDown API** to optimize AI processing costs, calculates a basic **risk score**, and provides simple **preventive recommendations**.

---

## Features

- User-friendly **Streamlit frontend** for entering health data.
- **Health information compression** via [ScaleDown API](https://scaledown.ai/).
- Computes a **basic risk score** based on user input.
- Displays **preventive recommendations** according to lifestyle symptoms.
- Shows **compression statistics**: tokens saved, API latency, and compression ratio.

---

## Setup Instructions

1. **Clone the repository**
git clone <your-repo-url>
cd MedAi

2. Create and activate a virtual environment

# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python -m venv venv
source venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Create a .env file in the project root with your ScaleDown API key:

SCALEDOWN_API_KEY=your_api_key_here

5. Run the Streamlit app

streamlit run frontend/app.py

6. Open your browser at http://localhost:8501 to use the app.

-----------------------------------------------------------------------------------------------------------

**How It Works**

1. Users enter age, sleep hours, stress level, fatigue, and medical history.

2. Backend sends this input to ScaleDown API to compress the text for AI optimization.

3. Streamlit displays:
      
      Original input
      
      Compressed input
      
      Basic risk score
      
      Preventive recommendations
      
      Compression stats (ratio, latency, tokens used)

*Notes*

Current version does not generate AI recommendations dynamically.

Future updates can integrate LLM-based AI suggestions using Hugging Face models.

**Dependencies**
Python 3.10+
Streamlit
python-dotenv
requests
sentence-transformers

***License***

MIT License © 2026 Aditi Shukla
