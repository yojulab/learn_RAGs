from langgraph.graph import StateGraph
from typing import Dict, TypedDict, List
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# 상태 정의
class AgentState(TypedDict):
    messages: List[str]
    next_steps: List[str]

from dotenv import load_dotenv
import os

# .env 파일에서 환경 변수 로드
load_dotenv()

# LLM 정의
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    api_key=os.getenv("OPENAI_API_KEY")
)


# 노드 함수 정의
def think(state: AgentState) -> AgentState:
    prompt = PromptTemplate.from_template(
        "Based on the conversation, what should be done next?\n\n{messages}"
    )
    response = llm.invoke(prompt.format(messages="\n".join(state["messages"])))
    state["next_steps"] = [response.content]
    return state

def respond(state: AgentState) -> AgentState:
    prompt = PromptTemplate.from_template(
        "Provide a helpful response based on: {next_steps}"
    )
    response = llm.invoke(prompt.format(next_steps=state["next_steps"]))
    state["messages"].append(f"Assistant: {response.content}")
    return state

# 그래프 정의
graph = StateGraph(AgentState)
graph.add_node("think", think)
graph.add_node("respond", respond)
graph.set_entry_point("think")
graph.add_edge("think", "respond")
graph.add_edge("respond", "think")

# 그래프 컴파일
app = graph.compile()
