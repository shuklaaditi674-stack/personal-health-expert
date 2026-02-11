# MedAgent AI — Smart Health Monitoring & Recommendation Agent

## Overview

MedAgent AI is an AI-powered preventive healthcare monitoring system that analyzes lifestyle and medical history data to generate personalized wellness recommendations while minimizing AI processing cost.

The system compresses medical information before sending it to a language model, enabling scalable and cost-efficient health guidance.

---

## Problem

Most people ignore early health indicators such as poor sleep, stress, and fatigue. Existing digital health tools provide generic advice and do not intelligently interpret medical history. Additionally, AI-based systems are expensive to scale due to high computational cost.

---

## Solution

MedAgent AI acts as a personal wellness assistant that:

* analyzes user health data
* summarizes medical history
* calculates risk score
* generates personalized recommendations
* reduces AI computation cost

---

## Key Features

* Personalized health recommendations
* Medical history compression
* Risk score analysis
* Cost-optimized AI processing
* Microservice architecture
* Preventive healthcare approach

---

## Technology Stack

Frontend:

* HTML
* CSS
* JavaScript

Backend:

* Java Spring Boot

AI Engine:

* Python FastAPI

AI Model:

* Large Language Model API

Database:

* SQLite / MySQL

---

## System Architecture

Frontend → Java Backend → Python AI Engine → Language Model → Response Dashboard

---

## How to Run

### 1. Start AI Engine

```
cd ai-engine
pip install -r requirements.txt
uvicorn main:app --reload
```

### 2. Start Backend

```
cd backend-java
mvn spring-boot:run
```

### 3. Open Frontend

Open index.html in browser.

---

## Project Structure

frontend/ → User interface
backend-java/ → API server
ai-engine/ → AI processing
docs/ → technical documentation
dataset/ → sample data

---

## Ethics Notice

This project is a wellness recommendation system and not a medical diagnostic tool. Users must consult a qualified healthcare professional for medical advice.

---

## Future Scope

* Wearable integration
* Mobile application
* Multilingual support
* Real-time monitoring

---

## Author

Aditi Shukla
Intel Unnati AI Program Project
