from tools.agent_tools import TOOLS

from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4.1",
    temperature=0,
)

agent = create_agent(
    model=llm,
    tools=TOOLS,
)

prompt = input("> ")

response = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }
)

print(response["messages"][-1].content)