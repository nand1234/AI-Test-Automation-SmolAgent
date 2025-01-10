from smolagents import CodeAgent, HfApiModel
from tools.tools import report, read_testcase_file, write_pytest_code, execute_api_test


test_case_agent = CodeAgent(tools=[read_testcase_file,report, write_pytest_code, execute_api_test], model=HfApiModel(), additional_authorized_imports=['requests', 'bs4', 'pytest','pytest-html', 'json'])

"""
write test code
"""
test_case_agent.run(
   """
   can you save generate pytest code for test case file using request module
   additional_args={"filename":'api_test.feature', "codefilename": "api_test.py"}
   """
)


"""
Execute test
"""
test_case_agent.run(
   """
   can you execute api test from saved file
   additional_args={"codefilename": "api_test.py"}
   """
)

