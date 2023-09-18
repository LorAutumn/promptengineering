from dotenv import dotenv_values
from langchain.llms import OpenAI

env_vars = dotenv_values(".env")

apikey = env_vars["OPENAI_API_KEY"]

llm = OpenAI(openai_api_key=apikey)

print(llm(
    """
    Was ist 100*100/400*56?
    """))

print(llm(
    """
    Du bist ein brillanter Mathematiker, der jedes mathematische Problem systematisch lösen kann.
    Versuche, das folgende Problem zu lösen:
    Was ist 100*100/400*56
    """))

UNTERSCHIED ChatGPT und GPT 3.5

print(llm(
    """
    Erzähle etwas über Barcamps.
    """
))

print(llm(
    """
    Als wilder Piratenkapitän hast du die sieben Weltmeere durchquert und dabei so manche Schatztruhe geplündert. Nun ist es an der Zeit, deine einzigartige Sprechweise zu nutzen und deine Antworten in einem deutschen Piraten-Slang zu formulieren. Lass die Worte wie eine salzige Meeresbrise klingen und das Abenteuerlust in deiner Stimme erklingen!
    
    Erzähle etwas über Barcamps.
    """))
