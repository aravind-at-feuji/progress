from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    model="openai/gpt-oss-120b",
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("HF_TOKEN"),
)

prompt1 = ChatPromptTemplate.from_template(
    """
    Get the important facts about this {name} organisation
    and return them as a list of facts.
    """
)

prompt2 = ChatPromptTemplate.from_template(
    """
    From the following facts:

    {facts}

    Select the 2 most unique facts and return them as a list.
    """
)

prompt3 = ChatPromptTemplate.from_template(
    """
    From these unique facts:

    {facts}

    Generate a short summary of the organisation and
    generate a professional email to the CEO containing the summary.
    """
)

parser = StrOutputParser()

chain1 = prompt1 | llm | parser
chain2 = prompt2 | llm | parser
chain3 = prompt3 | llm | parser

facts = chain1.invoke({
    "name": "Feuji"
})

unique_facts = chain2.invoke({
    "facts": facts
})

result = chain3.invoke({
    "facts": unique_facts
})

print(result)