from tavily import TavilyClient
from langchain.tools import tool

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def web_search(query: str) -> str:
    """Search the web and return results."""
    return tavily.search(query, max_results=10)

@tool
def scrape_page(url: str) -> str:
    """Scrape and clean content from a webpage."""
    # Implement with BeautifulSoup or Firecrawl
    ...
