# recipe-finder-agent
 This readme shows the step how to config before run application

### Prerequisite 
- python
- pip
- IDE (recommend PyCharm)


### 1. Create the venv
- Use the command below to create the virtual environment 

    ```python -m venv ./venv```</br>
    ```source ./venv/bin/activate```

### 2. Install the required packages
- Use the command below. This will install all the packages listed in your requirements.txt file.

    ```pip install -r requirements.txt```

### 3. Create .env file and add following code into the file
- Replace the key and endpoint
  ```
  OPENAI_API_TYPE=azure
  AZURE_OPENAI_API_KEY= # TODO Key: Replace by API-KEY (Azure OpenAI)
  AZURE_OPENAI_ENDPOINT= # TODO Key: Replace by Endpoint (Azure OpenAI)
  GOOGLE_API_KEY= # TODO Key: Replace by API-KEY (Google vertex - Gemini)
  ```
