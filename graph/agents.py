from langgraph.graph import StateGraph, END
from langchain_groq import ChatGroq
from typing import TypedDict, Annotated
import operator
from utils.prompts import PLANNER_PROMPT, RESEARCHER_PROMPT, WRITER_PROMPT, CRITIC_PROMPT
from graph.tools import web_search, scrape_page

llm = ChatGroq(model="llama-3.1-70b-versatile", temperature=0.3)

class ResearchState(TypedDict):
    query: str
    plan: str
    research_data: Annotated[list, operator.add]
    draft: str
    critique: str
    final_report: str

def planner_node(state: ResearchState):
    response = llm.invoke(PLANNER_PROMPT + f"\nQuery: {state['query']}")
    return {"plan": response.content}

def researcher_node(state: ResearchState):
    # Use tools via LLM
    tools = [web_search, scrape_page]
    tool_responses = []
    # For simplicity - in full version use create_react_agent
    for _ in range(3):  # limited iterations
        result = llm.invoke(f"Plan: {state['plan']}\nUse tools to research.")
        tool_responses.append(result.content)
    return {"research_data": tool_responses}

def writer_node(state: ResearchState):
    research_text = "\n\n".join(state['research_data'])
    response = llm.invoke(WRITER_PROMPT + f"\nResearch Data:\n{research_text}")
    return {"draft": response.content}

def critic_node(state: ResearchState):
    response = llm.invoke(CRITIC_PROMPT + f"\nDraft:\n{state['draft']}")
    return {"critique": response.content, "final_report": state['draft']}

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