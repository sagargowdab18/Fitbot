
# 💪 FitBot AI – Your Personal Fitness Assistant

FitBot AI is an AI-powered fitness chatbot built using Python, Streamlit, and Groq API. It helps users with workout guidance, nutrition information, and general fitness-related questions.

## 🚀 Features

- AI-powered fitness conversations
- Workout and exercise guidance
- General nutrition and protein recommendations
- Conversation memory during a session
- Interactive chat interface using Streamlit
- Groq LLM integration

## 🛠️ Tech Stack

- **Language:** Python
- **Frontend:** Streamlit
- **LLM API:** Groq API
- **SDK:** OpenAI Python SDK
- **Environment Variables:** python-dotenv
- **Model:** openai/gpt-oss-120b

## 📁 Project Structure

```text
FitBot/
│
├── app.py
├── chatbot.py
├── prompts.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/sagargowdab18/Fitbot.git
```

### 2. Navigate to the project folder

```bash
cd Fitbot
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```powershell
venv\Scripts\activate
```

### 5. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 6. Configure your API key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

Get your API key from:

https://console.groq.com/keys

Never share or upload your actual API key.

### 7. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🧠 How It Works

1. The user enters a fitness-related question.
2. Streamlit captures the input.
3. The conversation history is maintained using `st.session_state`.
4. The chatbot sends the system prompt and conversation history to the Groq API.
5. The LLM generates a response.
6. Streamlit displays the response to the user.

## 🔮 Future Improvements

- Personalized fitness profiles
- Custom workout plan generation
- Nutrition and calorie tracking
- Retrieval-Augmented Generation (RAG)
- Chat history stored in a database
- Deploy FitBot online

## ⚠️ Disclaimer

FitBot provides general fitness and nutrition information and is not a substitute for professional medical advice.

## 👨‍💻 Author

**Sagar B**

GitHub: https://github.com/sagargowdab18
