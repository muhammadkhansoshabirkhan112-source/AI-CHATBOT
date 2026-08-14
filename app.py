import streamlit as st
from google import genai

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# -----------------------------
# Gemini API configuration
# -----------------------------
GEMINI_API_KEY = st.secrets.get("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    st.error("GEMINI_API_KEY is not configured.")
    st.stop()

client = genai.Client(api_key=GEMINI_API_KEY)

# -----------------------------
# App title
# -----------------------------
st.title("🤖 AI Chatbot")
st.caption("Powered by Google Gemini")

# -----------------------------
# Initialize chat history
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "previous_interaction_id" not in st.session_state:
    st.session_state.previous_interaction_id = None

# -----------------------------
# Display previous messages
# -----------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# Chat input
# -----------------------------
user_message = st.chat_input("Type your message...")

if user_message:

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_message)

    st.session_state.messages.append({
        "role": "user",
        "content": user_message
    })

    try:
        # -----------------------------
        # Send message to Gemini
        # -----------------------------
        if st.session_state.previous_interaction_id:

            interaction = client.interactions.create(
                model="gemini-3.6-flash",
                input=user_message,
                previous_interaction_id=(
                    st.session_state.previous_interaction_id
                )
            )

        else:

            interaction = client.interactions.create(
                model="gemini-3.6-flash",
                input=user_message
            )

        # -----------------------------
        # Get Gemini response
        # -----------------------------
        response_text = interaction.output_text

        # Save interaction ID for conversation memory
        st.session_state.previous_interaction_id = interaction.id

        # -----------------------------
        # Display assistant response
        # -----------------------------
        with st.chat_message("assistant"):
            st.markdown(response_text)

        st.session_state.messages.append({
            "role": "assistant",
            "content": response_text
        })

    except Exception as e:

        st.error(f"Error: {e}")

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.header("⚙️ Settings")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.session_state.previous_interaction_id = None
        st.rerun()

    st.divider()

    st.write("**Model:** Gemini 3.6 Flash")
    st.write("**API:** Google Gemini Interactions API")