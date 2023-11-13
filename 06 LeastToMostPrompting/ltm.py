from dotenv import dotenv_values
from langchain.llms import OpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler


env_vars = dotenv_values(".env")

apikey = env_vars["OPENAI_API_KEY"]

llm = OpenAI(openai_api_key=apikey, max_tokens=1000, streaming=True,
             callbacks=[StreamingStdOutCallbackHandler()])

llm(

    '''
Q: denken, Maschine
A: ne

Q: lernen, Bewertung, Schlafen
A: ngn

Q: künstliche, Intelligenz
A: ez

Q: Transformer, Sprache, Vision
A: ren

Q: Löw, Menü, Bar, Brot, Tisch, Brei, Kalt, Fax, Reim, Sofa, Party, Brief, Apfel, Kino, Interview, Käse, Motor
A:
'''

    # 2. Attempt. Chain of thought prompt -> too complex

    #     '''
    # Q: denken, Maschine
    # A: Der letzte Buchstabe von "denken" ist "n". Der letzte Buchstabe von "Maschine" ist "e". Also ergibt "denken, Maschine" "ne".

    # Q: lernen, Bewertung, Schlafen
    # A: Der letzte Buchstabe von "lernen" ist "n". Der letzte Buchstabe von "Bewertung" ist "g". Der letzte Buchstabe von "Schlafen" ist "n". Also ergibt "lernen, Bewertung, Schlafen" "ngn".

    # Q: künstliche, Intelligenz
    # A: Der letzte Buchstabe von "künstliche" ist "e". Der letzte Buchstabe von "Intelligenz" ist "z". Also ergibt "künstliche, Intelligenz" "ez".

    # Q: Transformer, Sprache, Vision
    # A: Der letzte Buchstabe von "Transformer" ist "r". Der letzte Buchstabe von "Sprache" ist "e". Der letzte Buchstabe von "Vision" ist "n". Also ergibt "Transformer, Sprache, Vision" "ren".

    # Q: Löw, Menü, Bar, Brot, Tisch, Brei, Kalt, Fax, Reim, Sofa, Party, Brief, Apfel, Kino, Interview, Käse, Motor
    # A:
    # '''

    # 3. attempt: least to most -> removing complexity by splitting task into subtasks and concatenating results

    # '''
    # Q: denken, Maschine, lernen
    # A: Der letzte Buchstabe von "denken" ist "n". Der letzte Buchstabe von "Maschine" ist "e". Durch das Verbinden von "n" und "e" erhält man "ne".
    #     Der letzte Buchstabe von "lernen" ist "n". Durch das Verbinden von "ne" und "n" erhält man "nen". Also ergibt "denken, Maschine, lernen" "nen"

    # Q: künstliche, Intelligenz, Transformer
    # A: Der letzte Buchstabe von "künstliche" ist "e". Der letzte Buchstabe von "Intelligenz" ist "z". Durch das Verbinden von "e" und "z" erhält man "ez".
    #    Der letzte Buchstabe von "Transformer" ist "r". Durch das Verbinden von "ez" und "r" erhält man "ezr". Also ergubt "künstliche, Intelligenz, Transformer" "ezr".

    # Q: Löw, Menü, Bar, Brot, Tisch, Brei, Kalt, Fax, Reim, Sofa, Party, Brief, Apfel, Kino, Interview, Käse, Motor
    # A:
    # '''

)
