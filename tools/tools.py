from langchain_community.tools.tavily_search import TavilySearchResults

def get_profile_url_tavily(name: str):
    """Searches for LinkedIn or Twitter Profile Page"""
    search = TavilySearchResults() #max_results=20
    res = search.run(f"{name}")
    return res