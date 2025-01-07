
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
   Ensure these libraries are added to `additional_authorized_imports` for the LLM model to access them.

### Observations
- The output of the test agents depends on the underlying LLM model used for execution.  
- By default, Hugging Face uses the `HfApiModel()` instance, which typically employs models like Qwen/Qwen2.5-Coder-32B-Instruct.

---