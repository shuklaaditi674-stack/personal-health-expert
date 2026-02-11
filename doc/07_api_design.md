# API Design

## Backend Endpoint

POST /analyze-health

### Request JSON

{
"name": "Aditi",
"age": 20,
"weight": 55,
"sleep_hours": 5,
"exercise": "low",
"stress": "high",
"medical_history": "anemia in 2022",
"symptoms": "fatigue, headache"
}

### Response JSON

{
"risk_score": 62,
"summary": "User shows fatigue and insufficient sleep pattern.",
"recommendations": "Increase sleep to 7–8 hours and improve hydration.",
"diet_tips": "Include iron-rich foods and fruits.",
"lifestyle_changes": "Light daily exercise and stress management."
}

## AI Engine Endpoint

POST /ai/analyze

Used internally by the backend service.
