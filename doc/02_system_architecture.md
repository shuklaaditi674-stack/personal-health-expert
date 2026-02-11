# System Architecture

MedAgent AI follows a microservice-based architecture separating user interface, application logic, and artificial intelligence processing.

## Components

### 1. Frontend (Presentation Layer)

Technology: HTML, CSS, JavaScript
Purpose: Collect user health data and display results.

### 2. Java Backend (Application Layer)

Technology: Spring Boot
Responsibilities:

* API management
* Input validation
* Request routing
* Communication with AI engine

### 3. AI Engine (Intelligence Layer)

Technology: Python FastAPI
Responsibilities:

* Medical history compression
* Risk score calculation
* Recommendation generation

### 4. Language Model (Reasoning Layer)

The AI engine interacts with a language model API to produce human-readable personalized recommendations.

## Architecture Flow

User Interface → Java Backend → Python AI Engine → Language Model → Analysis → Backend → User Dashboard

## Benefits of this Architecture

* Scalable
* Maintainable
* Cost-efficient
* Independent deployment of services
