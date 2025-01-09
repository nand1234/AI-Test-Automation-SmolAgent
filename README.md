
# Automated Testing with Hugging Face SmolAgent

This project leverages [Hugging Face SmolAgent](https://huggingface.co/docs/smolagents/guided_tour) to create and execute automated tests using Selenium, Pytest, and Playwright.

---

## Prerequisites

- **Python 3.7 or higher**
- Required libraries specified in `requirements.txt`

---

## Setup Instructions

1. **Clone the repository**  
   Clone the repository to your local machine:
   ```bash
   git clone https://github.com/nand1234/AI-Test-Automation-SmolAgent.git
   cd AI-Test-Automation-SmolAgent
   ```

2. **Create a Python virtual environment**  
   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment**  
   - On **Linux/Mac**:
     ```bash
     source ./venv/bin/activate
     ```
   - On **Windows**:
     ```bash
     .\venv\Scripts\activate
     ```

4. **Install dependencies**  
   Install the required libraries with:
   ```bash
   pip install -r requirements.txt
   ```

---

## How to Run Tests

### 1. **API Test Agent**
Run the API test agent using the following command:
```bash
python api-agent.py
```

### 2. **Selenium UI Test Agent**
Execute Selenium-based UI tests with:
```bash
python selenium-agent.py
```

### 3. **Playwright Test Agent**
Run Playwright-based tests with:
```bash
python playwright-agent.py
```
### 4. **BDD test case creation Agent**
Run test case creatio with:
```bash
python testcase-agent.py
---

```
### 4. **BDD test case execution Agent**
Run BDD test case execution:
```bash
python test-executor-agent.py
---



## Key Insights

### Findings
1. **Additional Authorized Imports**  
   The `additional_authorized_imports` parameter enables the LLM model to interact with specified external libraries.  
   For example:
   ```python
   additional_authorized_imports=["playwright", "asyncio"]
   ```

2. **Installing External Libraries**  
   Install any required external libraries with:
   ```bash
   pip install <library-name>
   ```
   By default, the execution is done in your local environment. This should be safe because the only functions that can be called are the tools you provided (especially if it's only tools by Hugging Face) and a set of predefined safe functions like print or functions from the math module, so you're already limited in what can be executed.

   The Python interpreter also doesn't allow imports by default outside of a safe list, so all the most obvious attacks shouldn't be an issue. You can authorize additional imports by passing the authorized modules as a list of strings in argument additional_authorized_imports upon initialization of your [CodeAgent]:

### Observations
- The output of the test agents depends on the underlying LLM model used for execution.  
- By default, Hugging Face uses the `HfApiModel()` instance, which typically employs models like Qwen/Qwen2.5-Coder-32B-Instruct.

---