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
    Save a task description into a test case file and return the saved file name.

    This tool saves the provided task description into a file in the `test_cases` directory.
    If the directory does not exist, it will be created.

    Args:
        filename: The name of the test case file to be created. 
                    This should include the file extension (e.g., "test_case_1.txt").
        task: The task description or content to be saved in the file.

    Returns:
        str: A confirmation message with the name of the saved file.

    Raises:
        IOError: If the file cannot be created or written.
    """
    try:
        # Write the task to the specified file
        with open(f"features/{filename}", 'w') as file:
            file.write(task)

        print(f"File created successfully")
        return f"Saved file name is: {filename}"
    except IOError as e:
        return f"An error occurred while saving the file: {e}"

@tool
def read_testcase_file(filename: str, task: str) -> str:
    """
    Read the contents of a test case file and return its content.

    This tool reads the content of a specified test case file from the `test_cases` directory.
    If the file does not exist or cannot be read, an appropriate error message is returned.

    Args:
        filename: The name of the test case file to be read. 
                        This should include the file extension (e.g., "test_case_1.txt").
        task: The task to read file from filename.

    Returns: The content of the test case file if it is successfully read, 
             or an error message if the file cannot be found or read.
    """
    try:
        with open(f"features/{filename}", 'r') as file:
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
def save_code_to_file(code: str, codefilename: str) -> str:
    """
    Save LLM-generated code into a specified file.

    Args:
        code: The code to be saved into the file. This should be a valid string containing Python or any other language code.
        codefilename: The name of the file to save the code in. Defaults to "generated_code.py". 
                        The file will be created in the 'generated_code' directory.

    Returns:
        str: A confirmation message if the code is successfully saved, or an error message if something goes wrong.
    """
    
    try:
        with open(f"src/{codefilename}", "w") as file:
            file.write(code)
        return f"Code successfully saved to {codefilename}"
    except Exception as e:
        return f"Failed to save code: {e}"

@tool
def execute_api_test(codefilename: str, task: str) -> str:
    """
    This is a tool is to execute api test using pytest
    It returns saved filename.

    Args:
        task: The task to pytest code in file
        codefilename: name of the test code file.
    """
    result = subprocess.run(['pytest', './src/{}'.format(codefilename), '--html=report/report.html'], capture_output=True, text=True)    
    
    print(result.stdout)
    return f"saved filed name is: {codefilename}"