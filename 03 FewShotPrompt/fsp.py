from dotenv import dotenv_values
from langchain.llms import OpenAI

env_vars = dotenv_values(".env")

apikey = env_vars["OPENAI_API_KEY"]

llm = OpenAI(openai_api_key=apikey)

print(llm(
    """
    Es war alles bestens: positiv
    Die Qualität ist okay: neutral
    Ein Teil war beschädigt: negativ
    Ich nutze es jeden Tag:
    """))