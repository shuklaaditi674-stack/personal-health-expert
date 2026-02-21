# 💚 MedAgent AI - Preventive Healthcare Assistant

MedAgent AI is a **preventive healthcare monitoring system**.  
It allows users to input lifestyle and medical information, **compresses it using ScaleDown API** to optimize AI token usage, calculates a basic **risk score**, and provides simple **preventive recommendations**.

---

## Features

- User-friendly **Streamlit frontend** for entering health data.
- **Health information compression** using [ScaleDown API](https://scaledown.ai/).
- Calculates a **basic risk score** based on user input.
- Displays **preventive recommendations** based on lifestyle symptoms.
- Shows **compression statistics**: tokens saved, API latency, compression ratio.

---

## Folder Structure


MedAi/
│
├── frontend/
│ └── app.py # Streamlit frontend application
│
├── backend/
│ └── rag_backend.py # Health data compression backend
│
├── docs/
│ ├── frontend_app.md # Documentation for frontend app
│ └── backend_rag_backend.md # Documentation for backend
│
├── .env # Environment variables (API key)
├── requirements.txt # Python dependencies
└── README.md # This file


---

## Setup Instructions

1. **Clone the repository**

git clone <your-repo-url>
cd MedAi

Create and activate a virtual environment

python -m venv venv
# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate

Install dependencies

pip install -r requirements.txt

Create a .env file in the project root and add your ScaleDown API key:

SCALEDOWN_API_KEY=your_api_key_here

Run the Streamlit app

streamlit run frontend/app.py

Open your browser at http://localhost:8501
 to use the app.

How It Works

User enters age, sleep hours, stress, fatigue, and medical history.

Backend sends this input to ScaleDown API to compress the text.

Streamlit displays:

Original input

Compressed input

Basic risk score

Preventive recommendations

Compression stats (ratio, latency)

Notes

Current version does not generate AI recommendations dynamically.

Future updates can integrate LLM-based AI suggestions using Hugging Face models.

Dependencies

Python 3.10+

Streamlit

python-dotenv

requests

sentence-transformers
