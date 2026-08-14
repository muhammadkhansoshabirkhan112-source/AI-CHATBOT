README.md
🤖 AI Chatbot — Gemini + Streamlit
A simple AI chatbot built with Python, Streamlit, and the Google Gemini API. It provides a clean chat interface, maintains conversation context during the session, and securely loads the Gemini API key using Streamlit Secrets.
✨ Features
🤖 Google Gemini-powered AI chatbot
💬 Interactive Streamlit chat interface
🧠 Conversation memory during the current session
🗑️ Clear chat button
🔐 Secure API-key configuration
⚡ Fast and lightweight
📱 Responsive web interface
🛠️ Technologies
Python 3.10+
Streamlit
Google Gen AI SDK
Gemini API
Gemini Interactions API
📁 Project Structure
AI-CHATBOT/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── .streamlit/
    └── secrets.toml
🚀 Installation
1. Clone the repository
git clone YOUR_GITHUB_REPOSITORY_URL
cd AI-CHATBOT
2. Create a virtual environment
Windows:
python -m venv venv
venv\Scripts\activate
macOS/Linux:
python3 -m venv venv
source venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
Or:
pip install -U streamlit google-genai
🔑 API Key Setup
Create:
.streamlit/secrets.toml
Add your Gemini API key:
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
Never upload your API key to GitHub.
Add this to .gitignore:
.streamlit/secrets.toml
venv/
__pycache__/
*.pyc
.env
📦 requirements.txt
streamlit
google-genai
▶️ Run the Application
Start the chatbot with:
streamlit run app.py
If necessary, use:
python -m streamlit run app.py
Then open:
http://localhost:8501
in your browser.
💬 How It Works
The application loads the Gemini API key from Streamlit Secrets, creates a Google Gen AI client, accepts the user's message, sends it to Gemini through the Interactions API, and displays the AI response.
The application also stores the interaction ID so that Gemini can maintain context throughout the current conversation.
Example:
User: My name is Ahmed.

AI: Nice to meet you, Ahmed!

User: What is my name?

AI: Your name is Ahmed.
Clicking Clear Chat resets the conversation.
⚠️ Troubleshooting
404 Model Error
If you see:
404 NOT_FOUND
This model is no longer available to new users
your selected Gemini model is not available to your API account.
For example, if your code contains:
model="gemini-2.5-flash"
you should change it to a currently available model supported by your account.
You can check available models with:
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

for model in client.models.list():
    print(model.name)
Then use one of the available model names in your application.
API Key Error
If you get:
GEMINI_API_KEY is not configured
make sure this file exists:
.streamlit/secrets.toml
and contains:
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
Google Gen AI Module Error
If you get:
ModuleNotFoundError: No module named 'google'
run:
pip install -U google-genai
Streamlit Command Error
If streamlit isn't recognized, run:
python -m streamlit run app.py
🔐 Security
Never put your API key directly into app.py.
❌ Don't do this:
client = genai.Client(
    api_key="YOUR_SECRET_API_KEY"
)
✅ Use Streamlit Secrets:
import streamlit as st
from google import genai

client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)
If an API key is accidentally published, revoke it and create a new one.
☁️ Deployment
The chatbot can be deployed to a Streamlit-compatible hosting service.
For Streamlit Community Cloud:
Push app.py, requirements.txt, and README.md to GitHub.
Create your Streamlit application.
Add GEMINI_API_KEY through the application's Secrets settings.
Deploy the application.
Do not upload:
.streamlit/secrets.toml
to GitHub.
🔮 Future Improvements
🎨 Custom themes
🌙 Dark mode
📎 File uploads
🖼️ Image support
🎤 Voice input
🔊 Text-to-speech
💾 Persistent conversations
👤 User authentication
🗂️ Multiple chat sessions
⚙️ Custom AI settings
🌐 Cloud deployment
📚 Documentation
Google Gemini API Documentation⁠�
Gemini Interactions API⁠�
Streamlit Documentation⁠�
Google Gen AI Python SDK⁠�
👨‍💻 Author
Your Name
Built with ❤️ using Python + Streamlit + Google Gemini.
📄 License
This project is available for personal and educational use. Add your preferred open-source license if you plan to distribute the project publicly.
⭐ Support
If you find this project useful, consider giving it a ⭐ on GitHub.
