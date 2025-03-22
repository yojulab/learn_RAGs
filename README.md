- Basic settings for connecting dev langGraph Studio for RAG langGraph
- Providing langGraph access via URI  

#### Main package
- python:3.11
- mongo:7
- langGraph Studio

ports:
  - "8000:8000"  # LangGraph Studio

#### connect remote Docker container
```
~$ langgraph dev --port 8000 --host 0.0.0.0
```

#### samples
```
~$ cp .env_copy .env
~$ vi .env
OPENAI_API_KEY=<your api key>
```
- @LangGraph Studio: https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:8000

