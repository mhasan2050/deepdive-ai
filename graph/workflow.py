from langgraph.graph import StateGraph, END
from langchain_groq import ChatGroq
from typing import TypedDict, Annotated, List
import operator
from utils.prompts import PLANNER_PROMPT, RESEARCHER_PROMPT, WRITER_PROMPT, CRITIC_PROMPT
from graph.tools import web_search, scrape_page

# Initialize LLM (change model if you want)
llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.3)

class ResearchState(TypedDict):
    query: str
    plan: str
    research_data: Annotated[list, operator.add]
    draft: str
    critique: str
    final_report: str

def planner_node(state: ResearchState):
    """Break down the query into a research plan."""
    prompt = PLANNER_PROMPT + f"\n\nUser Query: {state['query']}"
    response = llm.invoke(prompt)
    return {"plan": response.content}

def researcher_node(state: ResearchState):
    """Gather information using tools."""
    research_results = []
    
    # First broad search
    search_result = web_search.invoke(state['plan'])
    research_results.append(f"Search Results:\n{search_result}")
    
    # You can add more targeted searches here later
    return {"research_data": research_results}

def writer_node(state: ResearchState):
    """Synthesize research into a report."""
    research_text = "\n\n".join(state.get("research_data", []))
    prompt = WRITER_PROMPT + f"\n\nResearch Findings:\n{research_text}\n\nOriginal Query: {state['query']}"
    
    response = llm.invoke(prompt)
    return {"draft": response.content}

def critic_node(state: ResearchState):
    """Review and finalize the report."""
    prompt = CRITIC_PROMPT + f"\n\nDraft Report:\n{state['draft']}"
    response = llm.invoke(prompt)
    
    # For now, use draft as final (you can improve this later)
    return {
        "critique": response.content,
        "final_report": state['draft']
    }

def build_research_graph():
    workflow = StateGraph(ResearchState)
    
    workflow.add_node("planner", planner_node)
    workflow.add_node("researcher", researcher_node)
    workflow.add_node("writer", writer_node)
    workflow.add_node("critic", critic_node)

    workflow.set_entry_point("planner")
    workflow.add_edge("planner", "researcher")
    workflow.add_edge("researcher", "writer")
    workflow.add_edge("writer", "critic")
    workflow.add_edge("critic", END)

    return workflow.compile()