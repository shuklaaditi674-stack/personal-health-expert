# Risk Scoring Model

MedAgent AI includes a rule-based risk assessment module.

## Parameters Considered

* Sleep duration
* Physical activity
* Stress level
* Weight condition
* Medical history

## Scoring Logic

Each risk factor adds points:

Low sleep (<6h) → +20
High stress → +20
No exercise → +20
Overweight → +20
Chronic condition → +20

Maximum Score = 100

## Risk Categories

0–30 : Low Risk
31–60 : Moderate Risk
61–100 : High Risk

The risk score helps the user understand wellness condition without providing medical diagnosis.
