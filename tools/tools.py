from smolagents import tool
from huggingface_hub import list_models
import subprocess


@tool
def model_download_tool(task: str) -> str:
    """
    This is a tool that returns the most downloaded model of a given task on the Hugging Face Hub.
    It returns the name of the checkpoint.

    Args:
        task: The task for which to get the download count.
    """
    most_downloaded_model = ['model1', 'model2']
    return most_downloaded_model[0]


@tool
def write_testcase_file(filename: str, task: str) -> str:
    """
    This is a tool that returns saved file name.
    It returns saved filename.

    Args:
        task: The task to save file into local directory.
        filename: name of the test case file.
    """
    with open(f"test_cases/{filename}", 'w') as file:
        file.write(task)

    print(f"File created successfully")
    return f"saved filed name is: {filename}"

@tool
def read_testcase_file(filename: str, task: str) -> str:
    """
    This is a tool that read feature file for execution.
    It returns file content.

    Args:
        task: The task to read file from filename.
        filename: name of the test case file.
    """
    try:
        with open(f"test_cases/{filename}", 'r') as file:
            content = file.read()
    except FileNotFoundError:
        return "Error: File not found."
    except PermissionError:
        return "Error: Permission denied."
    except IOError as e:
        return f"Error: An I/O error occurred: {e}"

    print(f"File created successfully")
    return str(content)

@tool
def report(task: str) -> str:
    """
    test execution report in json
    It save report json file.

    Args:
        task: The task to save test execution report in json format
    """
    with open('reports/result.json', 'w') as file:
        file.write(task)

    print(f"File created successfully")
    return f"saved filed name is result.json"

@tool
def write_pytest_code(codefilename: str, task: str) -> str:
    """
    This is a tool write pytest code in the file
    It returns saved filename.

    Args:
        task: The task to write pytest code in file
        codefilename: name of the test code file.
    """
    with open(f"test_cases/{codefilename}", 'w') as file:
        file.write(task)

    print(f"File created successfully")
    return f"saved filed name is: {codefilename}"

@tool
def execute_api_test(codefilename: str, task: str) -> str:
    """
    This is a tool is to execute api test using pytest
    It returns saved filename.

    Args:
        task: The task to pytest code in file
        codefilename: name of the test code file.
    """
    result = subprocess.run(['pytest', './test_cases/{}'.format(codefilename), '--html=report.html'], capture_output=True, text=True)    
    
    print(result.stdout)
    return f"saved filed name is: {codefilename}"