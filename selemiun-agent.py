from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel

agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=HfApiModel(), additional_authorized_imports=["selenium"])
#agent.run("write a selenium test in headful mode to navigate to https://gh-users-search.netlify.app/ and search for nand in search-bar and click on submits button")
agent.run("write a selenium test in headful mode to navigate to https://gh-users-search.netlify.app/ and enter nand in input field data-testid=search-bar and click on submits button")

