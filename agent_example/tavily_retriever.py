import os

# import getpass
# This will ask your key as a prompt in the terminal.
# If you can load password differently, you can set it directly
# os.environ["TAVILY_API_KEY"] = getpass.getpass()

# Alternatively you can use dotenv to load the key from a file
# You can see more about how to use it from here https://pypi.org/project/python-dotenv/
from dotenv import load_dotenv

load_dotenv()

from langchain.retrievers.tavily_search_api import TavilySearchAPIRetriever

retriever = TavilySearchAPIRetriever(k=3)

answer = retriever.invoke("what year was breath of the wild released?")

print(answer)