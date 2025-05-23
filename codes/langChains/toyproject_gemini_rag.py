# -*- coding: utf-8 -*-
"""ToyProject_Gemini_RAG.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tRwlVUl4ChkLKc88HJQWLCa5khiNk7FQ

## google 인증
"""

# Install required packages
# !pip install google-generativeai langchain-google-genai python-dotenv

# !pip show google-auth

import os
# from google.colab import userdata
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# # from : https://aistudio.google.com/apikey
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

## 테스트
for m in genai.list_models():
    if "generateContent" in m.supported_generation_methods:
        print(m.name)

model = genai.GenerativeModel("gemini-1.5-flash")

# Commented out IPython magic to ensure Python compatibility.
# %%time
# response = model.generate_content("What is the meaning of life?")
# # response

from langchain_google_genai import ChatGoogleGenerativeAI

os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
result= llm.invoke("Write me a ballad about LangChain")
print(result)
print(20*f'-')
from IPython.display import Markdown
result= llm.invoke("네이버에 대해 보고서를 작성해줘")
print(result.content)

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.document_loaders import PyPDFLoader

loader = PyPDFLoader("codes/langChains/이슈리포트-2022-2호-혁신성장-정책금융-동향.pdf")
pages = loader.load_and_split()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
texts = text_splitter.split_documents(pages)

# texts
print(type(texts))

from langchain_huggingface import HuggingFaceEmbeddings
model_name = "jhgan/ko-sbert-nli"
# model_kwargs = {'device': 'cpu'}
model_kwargs = {}
encode_kwargs = {'normalize_embeddings': True}

os.environ["HF_TOKEN"] = os.getenv("HF_TOKEN")
hf = HuggingFaceEmbeddings(
  model_name=model_name, model_kwargs=model_kwargs, encode_kwargs=encode_kwargs
)

docsearch = Chroma.from_documents(texts, hf)

retriever = docsearch.as_retriever(search_type="mmr", search_kwargs={'k':3,'fetch_k': 10})
retriever.get_relevant_documents("혁신성장 정책금융에 대해서 설명해줘")

from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableMap
template = """Answer the question as based only on the following context:
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

gemini = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature = 0)

chain = RunnableMap({
  "context": lambda x: retriever.get_relevant_documents(x['question']),
  "question": lambda x: x['question']
}) | prompt | gemini

# Markdown(chain.invoke({'question': "혁신성장 정책금융에 대해서 설명해줘"}).content)
# This question cannot be answered from the given source. The provided text discusses innovation growth policy financing, focusing on the ICT industry. It mentions trends and the role of policy financing in supporting these industries. However, no specific question is posed within the provided text.
print(chain.invoke({'question': "혁신 ICT 대해 한국어로 설명"}).content)

