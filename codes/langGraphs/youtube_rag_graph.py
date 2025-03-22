import os
from typing import Dict, List, TypedDict
import json
import logging

# LangChain and LangGraph imports
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.tools import tool
from langchain_core.messages import HumanMessage

# Vector store imports
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_core.documents import Document

# LangGraph imports
from langgraph.graph import StateGraph, END

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# 환경 변수 설정
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
os.environ['TAVILY_API_KEY'] = os.getenv('TAVILY_API_KEY')

# Create web search tool
web_search_tool = TavilySearchResults(k=3)

# Define a more robust version of the YouTube retriever
@tool
def youtube_search_and_retrieve(query: str) -> str:
    """
    Search for YouTube videos and retrieve information about them without transcripts.
    This is a fallback when we can't get transcripts directly.
    """
    try:
        # Use web search to find information about YouTube videos
        search_query = f"{query} YouTube video information"
        search_results = web_search_tool.invoke(search_query)
        
        # Filter results that are likely about YouTube videos
        youtube_results = [
            result for result in search_results 
            if "youtube" in result["url"].lower() or "video" in result["content"].lower()
        ]
        
        if youtube_results:
            return "\n\n".join([
                f"Video Information:\nTitle: {result.get('title', 'Unknown title')}\nURL: {result['url']}\nContent: {result['content']}"
                for result in youtube_results
            ])
        else:
            return f"No YouTube video information found for '{query}'. Using web search results instead:\n\n" + "\n\n".join([
                f"Source: {result['url']}\nTitle: {result['title']}\nContent: {result['content']}"
                for result in search_results[:2]
            ])
    except Exception as e:
        logger.error(f"Error in YouTube search and retrieve: {e}")
        return f"Unable to retrieve YouTube information due to an error. Using web search as fallback for '{query}'."

# Define state schema
class AgentState(TypedDict):
    query: str
    video_analysis: str
    research_results: str
    final_answer: str
    messages: List
    next: str

# Create LLM
llm = ChatOpenAI(model="gpt-4o-mini")

# Define the Video Analysis Agent
def video_analyzer(state: AgentState) -> AgentState:
    query = state["query"]
    
    try:
        # Create prompt for video analyzer
        prompt = f"""You are a Video Analyzer agent.
        Your role is to analyze content about: "{query}"
        Identify main topics, key points, and areas needing further research.
        This is crucial for answering the user's query.
        
        Here is the content from relevant sources:
        """
        
        # Get video information using the fallback tool
        video_content = youtube_search_and_retrieve(query)
        
        # Add video content to prompt
        prompt += f"\n{video_content}\n\n"
        prompt += """Based on this information, please provide:
        1. Main topics covered
        2. Key points for each topic
        3. Questions that need further research to fully answer the user's query
        
        Format your response in a clear, structured manner."""
        
        # Pass to LLM for analysis
        messages = [HumanMessage(content=prompt)]
        response = llm.invoke(messages)
        
        # Update state
        state["video_analysis"] = response.content
        state["messages"] = state.get("messages", []) + messages + [response]
    except Exception as e:
        logger.error(f"Error in video analyzer: {e}")
        state["video_analysis"] = f"Error analyzing video content. Proceeding with web research for: {query}"
    
    # Always proceed to the next step even if there was an error
    state["next"] = "researcher"
    return state

# Define the Web Researcher Agent
def researcher(state: AgentState) -> AgentState:
    query = state["query"]
    video_analysis = state["video_analysis"]
    
    try:
        # Create prompt for researcher
        prompt = f"""You are a Web Researcher agent.
        Your role is to conduct web searches to find information on topics identified from the previous analysis.
        User's query: "{query}"
        
        Here is the previous analysis:
        {video_analysis}
        
        Based on this analysis and the user's query, find additional information that would help provide a comprehensive answer.
        """
        
        # Pass to LLM to decide what to search for
        messages = [HumanMessage(content=prompt)]
        response = llm.invoke(messages)
        
        # Let's search based on the original query
        search_results = web_search_tool.invoke(query)
        
        # Format search results
        formatted_results = "\n\n".join([
            f"Source: {result['url']}\nTitle: {result['title']}\nContent: {result['content']}"
            for result in search_results
        ])
        
        # Create prompt for synthesizing results
        synthesis_prompt = f"""Based on the web search results below, prepare a comprehensive research report that addresses the user's query: "{query}"
        
        Here is the previous analysis that identified knowledge gaps:
        {video_analysis}
        
        Web search results:
        {formatted_results}
        
        Please synthesize this information into a well-structured research report. Include relevant URLs as references."""
        
        # Get synthesis from LLM
        synthesis_messages = [HumanMessage(content=synthesis_prompt)]
        synthesis_response = llm.invoke(synthesis_messages)
        
        # Update state
        state["research_results"] = synthesis_response.content
        state["messages"] = state.get("messages", []) + messages + [response] + synthesis_messages + [synthesis_response]
    except Exception as e:
        logger.error(f"Error in researcher: {e}")
        state["research_results"] = f"Error conducting research. Using available information to generate an answer for: {query}"
    
    # Always proceed to the next step
    state["next"] = "rag_agent"
    return state

# Define the RAG Agent
def rag_agent(state: AgentState) -> AgentState:
    query = state["query"]
    video_analysis = state["video_analysis"]
    research_results = state["research_results"]
    
    try:
        # Create prompt for RAG agent
        prompt = f"""You are a RAG Agent.
        Your role is to answer the user's query based on all available information.
        
        User's query: "{query}"
        
        Here is the content analysis:
        {video_analysis}
        
        Here is the additional research:
        {research_results}
        
        Based on all this information, provide a well-structured, engaging, and concise answer to the user's query.
        Include a title, main content, and references (including URLs when available).
        Consider the user's language preference and provide the answer in the same language as the query.
        
        If you notice the information is incomplete or there were errors in the analysis or research phases,
        please acknowledge this and provide the best possible answer with the available information.
        """
        
        # Get final answer from LLM
        messages = [HumanMessage(content=prompt)]
        response = llm.invoke(messages)
        
        # Update state
        state["final_answer"] = response.content
        state["messages"] = state.get("messages", []) + messages + [response]
    except Exception as e:
        logger.error(f"Error in RAG agent: {e}")
        # Create a basic response if there's an error
        state["final_answer"] = f"""
        # Response to query: {query}
        
        I apologize, but I encountered technical difficulties while processing your request.
        Please try again later or refine your query for better results.
        """
    
    # Always mark as done
    state["next"] = END
    return state

# Build the graph
def build_graph():
    # Create a new graph
    workflow = StateGraph(AgentState)
    
    # Add nodes
    workflow.add_node("video_analyzer", video_analyzer)
    workflow.add_node("researcher", researcher)
    workflow.add_node("rag_agent", rag_agent)
    
    # Add edges directly
    workflow.add_edge("video_analyzer", "researcher")
    workflow.add_edge("researcher", "rag_agent")
    workflow.add_edge("rag_agent", END)
    
    # Set entry point
    workflow.set_entry_point("video_analyzer")
    
    # Compile the graph
    return workflow.compile()

# Function to run the workflow
def run_rag_workflow(query):
    # Build the graph
    graph = build_graph()
    
    # Set initial state
    state = {
        "query": query,
        "video_analysis": "",
        "research_results": "",
        "final_answer": "",
        "messages": [],
        "next": "video_analyzer"
    }
    
    try:
        # Run the graph
        result = graph.invoke(state)
        return result
    except Exception as e:
        logger.error(f"Error running workflow: {e}")
        # Return a basic fallback response if the workflow fails completely
        return {
            "query": query,
            "final_answer": f"I apologize, but I encountered an error while processing your query about '{query}'. Please try again later."
        }

app = build_graph()
# Example usage
if __name__ == "__main__":
    # query = "테디노트는 누구인가요?"
    # result = run_rag_workflow(query)
    # print(result["final_answer"])
    pass