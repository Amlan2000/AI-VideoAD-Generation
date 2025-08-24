from agent.agent import get_agent


if __name__ == "__main__":
    agent = get_agent()
    response = agent.invoke({
        "input": "Create an Instagram marketing video for a shoe using top trending songs"
    })
    print(response)
