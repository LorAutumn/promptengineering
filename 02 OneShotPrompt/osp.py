from dotenv import dotenv_values
from langchain.llms import OpenAI

env_vars = dotenv_values(".env")

apikey = env_vars["OPENAI_API_KEY"]

llm = OpenAI(openai_api_key=apikey)

print(llm(
    """
    Eine Konversation zum Thema Nuturwissenschaften:
    Frage: Was ist eine Wasserratte?
    Antwort: Eine Wasserratte ist ein biologisch ungenauer Begriff zur Bezeichnung verschiedener
    Nagetier-Arten, die nicht miteinander verwandt sind.
    Unter folgendem Link kannst du mehr über dieses Thema erfahren: https://de.wikipedia.org/wiki/Wasserratte

    Eine Konversation zum Thema Scherzfragen:
    """))