from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_template("tell me a short joke about {topic}")
prompt_value = prompt.invoke({"topic": "ice cream"})
model = ChatOllama(model="llama3")
message = model.invoke(prompt_value)
output_parser = StrOutputParser()
result = output_parser.invoke(message)
print(result)
