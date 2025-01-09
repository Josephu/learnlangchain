from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3")
result = llm.invoke("What is the capital of Australia")
print(result)