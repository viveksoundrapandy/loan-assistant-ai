import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from crewai.tools import BaseTool
from pydantic import Field
from langchain_community.utilities import GoogleSerperAPIWrapper
import certifi
import pdb
import openai
# Set up your SERPER_API_KEY key in an .env file, eg:
SERPER_API_KEY='6cedcb304c1ea70a72239faece6898b57e8da2b6'


load_dotenv()

from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_openai import OpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType

import os

os.environ['OPENAI_API_KEY'] = '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'

# Google search Tool
def search_tool():
    llm = OpenAI(temperature=0)
    search = GoogleSerperAPIWrapper()
    tools = [
        Tool(
            name="Intermediate Answer",
            func=search.run,
            description="useful for when you need to ask with search"
        )
    ]

    self_ask_with_search = initialize_agent(tools, llm, agent=AgentType.SELF_ASK_WITH_SEARCH, verbose=True)
    self_ask_with_search.run("What is the hometown of the reigning men's U.S. Open champion?")

# document retrieval tools
def document_from_web_tool():
    from langchain_community.document_loaders import WebBaseLoader
    from langchain.chains import ConversationalRetrievalChain
    from langchain.memory import ConversationBufferMemory
    from langchain.embeddings import OpenAIEmbeddings
    from langchain.vectorstores import Chroma
    loader = WebBaseLoader("https://www.example.com/")
    docs = loader.load()
    #Use OpenAI embeddings
    embeddings = OpenAIEmbeddings()

    # create a vector database using the sample document
    # and the OpenAI embeddings
    vectordb = Chroma.from_documents(
        documents=docs, embedding=embeddings, persist_directory="chromadb"
    )
    # persist the database to disk for later use
    vectordb.persist()

    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    pdf_chat = ConversationalRetrievalChain.from_llm(OpenAI(temperature=0.8) , vectordb.as_retriever(), memory=memory)
    while True:
        line = input("Enter a question: ")
        if line == "":
            break
        result = pdf_chat({"question": line})
        print(f"Answer: {result['answer']}")

def custom_llm():
    import requests

    # Define the URL
    url = "https://llmproxy.go-yubi.in/chat/completions"

    # Define the headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer sk-2mEkJzmQkToFbmpcmmkL2w"
    }

    # Define the JSON payload
    data = {
        "model": "gpt-4o-(US)",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful math tutor. Guide the user through the solution step by step."
            },
            {
                "role": "user",
                "content": "how can I solve 8x + 7 = -23"
            }
        ]
    }

    # Make the POST request
    response = requests.post(url, headers=headers, json=data)

    # Check the response status and print the result
    if response.status_code == 200:
        res = response.json()
        # import pdb;pdb.set_trace()

        print("Response:", res['choices'][0]['message']['content'])
    else:
        print(f"Error: {response.status_code}")
        print("Response:", response)
# document_from_web_tool()
custom_llm()

