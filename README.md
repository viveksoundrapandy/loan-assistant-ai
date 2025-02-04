# Setup and Execution Guide

Ensure you follow the steps below to set up and run the project using Python 3.10. The OpenAI SDK may fail on the latest version of Python, so we will use `pyenv` to manage Python versions locally.

---

## Prerequisites

1. **Install pyenv**  
   Use `pyenv` to manage multiple Python versions on your local machine. If you don't have `pyenv` installed, follow the installation guide for your operating system from [here](https://github.com/pyenv/pyenv).

2. **Install virtualenv**  
   Ensure that `virtualenv` is installed on your system. You can install it using pip:
   ```bash
   pip install virtualenv
- Install dependencies from `requirements.txt`
- Run `python testai.py` to validate the flow


## Install Langflow

To install Langflow, follow the steps provided in the official documentation: [Langflow Installation Guide](https://docs.langflow.org/get-started-installation).

## Start Langflow Project

Once Langflow is installed, you can start your Langflow project by running the following command:

   ```bash
   python -m langflow run
   ```
- Install dependencies from `requirements.txt`

## Import Project File

After starting the project, import the project file `Loan Assistant.json` into Langflow to begin using the pre-configured project.
