import requests

def generate_answer(query, context):
    try:
        API_KEY = "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"   



        prompt = f"""
You are a strict document extraction system.

RULES:
- ONLY use the given context
- DO NOT add external knowledge
- DO NOT summarize
- RETURN full detailed answer
- Include ALL relevant points
- Keep exact technical wording

If answer not found → say: "Not found in document"

Context:
{context}

Question:
{query}

Answer:
"""

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json",
                "HTTP-Referer": "http://localhost",
                "X-Title": "Local RAG App"
            },
            json={
                "model": "meta-llama/llama-3-8b-instruct",
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0
            }
        )

        data = response.json()

        if "choices" not in data:
            return f"LLM ERROR: {data}"

        return data["choices"][0]["message"]["content"]

    except Exception as e:
        return f"LLM ERROR: {str(e)}"