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

