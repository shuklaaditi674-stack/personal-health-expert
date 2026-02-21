# backend/rag_backend.py
import os
import requests
import numpy as np
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

load_dotenv()

# Cache model loading
def get_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

class RAGBackend:
    def __init__(self):
        self.api_key = os.getenv("SCALEDOWN_API_KEY", "").strip()
        self.model = get_model()

    def compress_health_info(self, text):
        """Compress health/lifestyle info via ScaleDown API"""
        if not self.api_key:
            return {"successful": False, "error": "API Key missing in .env"}
            
        headers = {"x-api-key": self.api_key, "Content-Type": "application/json"}
        payload = {
            "context": "Compress medical history and lifestyle info for AI analysis.",
            "prompt": text,
            "model": "gpt-4o",
            "scaledown": {"rate": "auto"}
        }
        
        try:
            response = requests.post(
                "https://api.scaledown.xyz/compress/raw/", 
                json=payload, 
                headers=headers,
                timeout=30
            )

            data = response.json()
            
            # Extract main compressed text
            compressed_text = data.get("compressed_prompt") \
                              or data.get("results", {}).get("compressed_prompt") \
                              or text

            # Extract metadata safely
            model_used = data.get("model_used") or data.get("results", {}).get("model_used", "N/A")
            original_tokens = data.get("original_prompt_tokens") or data.get("results", {}).get("original_prompt_tokens", 0)
            compressed_tokens = data.get("compressed_prompt_tokens") or data.get("results", {}).get("compressed_prompt_tokens", 0)
            latency_ms = data.get("latency_ms") or 0

            return {
                "successful": True,
                "compressed_prompt": compressed_text,
                "model_used": model_used,
                "original_tokens": original_tokens,
                "compressed_tokens": compressed_tokens,
                "latency_ms": latency_ms
            }      
                        
        except Exception as e:
            return {"successful": False, "error": f"Connection failed: {str(e)}"}

    def calculate_similarity(self, doc_text, user_text):
        """Optional: Compute semantic similarity (0-100%)"""
        if not doc_text or not user_text:
            return 0.0
        v1 = self.model.encode(doc_text)
        v2 = self.model.encode(user_text)
        score = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
        return round(float(score) * 100, 1)