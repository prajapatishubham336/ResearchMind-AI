from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient 
import os
from dotenv import load_dotenv
from rich import print

load_dotenv()
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def web_search(query:str)-> str:
    """Search the web for recent add reliable information on a topic. Return Titles, URLs and snnipets."""

    results = tavily.search(query=query, max_results=5)
    out = []
    for r in results["results"]:
        out.append(
            f"title: {r['title']}\n"
            f"URL: {r['url']}\n"
            f"Snippet: {r['content'][:300]}\n")
    return "\n---\n".join(out)

@tool
def Scrape_url(url : str)->str:
    """Scrape and return a clean text content from a given URl for deeper reading."""
    try:
        resp = requests.get(url, timeout=8, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(resp.text, "html.parser")
        for tag in soup(["script","style","nav", "footer"]):
            tag.decompose()
        return soup.get_text(separator=" ", strip = True)[:3000]
    except Exception as e:
        return f"Could not scrape URl: {str(e)}"


print(Scrape_url.invoke("https://www.cricbuzz.com/live-cricket-scores/151532/wi-vs-ind-1st-odi-west-indies-tour-of-india-2026"))