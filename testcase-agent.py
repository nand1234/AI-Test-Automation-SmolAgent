from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel
from tools.tools import write_testcase_file


test_case_agent = CodeAgent(tools=[write_testcase_file], model=HfApiModel(), additional_authorized_imports=['requests', 'bs4', 'pytest'])

"""
agent to create UI test cases based on requirements
"""
test_case_agent.run(
   """
   can you please write BDD style test cases for below requirement.
   rules: create single feature, include edge cases, use boundry value and equivalent partitioning test case creation technique. also, don't hallucinate or create madeup testcases.
   additional_args={"filename":'login_test.feature'}
   requirement:The login page should be the first page that users see in the modified application. It should provide two text fields - one for entering a login name and one for entering a password. In addition it should have a command button that initiates the password checking action. If either of the text fields is left blank it is an error that must be reported to the user. If both fields are filled in but there is no record of the user name or the password is incorrect that must also be reported to the user. 
   """
)

"""
agent to create API tests
"""
test_case_agent.run(
   """
   can you please write BDD style test cases for below requirement.
   rules: create single feature, include edge cases, negative cases, use boundry value and equivalent partitioning test case creation technique. also, don't hallucinate or create madeup testcases.
   additional_args={"filename":'api_test.feature'}
   requirement: GET endpoint https://httpbin.org/get without query param
   """
)

