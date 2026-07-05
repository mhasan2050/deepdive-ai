import streamlit as st
from graph.workflow import build_research_graph

st.title("DeepDive AI - Multi-Agent Research Assistant")

query = st.text_input("What would you like to research?")

if st.button("Start Research"):
    with st.spinner("Researching..."):
        graph = build_research_graph()
        result = graph.invoke({"query": query})
        st.markdown(result["final_report"])
        st.download_button("Download Report", result["final_report"])
