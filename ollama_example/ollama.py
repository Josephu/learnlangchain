from langchain_community.llms import Ollama

llm = Ollama(model="llama2")
result = llm.invoke("What is the capital of Australia")
print(result)