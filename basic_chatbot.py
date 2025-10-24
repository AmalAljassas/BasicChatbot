import os
from openai import AzureOpenAI

# Environment variables
endpoint = os.getenv("ENDPOINT_URL", "https://<your-foundry-endpoint>.openai.azure.com/")
deployment = os.getenv("DEPLOYMENT_NAME", "gpt-4")
subscription_key = os.getenv("AZURE_OPENAI_API_KEY", "<your-api-key>")

# Initialize Azure OpenAI client
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=subscription_key,
    api_version="2025-01-01-preview",
)

# Chat prompt
chat_prompt = [
    {
        "role": "system",
        "content": [{"type": "text", "text": "You are an AI assistant that helps people find information."}]
    },
    {
        "role": "user",
        "content": [{"type": "text", "text": "Hello! Can you introduce yourself in 2 sentences?"}]
    }
]

# Generate completion
completion = client.chat.completions.create(
    model=deployment,
    messages=chat_prompt,
    max_tokens=1638,
    temperature=0.7
)

# Display response
bot_text = completion.choices[0].message.content
print("=== Chatbot Response ===")
print(bot_text)
