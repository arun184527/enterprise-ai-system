import requests
API_KEY = "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"
def generate_answer(query, context):
    prompt = f"""
    Answer the question based on the context below.

    Context:
    {context}

    Question:
    {query}

    Give a clear and concise answer.
    """

    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost",
            "X-Title": "AI Project"
        },
        json={
            "model": "openai/gpt-3.5-turbo",  # ✅ GUARANTEED WORKING
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
    )

    data = response.json()
    print("DEBUG:", data)  # keep this for now

    if "choices" not in data:
        return f"LLM ERROR: {data}"

    return data['choices'][0]['message']['content']