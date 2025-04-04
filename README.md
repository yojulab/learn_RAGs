- Basic settings for connecting dev langGraph Studio for RAG langGraph
- Providing langGraph access via URI  

#### Main package
- python:3.11
- langGraph Studio

#### execute langGraphs
```
~$ cp .env_copy .env
~$ vi .env
OPENAI_API_KEY=<your api key>
~$ langgraph dev --port 8000 --host 127.0.0.1
```
@LangGraph Studio: https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:8000

# Codes Directory Overview

This directory contains various implementations and examples related to the LangChain framework, focusing on integrating language models with databases and other tools for enhanced data retrieval and analysis.

## Directory Structure

### 1. `langChains/`
This folder includes projects that utilize LangChain to interact with SQL databases and generative AI models.

- **`toyproject_agent_prompttomakeSQL.py`**: Demonstrates how to create a SQL agent using LangChain to process natural language queries and convert them into SQL commands. It connects to a SQLite database and showcases various SQL queries.
  
- **`toyproject_gemini_rag.py`**: Implements a RAG (Retrieval-Augmented Generation) approach using Google's Gemini model. It integrates web search and generative AI to answer user queries based on video content analysis.

### 2. `langGraphs/`
This folder contains examples of state graphs built with LangGraph, which facilitate complex workflows involving language models.

- **`example_graph.py`**: Defines a simple state graph with nodes for thinking and responding based on user input. It utilizes a language model to generate responses based on the conversation context.

- **`youtube_rag_graph.py`**: Implements a more complex RAG workflow that analyzes YouTube video content and conducts web research to provide comprehensive answers to user queries.

- **`langgraph.json`**: Configuration file that maps graph names to their respective Python files for easy execution.

### 3. `streamlit_io/`
This folder contains Streamlit applications that allow users to interact with databases using natural language queries.

- **`app_agent_prompttomakeSQL_HF.py`**: A Streamlit app that enables users to query the Chinook music database using natural language. It leverages Hugging Face models to interpret user queries and generate SQL commands.

- **`app_agent_prompttomakeSQL_openAI.py`**: Similar to the above but uses OpenAI's models for processing queries. It provides a user-friendly interface for database interaction.

- **`AI_prompt copy.txt`**: Contains notes and prompts related to the application's functionality and design.

## Usage Instructions

1. **Set Up Environment**: Ensure you have the necessary API keys and dependencies installed.
2. **Run Applications**: Use Streamlit to run the applications in the `streamlit_io` folder to interact with the databases.
3. **Explore Graphs**: Utilize the examples in `langGraphs` to understand how to build and execute state graphs with LangChain.

## Requirements

- Python 3.11+
- Required libraries: `langchain`, `streamlit`, `sqlite3`, `google.generativeai`, etc.
- API keys for OpenAI and Hugging Face (if applicable).

## Conclusion

This directory serves as a resource for exploring the integration of language models with databases and workflows, providing practical examples and applications for developers and data scientists.

