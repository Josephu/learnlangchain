from langchain_community.retrievers import WikipediaRetriever

retriever = WikipediaRetriever()

docs = retriever.get_relevant_documents(query="HUNTER X HUNTER")

answer = docs[0].metadata  # meta-information of the Document
print(answer)

answer = docs[0].page_content[:400]  # a content of the Document
print(answer)
