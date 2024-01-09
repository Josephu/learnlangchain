# learnlangchain
My experiments with langchain

Below are just notes of how I got the app setup. Useful for infrequent Python user like me.

### Setup LLM

Since we are using llama2 in this environment, to utilize llm in your local environment, you also need to install
llama2 to be able to run the script.

Check this out to use llama2 locally in no time https://github.com/jmorganca/ollama.

Note that the reason I don't use GPT is because GPT needs to pay, while llama2 is free.

## How to setup the python environment

Assume you just cloned this code, all you need to do is:

```
pipenv install
```

This will get your pipenv environment setup.

## Walk through each example

### 1. lcel_example

The content is from https://python.langchain.com/docs/expression_language/get_started.

The goal is to help you see:
1. How to use a prompt to provide a question framework to the llm,
2. Use llm to get your answer to your question
3. Use parser to process output
4. Use a chain to join all your work

#### What is LCEL

LCEL is langchain expression language https://python.langchain.com/docs/expression_language/

It is the language that provides chaining feature to simplify writing an AI application.

#### Setup

I use pipenv to manage my local python environment. Below is how I setup to run lcel_example to start with

```
# pipenv allow you to run a specific virtualenv with a Pipfile and Pipfile.lock
# therefore, you can ensure all package versions you use are locked to this repo
# and you won't polute your local environment
# Gotcha - there are times when pipenv shell cache in wrong state, then you will need to delete your local profile
# some ppl use pipenv --rm, I just delete the profile directly in /Users/<username>/.local/share/virtualenvs/xxx

# This will install libraries you need in the pipenv virtualenv environment and add to Pipfile and Pipfile.lock
pipenv install langchain-core
pipenv install langchain-community

# This will run the terminal within that environment, you can run any commands in the new terminal
pipenv shell

# This is alternatively to above where you can just run directly in the shell
pipenv run python ./lcel_example/0.1_prompty.py
```

### 2. rag_example

The content is from https://python.langchain.com/docs/expression_language/get_started

RAG means retrieval-augmented generation, which means you can introduce additional context into'
the engine for the AI to use to answer the questions

#### Setup

Below is how I setup rag_example to start with

```
pipenv install langchain
pipenv install docarray
pipenv install tiktoken
pipenv install pydantic==1.10.9 # This is to fix this bug https://stackoverflow.com/questions/76880224/error-using-using-docarrayinmemorysearch-in-langchain-could-not-import-docarray
```

### 3. How retriever_example was setup

The content is from https://python.langchain.com/docs/get_started/quickstart

This is similar to previous example, except it provide more details on how to use
a vector store as well as an embedding model.

#### What is embedding model?

For more context read https://stackoverflow.blog/2023/11/09/an-intuitive-introduction-to-text-embeddings/.

In short, it is a tool to transform text into a vector store for AI to be able to 
search efficiently using similarity algorithms.

#### Setup

```
pipenv install faiss-cpu
pipenv install faiss-gpu # Only use this if your local machine has good GPU, I have not tested
```

### 4. agent_example

An agent is a tool manager that manages multiple sources of retrievers and use the right tool for the questions. Before we build agent, it is good to know what retrievers you can use.

Langchain supports a lot of retrievers by default. https://python.langchain.com/docs/integrations/retrievers

The content is from several articles:
1. Tavily Search API: This is a search engine build for AI agents. You will need to get a key, and there is a credit limit before paying https://python.langchain.com/docs/integrations/retrievers/tavily
2. Wikipedia: This do a search to wikipedia to find the closet article using the search string

You can also build your own retriever from your preferred data source

#### Setup

```
pipenv install tavily-python
pipenv install wikipedia
pipenv install langchainhub # This is used to download well written prompts
```

#### Additional tool

To use the super Jupyter notebook and tools, this is certainly a plus

```
pipenv install jupyterlab
```
