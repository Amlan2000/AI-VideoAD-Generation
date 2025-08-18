from agent.agent import get_agent


if __name__ == "__main__":
    agent = get_agent()
    response = agent.run("What is the capital of India?")
    print(response)
