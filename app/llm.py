import requests

def generate_answer(query, context):
    try:
        API_KEY = "********************************************************************"   

        prompt = f"""
Answer the question based ONLY on the context.

Context:
{context}

Question:
{query}
"""

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": "meta-llama/llama-3-8b-instruct",
                "messages": [
                    {"role": "user", "content": prompt}
                ]
            }
        )

        data = response.json()

        if "choices" not in data:
            return f"LLM ERROR: {data}"

        return data["choices"][0]["message"]["content"]

    except Exception as e:
        return f"LLM ERROR: {str(e)}"