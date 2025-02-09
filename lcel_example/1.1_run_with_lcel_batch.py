# https://python.langchain.com/docs/expression_language/get_started

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

prompt = ChatPromptTemplate.from_template("tell me a short joke about {topic}")
model = ChatOllama(model="llama3")
output_parser = StrOutputParser()

# this is using the LCEL (Langchain Expression Language)
# see more here https://python.langchain.com/docs/expression_language/get_started
chain = prompt | model | output_parser

# you can use batch to run two topics at the same time
result = chain.batch([{"topic": "ice cream"}, {"topic": "koala"}])

print(result)
# "Why don't ice creams ever get invited to parties?\n\nBecause they always drip when things heat up!"
