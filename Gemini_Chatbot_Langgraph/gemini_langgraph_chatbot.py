import os
from typing import TypedDict, List, Union
from langchain_core.messages import HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv


load_dotenv()

class AgentState(TypedDict):
    messages: List[Union[HumanMessage, AIMessage]]

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash", # -> Gemini 2.0 flash
    google_api_key=os.getenv("GEMINI_API_KEY") 
)  

def process(State: AgentState) -> AgentState:
    """This node will act as the request you enter / input"""  
    response = llm.invoke(State["messages"])
    State["messages"].append(AIMessage(content=response.content))
    print(f"\nAI Agent: {response.content}")
    print("CURRENT STATE: ", State["messages"]) # This output is for debugging purposes

    return State

# The graph's defined below 
graph = StateGraph(AgentState)
graph.add_node("process", process)
graph.add_edge(START, "process")
graph.add_edge("process", END) 
agent = graph.compile()  ### --> Compiling the graph

conversation_history = [] # Conversation memory 

user_input = input("Enter: ") # Request by the user 
while user_input != "exit":  # The loop ends if user texts exit
    conversation_history.append(HumanMessage(content=user_input))  # Human Message appended's to conversation history
    # Entire conversation is set 
    result = agent.invoke({"messages": conversation_history}) # Invoke the agent with the conversation history
    conversation_history = result["messages"]
    user_input = input("Enter: ") # Request by the user -- Ask me something :)

with open("logging.txt", "w") as file:  # Open a file to log the conversation
    file.write("Your Conversation Log:\n")  # Efficient way for prototypes 
    
    for message in conversation_history: # For every message in the conversation history 
        if isinstance(message, HumanMessage): # We store human and AI messages
            file.write(f"You: {message.content}\n")
        elif isinstance(message, AIMessage):
            file.write(f"AI: {message.content}\n\n")
    file.write("End of Conversation")

print("Conversation logged to logging.txt")  # Confirmation message after logging