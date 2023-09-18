from dotenv import dotenv_values
from langchain.llms import OpenAI

env_vars = dotenv_values(".env")

apikey = env_vars["OPENAI_API_KEY"]

llm = OpenAI(openai_api_key=apikey, max_tokens=1000, temperature=0.7)

print(llm(
    '''
    Fritz hat 20 Äpfel. Er isst drei Stück. Danach kauft er 10 Äpfel dazu. 
    14 verschenkt er an Freunde. Wieviele Äpfel hat er am Ende noch?
    Think step by step.
    '''
))
