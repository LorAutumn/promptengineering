from dotenv import dotenv_values
from langchain.llms import OpenAI

from dotenv import dotenv_values
from langchain.llms import OpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler


env_vars = dotenv_values(".env")

apikey = env_vars["OPENAI_API_KEY"]

# set temperature between 0 and 2 to see effects in outputet creativity

llm = OpenAI(openai_api_key=apikey, max_tokens=1000, temperature=0.7, streaming=True,
             callbacks=[StreamingStdOutCallbackHandler()])

llm(

    '''
    Schrebe einen Buchtitel für ein Buch über die Schraube.
    '''
)
