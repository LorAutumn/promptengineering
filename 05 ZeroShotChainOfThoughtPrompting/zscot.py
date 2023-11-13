from dotenv import dotenv_values
from langchain.llms import OpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler


env_vars = dotenv_values(".env")

apikey = env_vars["OPENAI_API_KEY"]

llm = OpenAI(openai_api_key=apikey, max_tokens=1000, streaming=True,
             callbacks=[StreamingStdOutCallbackHandler()])

llm(
    """
    Fritz hat 20 Äpfel. Er isst drei Stück. Danach kauft er 10 Äpfel dazu.
    14 verschenkt er an Freunde. Wieviele Äfpel hat er am Ende noch?
    """)

# llm(
#     """
#     Fritz hat 20 Äpfel. Er isst drei Stück. Danach kauft er 10 Äpfel dazu.
#     14 verschenkt er an Freunde. Wieviele Äfpel hat er am Ende noch?
#     Denke Schritt für Schritt.
#     """)

# llm(
#     """
#     Fritz hat 20 Äpfel. Er isst drei Stück. Danach kauft er 10 Äpfel dazu.
#     14 verschenkt er an Freunde. Wieviele Äfpel hat er am Ende noch?
#     Think step by step.
#     """)
