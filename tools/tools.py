from langchain_community.tools.tavily_search import TavilySearchResults

def get_profile_url_tavily(name: str):
    """Searches for Linkedin or Twitter Profile Page"""
    search = TavilySearchResults()
    res = search.run(f"{name}")
    return res[0]["url"]

if __name__ == "__main__":
    linkedin_url = get_profile_url_tavily(name="Qiang Cui Linkedin Poppulo")
    print(linkedin_url)