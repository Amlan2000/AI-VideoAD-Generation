# agent/agent.py
from langchain_core.prompts import PromptTemplate
from langchain.agents import create_react_agent, AgentExecutor
from langchain_ollama import ChatOllama
from tools.audio_generation_tool import audio_generation
from tools.video_generation_tool import generate_shoe_video

def get_agent():
    llm = ChatOllama(model="llama3", temperature=0.5)
    tools = [audio_generation, generate_shoe_video]
    
    # Use PromptTemplate for ReAct agents (string-based scratchpad)
    prompt = PromptTemplate.from_template("""
You are an AI assistant that creates Instagram marketing videos for shoes.

WORKFLOW:
1. First call audio_generation_tool to get beat data
2. Then call video_generation_tool with that beat data
3. Return the final video path

You have access to the following tools:
{tools}

Tool names: {tool_names}

Use the following format:
Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
Thought: {agent_scratchpad}
""")
    
    agent = create_react_agent(llm, tools, prompt)
    return AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)
