import requests

API_URL = "https://api.groq.com/v1/completions"
API_KEY = "your_api_key_here"

def ml_suggest(code_snippet):
    try:
        headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
        data = {
            "model": "mixtral-8x7b-32768",
            "prompt": code_snippet,
            "max_tokens": 10
        }
        response = requests.post(API_URL, json=data, headers=headers)

        if response.status_code == 200:
            return response.json().get("choices", [{}])[0].get("text", "").strip()
        return f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"ML Suggestion Failed: {str(e)}"
