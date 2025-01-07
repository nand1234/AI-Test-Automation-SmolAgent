from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel

playwright_agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=HfApiModel(), additional_authorized_imports=["playwright", "asyncio"])
playwright_agent.run("write a playwright test in headlful mode to navigate to https://gh-users-search.netlify.app/ and enter nand in input field data-testid=search-bar and click on search button")