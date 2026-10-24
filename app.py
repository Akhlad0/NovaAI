import os
from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)

SYSTEM_PROMPT = (
    "You are Nova, a friendly, helpful AI voice assistant. "
    "Answer clearly and naturally for spoken conversation. "
    "Keep most answers concise unless the user asks for detail. "
    "You cannot actually control the user's device or access live information "
    "unless a tool explicitly provides it."
)

@app.get("/")
def home():
    return render_template("index.html")

@app.post("/chat")
def chat():
    data = request.get_json(silent=True) or {}
    message = (data.get("message") or "").strip()
    history = data.get("history") or []

    if not message:
        return jsonify({"error": "Please enter or say a message."}), 400

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        return jsonify({
            "error": "OPENAI_API_KEY is not set. Add it in your Codespace Secrets, then restart the app."
        }), 500

    try:
        client = OpenAI(api_key=api_key)
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]

        # Only accept a small, safe amount of recent conversation history.
        for item in history[-8:]:
            role = item.get("role")
            content = item.get("content")
            if role in ("user", "assistant") and isinstance(content, str):
                messages.append({"role": role, "content": content[:4000]})
        messages.append({"role": "user", "content": message[:4000]})

        response = client.chat.completions.create(
            model=os.environ.get("OPENAI_MODEL", "gpt-4o-mini"),
            messages=messages,
            max_tokens=500,
        )
        answer = response.choices[0].message.content or "Sorry, I couldn't create a response."
        return jsonify({"answer": answer})
    except Exception as exc:
        # Avoid exposing credentials or detailed internal errors to the browser.
        print("AI request failed:", repr(exc))
        return jsonify({"error": "The AI request failed. Check your API key, model access, and API billing."}), 502

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "8000")), debug=False)
