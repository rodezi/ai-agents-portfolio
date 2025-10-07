# 🤖 Gemini Chatbot with LangGraph

Hi, I'm **Rodrigo Zayas** — this is my prototype chatbot built with **LangGraph** and **Google's Gemini 2.0 Flash**.

---

## 🧠 Description

This project implements a **conversational AI agent** using [LangGraph](https://github.com/langchain-ai/langgraph) for state management and [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs) as the underlying large language model.

The chatbot maintains **multi-turn conversations**, logs the full dialogue into a local `logging.txt` file, and runs entirely from the terminal — ideal for quick prototyping or backend integration.

---

## ✨ Features

* ⚙️ Built with **LangGraph** for graph-based conversational flow
* 💬 Uses **Gemini 2.0 Flash** (Google Generative AI)
* 🧾 Logs conversation history to `logging.txt`
* 🧩 Simple **terminal interface** (adaptable to FastAPI, Streamlit, etc.)
* 🔁 Supports **multi-turn** memory through message history

---

## 🧩 Tech Stack

| Component            | Description                         |
| -------------------- | ----------------------------------- |
| **LangGraph**        | Conversation and state management   |
| **Gemini 2.0 Flash** | Large Language Model (LLM)          |
| **LangChain Core**   | Message schema & prompt handling    |
| **Python dotenv**    | Securely loads API keys from `.env` |

---

## 🚀 Setup & Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/tuusuario/gemini-langgraph-agent.git
cd gemini-langgraph-agent
```

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Create a `.env` file

Inside the project folder, add your Google API key:

```
GEMINI_API_KEY=your_api_key_here
```

### 5️⃣ Run the chatbot

```bash
python main.py
```

---

## 🗂️ Project Structure

```
.
├── main.py            # Core chatbot logic
├── .env               # Environment variables
├── requirements.txt   # Dependencies list
└── logging.txt        # Conversation logs
```

---

## 🧠 How It Works

1. The chatbot starts a LangGraph with a single `process` node.
2. Each user input is appended to a message list (`conversation_history`).
3. The Gemini model generates responses through `llm.invoke()`.
4. All messages (user + AI) are stored and finally logged to `logging.txt`.

---

## 📄 Example Output

**User:** What’s the capital of Japan?
**AI:** The capital of Japan is Tokyo.

All exchanges are automatically stored in `logging.txt` for review.

---

## 🔮 Future Improvements

* Integrate FastAPI or Streamlit interface
* Add persistent vector-based memory (e.g., Pinecone)
* Enable function calling or structured outputs
* Deploy on Hugging Face or a local web UI

---

## 🧑‍💻 Author

**Rodrigo Zayas**
AI Engineer in progress — passionate about building agentic systems and automation with LangGraph & LLMs.

---

## 🪪 License

This project is released under the **MIT License** — feel free to use and modify it.


