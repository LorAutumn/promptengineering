from dotenv import dotenv_values
from langchain.llms import OpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler


env_vars = dotenv_values(".env")

apikey = env_vars["OPENAI_API_KEY"]

llm = OpenAI(openai_api_key=apikey, max_tokens=1000, streaming=True,
             callbacks=[StreamingStdOutCallbackHandler()])

llm(
    """
    Eine Konversation zum Thema Nuturwissenschaften:
    Frage: Was ist eine Wasserratte?
    Antwort: Eine Wasserratte ist ein biologisch ungenauer Begriff zur Bezeichnung verschiedener
    Nagetier-Arten, die nicht miteinander verwandt sind.

    Eine Konversation zum Thema Scherzfragen:
    """)
