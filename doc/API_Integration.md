# 💚 MedAgent AI - ScaleDown API Integration

## Overview

The project uses **ScaleDown API** to compress user health information. This reduces **token usage** for AI models, optimizing costs for potential future AI analysis.

---

## Endpoint


POST https://api.scaledown.xyz/compress/raw/


### Headers
{
  "x-api-key": "YOUR_API_KEY",
  "Content-Type": "application/json"
}
Payload Example
{
  "context": "Compress medical history and lifestyle info for AI analysis.",
  "prompt": "User health input here...",
  "model": "gpt-4o",
  "scaledown": {
    "rate": "auto"
  }
}
Response Structure
{
  "compressed_prompt": "Optimized text...",
  "model_used": "gpt-4o",
  "original_prompt_tokens": 150,
  "compressed_prompt_tokens": 65,
  "successful": true,
  "latency_ms": 2341,
  "request_metadata": {
    "compression_time_ms": 2341,
    "compression_rate": "auto"
  }
}


Usage in Project

Frontend sends user input → backend

Backend calls ScaleDown API

API returns compressed prompt → frontend displays compressed text and stats
