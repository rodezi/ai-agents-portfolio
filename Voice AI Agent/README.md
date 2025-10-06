# LiveKit Voice AI Agent 

# 🏡 Real Estate AI Assistant (LiveKit + OpenAI Llama + Deepgram)

An intelligent **voice-based AI agent** built with **LiveKit**, designed to assist **real estate professionals** by answering property inquiries, qualifying leads, and managing client interactions in real time.

This project demonstrates how to build an **AI-powered sales assistant** that can:

* Listen to users via voice input (Deepgram STT)
* Generate natural responses using LLMs (OpenAI Llama-3.3-70B via Cerebras)
* Speak back responses (Deepgram TTS)
* Handle turn-taking and voice activity detection automatically

---

## 🚀 Features

* 🎙️ **Real-time voice interaction** using LiveKit Agents
* 🧠 **LLM-powered logic** for conversational understanding
* 🏠 **Context-driven real estate knowledge base**
* 🔉 **Voice Activity Detection (VAD)** via Silero
* 🔁 **End-to-end speech pipeline** (STT → LLM → TTS)
* ⚙️ **Plugin architecture** with modular integrations

---

## 🧩 Architecture Overview

```plaintext
User 🎤
   ↓ (audio)
[LiveKit Room]
   ↓
Deepgram STT → Silero VAD → OpenAI (LLM via Cerebras) → Deepgram TTS
   ↓
Voice reply 🔊
```

The assistant uses contextual information loaded from `context.py` to provide accurate and compliant property information — without inventing or fabricating details.

---

## 🧠 Example Agent Logic

```python
class SalesAgent(Agent):
    def __init__(self):
        context = load_context()

        llm = openai.LLM.with_cerebras(model="llama-3.3-70b")
        stt = deepgram.STT()
        tts = deepgram.TTS()
        vad = silero.VAD.load()

        instructions = f"""
        You are a real estate sales agent communicating by voice. All text you return
        will be spoken aloud, so don't use things like bullets or slashes.

        Company Information:
        {context}

        CRITICAL RULES:
        - Only use information from the context.
        - If asked something not included, respond: "I don't have that information."
        - Never invent property details.
        """

        super().__init__(instructions=instructions, stt=stt, llm=llm, tts=tts, vad=vad)
```

---

## 🏗️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/real-estate-ai-agent.git
cd real-estate-ai-agent
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # on macOS/Linux
.venv\Scripts\activate     # on Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your environment variables

Create a `.env.local` file with your API keys:

```bash
LIVEKIT_URL=<your_livekit_server_url>
LIVEKIT_API_KEY=<your_api_key>
LIVEKIT_API_SECRET=<your_api_secret>

OPENAI_API_KEY=<your_openai_key>
DEEPGRAM_API_KEY=<your_deepgram_key>
```

---

## 🧰 Required Plugins

Make sure you have all necessary LiveKit plugins installed:

```bash
pip install livekit-agents
pip install livekit-plugins-openai
pip install livekit-plugins-deepgram
pip install livekit-plugins-silero
pip install livekit-plugins-turn-detector
python-dotenv
```

---

## 🧾 Example JSON (Business Context)

The assistant can be enriched with contextual product data, such as pricing, objections, and benefits:

```json
{
  "ai_agent": {
    "name": "RealEstate AI Assistant",
    "description": "Voice-based assistant that qualifies leads and answers property questions using LiveKit and Deepgram.",
    "key_capabilities": [
      "Answers property inquiries in real time",
      "Qualifies leads by intent and budget",
      "Schedules visits and syncs with CRM",
      "Integrates with Kommo or Zoho"
    ],
    "target_users": "Real estate agents and agencies"
  }
}
```

This data is loaded dynamically from `context.py`.

---

## 🧪 Run the Agent

```bash
```
