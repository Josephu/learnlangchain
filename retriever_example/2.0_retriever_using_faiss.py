from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM
from langchain_community.document_loaders import WebBaseLoader
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain

# Load the source data to be queried on
loader = WebBaseLoader("https://docs.smith.langchain.com/overview")
docs = loader.load()

# Embedding is used to vectorize the documents
embeddings = OllamaEmbeddings(
    model="llama3",
)

# The source data is split into chunks and build into a vector DB
text_splitter = RecursiveCharacterTextSplitter()
documents = text_splitter.split_documents(docs)
# FAISS is a fast vector store from Facebook
# https://github.com/facebookresearch/faiss
vector = FAISS.from_documents(documents, embeddings)

# Create the prompt, llm and setup the dicynebt chain
prompt = ChatPromptTemplate.from_template(
    """Answer the following question based only on the provided context:

<context>
{context}
</context>

Question: {input}"""
)

llm = OllamaLLM(model="llama3")
document_chain = create_stuff_documents_chain(llm, prompt)

# Below is the result if we don't use the retriver chain
from langchain_core.documents import Document

answer = document_chain.invoke(
    {
        "input": "how can langsmith help with testing?",
        "context": [
            Document(page_content="langsmith can let you visualize test results")
        ],
    }
)

print("--- Not using retriever ---")
print(answer)

# Below is the result if we use the retriever chain, which has a vector DB to source data
from langchain.chains import create_retrieval_chain

retriever = vector.as_retriever()
retrieval_chain = create_retrieval_chain(retriever, document_chain)

response = retrieval_chain.invoke({"input": "how can langsmith help with testing?"})
print("--- Using retriever ---")
print(response["answer"])
