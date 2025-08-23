from agent.agent import get_agent


if __name__ == "__main__":
    agent = get_agent()
    response = agent.run("what are the top 3 trending songs right now?")
    print(response)
