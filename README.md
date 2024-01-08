# learnlangchain
My experiments with langchain

## Prerequisite

Below are just notes of how I got the app setup. Useful for infrequent Python user like me.

### Setup LLM

Since we are using llama2 in this environment, to utilize llm in your local environment, you also need to install
llama2 to be able to run the script.

Check this out to use llama2 locally in no time https://github.com/jmorganca/ollama.

Note that the reason I don't use GPT is because GPT needs to pay, while llama2 is free.

### How to setup the python environment

#### Setup the repo

Assume you just cloned this code, all you need to do is:

```
pipenv install
```

This will get your pipenv environment setup.

#### How lcel_example was setup

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

#### How rag_example was setup

Below is how I  setup rag_example to start with

```
pipenv install langchain
pipenv install docarray
pipenv install tiktoken
pipenv install pydantic==1.10.9 # This is to fix this bug https://stackoverflow.com/questions/76880224/error-using-using-docarrayinmemorysearch-in-langchain-could-not-import-docarray
```

#### Additional tool

To use the super Jupyter notebook and tools, this is certainly a plus

```
pipenv install jupyterlab
```
