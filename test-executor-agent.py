from smolagents import CodeAgent, HfApiModel
from tools.tools import report, read_testcase_file


test_case_agent = CodeAgent(tools=[read_testcase_file,report], model=HfApiModel(), additional_authorized_imports=['requests', 'bs4', 'pytest-bdd', 'json'])

"""
Execute BDD style test cases from feature file
"""
test_case_agent.run(
   """
   can you execute BDD style test case using pytest-bdd using task "read_file" return test execution report in json format using task "report"
   additional_args={"filename":'api_test.feature'}
   """
)

