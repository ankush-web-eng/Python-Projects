from langchain_openai import OpenAI
from os import getenv
from dotenv import load_dotenv
import openai

load_dotenv("../.env")
SECRET_KEY = getenv("OPENAI_API_KEY")

# print(SECRET_KEY)

llm = OpenAI(openai_api_key=SECRET_KEY)
print(llm.predict("Translate this text to French: Hello, how are you?"))