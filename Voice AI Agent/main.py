from dotenv import load_dotenv
from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.plugins import noise_cancellation, silero, openai, deepgram
from livekit.plugins import openai
from livekit.plugins.turn_detector.multilingual import MultilingualModel
from context import load_context

load_dotenv(".env.local")


class SalesAgent(Agent):
    def __init__(self):
        # Load context once at startup
        context = load_context()
        print(f"📄 Loaded context: {len(context)} characters")

        llm = openai.LLM.with_cerebras(
            model="llama-3.3-70b"
        )
        stt = deepgram.STT()
        tts = deepgram.TTS()
        vad = silero.VAD.load()

        # Put ALL context in system instructions
        instructions = f"""
        You are a real estate sales agent communicating by voice. All text you return
        will be spoken aloud, so don't use things like bullets, slashes, or any
        other non-pronouncable punctuation.

        You have access to the following company information:

        {context}

        CRITICAL RULES:
        - ONLY use information from the context above
        - If asked about an specific property or something not in the context, say "I don't have that information"
        - DO NOT make up prices, features, or any other details
        - Quote directly from the context when possible
        - Be a sales agent but only use the provided information
        """

        super().__init__(
            instructions=instructions,
            stt=stt, llm=llm, tts=tts, vad=vad
        )

    # This tells the Agent to greet the user as soon as they join, with some context about the greeting.
    async def on_enter(self):
        self.session.generate_reply(
            user_input="Give a short, 1 sentence greeting. Offer to answer any questions.")


print("Real Estate assistant class is ready")
