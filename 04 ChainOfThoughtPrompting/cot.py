from dotenv import dotenv_values
from langchain.llms import OpenAI

env_vars = dotenv_values(".env")

apikey = env_vars["OPENAI_API_KEY"]

llm = OpenAI(openai_api_key=apikey)

print(llm(
    """
    Fritz hat 20 Äpfel. Er isst drei Stück. Danach kauft er 10 Äpfel dazu. 
    14 verschenkt er an Freunde. Wieviele Äfpel hat er am Ende noch?
    """))

# print(llm(
#     """
#     Steffi hat 10 Birnen. Sie pflückt 8 weitere Birnen vom Baum.
#     Dabei isst sie eine Birne. Danach verschenkt sie 7 Stück an ihre Freunde.
#     Steffi hat 10 Birnen: 10
#     Sie pflückt 8 weitere Birnen vom Baum: 10+8=18
#     Dabei isst sie eine Birne: 18-1=17
#     Danach verschenkt sie 7 Stück an Ihre Freunde: 17-7=10
    
#     Fritz hat 20 Äpfel. Er isst drei Stück. Danach kauft er 10 Äpfel dazu. 
#     14 verschenkt er an Freunde. Wieviele Äpfel hat er am Ende noch?
#     """))