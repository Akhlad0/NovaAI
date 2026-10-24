# Nova AI Voice Assistant (Python + GitHub Codespaces)

A simple browser-based voice assistant with a Python/Flask backend and an AI chat API.

## Features
- Text chat with an AI model
- Browser speech-to-text (supported browsers)
- Browser text-to-speech
- Responsive mobile-friendly interface
- Simple website-opening commands can be added later

## Run in GitHub Codespaces

1. Create a GitHub repository and upload these project files.
2. Open the repository, choose **Code → Codespaces → Create codespace**.
3. In the Codespaces terminal, install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set the API key as a Codespaces secret named `OPENAI_API_KEY` (recommended), or temporarily set it in the terminal:
   ```bash
   export OPENAI_API_KEY="your_api_key_here"
   ```
   Never commit the key into GitHub or paste it into `app.py`.
5. Optional: choose a model available to your API account:
   ```bash
   export OPENAI_MODEL="gpt-4o-mini"
   ```
6. Start the app:
   ```bash
   python app.py
   ```
7. When Codespaces offers to open port **8000**, choose **Open in Browser**.

## Notes
- The AI API requires an API key and may incur usage charges. ChatGPT subscriptions and API billing are separate.
- Voice input uses browser speech-recognition support and may depend on browser permissions and connectivity.
- Text-to-speech uses your browser/device voices.
- If the mic does not work, allow microphone access or use text chat.
- The app does not listen continuously; tap **Speak** when you want to talk.
