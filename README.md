# BasicChatbot

A simple Python chatbot using Azure AI Foundry that responds to user prompts.

## Features
- Connects to Azure OpenAI / AI Foundry
- Chatbot responds to user input
- Easy to run locally

## Requirements
- Python 3.10+
- Libraries: `openai`, `azure-identity`, `requests`
- Azure AI account with GPT model deployed

## Setup & Run

### 1. Install libraries
```bash
pip install openai azure-identity requests
```

### 2. Set environment variables
```bash
set ENDPOINT_URL=https://<your-foundry-endpoint>.openai.azure.com/
set DEPLOYMENT_NAME=gpt-4
set AZURE_OPENAI_API_KEY=<your-api-key>
```

### 3. Run the chatbot
```bash
python basic_chatbot.py
```

## Notes

- You can edit the prompt in the code to change chatbot behavior.

- The project can be extended to include a web interface, file input, or images.
