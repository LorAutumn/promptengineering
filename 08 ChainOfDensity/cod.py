import os
from dotenv import dotenv_values
from langchain import LLMChain, PromptTemplate, OpenAI

env_vars = dotenv_values(".env")

apikey = env_vars["OPENAI_API_KEY"]

llm = OpenAI(openai_api_key=apikey, model_name="gpt-4")

with open(r"/Users/lorenz/code/promptengineering/08 ChainOfDensity/article.txt", "r") as f:
    article = f.read()

cod_template = PromptTemplate(
    input_variables=['article'],
    template='''
        Article: {article}
        You will generate increasingly concise entity-dense summaries of the above article. Repeat the following 2 steps 5 times.

        Step 1: Identify 1-3 informative entities (delimited) from the article which are missing from the previously generated summary.
        Step 2: Write a new denser summary of identical length which covers every entity and detail from the previous summary plus the missing entities.

        A missing entity is
        - Relevant: to the main storys.
        - Specific: descriptive yet concise (5 words or fewer).
        - Novel: not in the previous summary.
        - Faithful: present in the article.
        - Anywhere: located in the article.

        Guidelines:
        - The first summary should be long (4-5 sentences, ~80 words), yet highly non-specific, containing little information beyond the entities marked as missing. Use overly verbose language and fillers (e.g., "this article discusses") to reach ~80 words.
        - Make every word count. Rewrite the previous summary to improve flow and make space for additional entities.
        - Make space with fusion, compression, and removal of uninformative phrases like "the article discusses".
        - The summaries should become highly dense and concise, yet self-contained, e.g., easily understood without the article.
        - Missing entities can appear anywhere in the new summary.
        - Never drop entities from the previous summary. If space cannot be made, add fewer new entities.

        Remember: Use the exact same number of words for each summary.
    '''
)

cod_chain = LLMChain(llm=llm, prompt=cod_template, verbose=True)

print(cod_chain.run(article=article))
