from dotenv import dotenv_values
from langchain.llms import OpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler


env_vars = dotenv_values(".env")

apikey = env_vars["OPENAI_API_KEY"]

llm = OpenAI(openai_api_key=apikey, max_tokens=1000, streaming=True,
             callbacks=[StreamingStdOutCallbackHandler()])

llm(
    """
    Was ist 100*100/400*56?
    """)

# llm(
#     """
#     Du bist ein brillanter Mathematiker, der jedes mathematische Problem systematisch lösen kann.
#     Versuche, das folgende Problem zu lösen:
#     Was ist 100*100/400*56
#     """)
