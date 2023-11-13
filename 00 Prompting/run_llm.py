from dotenv import dotenv_values
from langchain.llms import OpenAI

env_vars = dotenv_values(".env")

apikey = env_vars["OPENAI_API_KEY"]

llm = OpenAI(openai_api_key=apikey, max_tokens=1000, temperature=2)

print(llm(
    # '''
    # Schreibe ein Gedicht.
    # '''
    # '''
    # Schreibe ein Gedicht über die Seefahrt und erwähne die Mayflower. Mache daraus ein japanisches Gedicht.
    # '''
    # '''
    # Schreibe ein Gedicht über die Seefahrt und erwähne die Mayflower. Schreibe es in einer kurzen typischren japanischen Gedichtsform.
    # '''

    '''
    Schrebe einen Buchtitel für ein Buche über Blumen.
    '''
))
