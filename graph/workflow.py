from langgraph.graph import StateGraph, END
from typing import TypedDict, List

class ResearchState(TypedDict):
    query: str
    plan: str
    sources: List[dict]
    draft: str
    final_report: str
    critique: str

def build_research_graph():
    workflow = StateGraph(ResearchState)
    
    workflow.add_node("planner", planner_node)
    workflow.add_node("researcher", researcher_node)
    workflow.add_node("writer", writer_node)
    workflow.add_node("critic", critic_node)
    
    # Define edges (loops for critique)
    workflow.set_entry_point("planner")
    workflow.add_edge("planner", "researcher")
    workflow.add_edge("researcher", "writer")
    workflow.add_edge("writer", "critic")
    workflow.add_conditional_edges("critic", should_continue)
    
    return workflow.compile()
