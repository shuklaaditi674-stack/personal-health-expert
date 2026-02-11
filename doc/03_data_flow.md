# Data Flow

## Step 1: User Input

The user fills a health form containing lifestyle and medical information.

## Step 2: Frontend to Backend

The frontend sends a POST request in JSON format to the backend API endpoint:

/analyze-health

## Step 3: Backend Processing

The backend validates the data and forwards it to the AI engine.

## Step 4: AI Engine Processing

The AI engine:

1. Compresses medical history
2. Calculates risk score
3. Generates recommendations

## Step 5: AI Response

The AI engine returns structured output including:

* health summary
* risk score
* suggestions

## Step 6: Backend Response

The backend sends formatted results to the frontend dashboard.

## Step 7: User Output

The dashboard displays personalized recommendations to the user.
