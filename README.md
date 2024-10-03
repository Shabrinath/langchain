## Overview

This project builds a **Skill Generator** web application using **Streamlit** and **Langchain**. The tool helps users generate a list of technologies to learn based on a specific engineering job role (e.g., DevOps Engineer, Data Engineer, etc.). It leverages the power of OpenAI’s language models to suggest relevant skills dynamically.

### Features:
- **Role-Based Skill Recommendations**: Users can select from various engineering roles, and the app provides a list of recommended technologies for each role.
- **Streamlit Integration**: The application is built with Streamlit, making it easy to run as a web application with an interactive user interface.
- **OpenAI's GPT Integration**: The app uses OpenAI's GPT model to generate skill suggestions using the Langchain framework.

## How It Works

### File: `main.py`

1. **Imports and Environment Setup**:
   - The required packages (`streamlit`, `langchain`, `os`, and `langchain_helper`) are imported.
   - The OpenAI API key is set using the `os.environ` variable to securely manage the API key.

2. **Langchain Setup**:
   - The code defines the prompt structure using `Langchain`, which tells GPT to generate a comma-separated list of technologies based on the job role selected by the user.
   - The `generate_technologies_for_role` function utilizes a prompt template. It asks GPT to suggest technologies for a specific engineering role and provides descriptions for each technology.

3. **Streamlit UI**:
   - The `streamlit` application has a title, "Skill Generator."
   - A sidebar allows users to pick from different job roles like **DevOps Engineer**, **Data Engineer**, **AI Engineer**, **QA Engineer**, and **Java Developer**.
   - When the user selects a job role, the `langchain_helper.generate_technologies_for_role` function is called to generate a list of technologies.
   - The response is displayed in a clean, user-friendly format on the Streamlit app.

### File: `langchain_helper.py`

This file contains the **Langchain** logic for generating skills based on job roles:

1. **LLMChain Setup**:
   - The OpenAI GPT-3 model is instantiated with a temperature of `0.7`, which controls the model's creativity level.
   
2. **Prompt Template**:
   - The `PromptTemplate` ensures that the model receives consistent input to generate technologies relevant to a specific engineering role. It asks GPT to provide the technologies and descriptions in a comma-separated format.

3. **Chain Execution**:
   - The `LLMChain` handles the prompt execution, passing the job role to the OpenAI model and retrieving the response.

4. **Return Output**:
   - The function formats the response, which is then passed to the Streamlit app for display.

## How to Run the Project

1. **Install Dependencies**:
   ```bash
   pip install streamlit
   pip install langchain
   pip install langchain_community
   pip install openai
   ```

2. **Set OpenAI API Key**:
   You will need to set your OpenAI API key in a `secret_key.py` file or as an environment variable:
   ```python
   openapi_key = "your-openai-api-key-here"
   ```

3. **Run the Application**:
   Use the following command to run the app:
   ```bash
   streamlit run main.py
   ```

4. **Access the App**:
   Once the app is running, a browser window will open where you can select a job role from the sidebar. The app will then generate a list of technologies relevant to that role.

---
