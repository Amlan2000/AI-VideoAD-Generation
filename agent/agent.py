from os import system
from langchain_ollama import ChatOllama
from langchain.agents import initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory
from tools.spotify_tool import fetch_top_songs


def get_agent():
    llm = ChatOllama(
        model="llama3",
        temperature=0.5
    )

    # tools = [audio_tool, spotify_tool, sync_tool, video_tool]
    tools=[fetch_top_songs]

    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )

    # system_prompt = get_system_prompt()
    system_prompt = "Answer questions as you are asked"

    agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
        verbose=True,
        memory=memory,
        handle_parsing_errors=True,
        system_message=system_prompt
    )

    return agent
