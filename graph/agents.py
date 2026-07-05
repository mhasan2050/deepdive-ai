from langgraph.prebuilt import create_react_agent

planner = create_react_agent(llm, tools=[web_search], system_prompt=PLANNER_PROMPT)
researcher = create_react_agent(llm, tools=[web_search, scrape_page])
writer = create_react_agent(llm, tools=[], system_prompt=WRITER_PROMPT)
