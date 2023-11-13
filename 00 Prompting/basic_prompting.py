from dotenv import dotenv_values
from langchain.llms import OpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler


env_vars = dotenv_values(".env")

apikey = env_vars["OPENAI_API_KEY"]

llm = OpenAI(openai_api_key=apikey, max_tokens=1000, temperature=0.7, streaming=True,
             callbacks=[StreamingStdOutCallbackHandler()])

llm(

    'Schreibe ein Gedicht über die Schraube und erwähne die Firma Würth.'

    # 'Schreibe ein Gedicht über die Schraube und erwähne die Firma Würth. Mache daraus ein japanisches Gedicht.'

    # 'Schreibe ein einzelnes Gedicht in typischer japanischer Kurzgedicht-Form (Haiku) über die Schraube und erwähne die Firma Würth.'
)
