from dotenv import load_dotenv

load_dotenv()

from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://docs.smith.langchain.com/overview")

docs = loader.load()

from langchain_community.embeddings import OllamaEmbeddings

embeddings = OllamaEmbeddings()

from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter()
documents = text_splitter.split_documents(docs)
vector = FAISS.from_documents(documents, embeddings)

from langchain.tools.retriever import create_retriever_tool

retriever = vector.as_retriever()
retriever_tool = create_retriever_tool(
    retriever,
    "langsmith_search",
    "Search for information about LangSmith. For any questions about LangSmith, you must use this tool!",
)

from langchain_community.tools.tavily_search import TavilySearchResults

search = TavilySearchResults()
tools = [retriever_tool, search]

from langchain_community.chat_models import ChatOllama

llm = ChatOllama(model="llama2")

from langchain import hub

from langchain.chains import LLMChain
from langchain.agents import LLMSingleActionAgent
from langchain.agents import AgentExecutor
from langchain_core.output_parsers import StrOutputParser

prompt = hub.pull("hwchase17/openai-functions-agent")
llm_chain = LLMChain(llm=llm, prompt=prompt)
output_parser = StrOutputParser()
agent = LLMSingleActionAgent(llm_chain=llm_chain, stop=["Observation:"], output_parser=output_parser)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# from langchain.agents import initialize_agent

# zero_shot_agent = initialize_agent(
#     agent="zero-shot-react-description",
#     tools=tools,
#     llm=llm,
#     verbose=True,
#     max_iterations=3,
# )

# agent_executor = AgentExecutor(
#     agent=zero_shot_agent, tools=tools, verbose=True, return_intermediate_steps=True
# )

answer = agent_executor.invoke({"input": "how can langsmith help with testing?", 'intermediate_steps': []})
print(answer)

answer = agent_executor.invoke({"input": "what is the weather in SF?", 'intermediate_steps': []})

print(answer)
