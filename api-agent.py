from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel


api_agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=HfApiModel(), additional_authorized_imports=['requests', 'bs4', 'pytest'])
#api_agent.run("write pytest for GET endpoint https://httpbin.org/get and check status is 200")
api_agent.run("write pytest for GET endpoint https://httpbin.org/get and check status is not 300, 500, 302")

