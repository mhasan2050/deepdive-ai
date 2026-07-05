from tavily import TavilyClient
from langchain.tools import tool
import os

tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def web_search(query: str) -> str:
    """Search the web for up-to-date information."""
    try:
        results = tavily_client.search(query, max_results=8)
        return str(results)
    except Exception as e:
        return f"Search error: {str(e)}"

@tool
def scrape_page(url: str) -> str:
    """Scrape content from a specific webpage."""
    import requests
    from bs4 import BeautifulSoup
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.get_text()[:8000]  # Limit content length
    except Exception as e:
        return f"Scraping error: {str(e)}"