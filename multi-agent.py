from smolagents import (
    CodeAgent,
    ToolCallingAgent,
    HfApiModel,
    ManagedAgent,
    DuckDuckGoSearchTool,
    LiteLLMModel,
)

from tools.tools import visit_webpage

model = HfApiModel()

web_agent = ToolCallingAgent(
    tools=[visit_webpage],
    model=model,
    max_steps=5,
)

managed_web_agent = ManagedAgent(
    agent=web_agent,
    name="search",
    description="Runs web searches for you. Give it your query as an argument.",
)

manager_agent = CodeAgent(
    tools=[],
    model=model,
    managed_agents=[managed_web_agent],
    additional_authorized_imports=["time", "numpy", "pandas" ,"bs4", "request"],
)

answer = manager_agent.run("""
                           visit website and list prices
                            additional_args={"url": "https://www.smartbox.com/fr/"}
                           """)
print(answer)