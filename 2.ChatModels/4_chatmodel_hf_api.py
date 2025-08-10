from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()  # Loads HUGGINGFACEHUB_ACCESS_TOKEN from .env

llm = HuggingFaceEndpoint(
    repo_id="microsoft/DialoGPT-medium",  # Supported for chat-like text generation
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
)

response = llm.invoke("What is the capital of India?")
print(response)
