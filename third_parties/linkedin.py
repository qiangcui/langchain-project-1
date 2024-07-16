import os
import requests
from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """scarpe information from LinkedIn profiles, Manually scrape the information from the LinkedIn profile"""
    
    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/qiangcui-poppulo/5d71163dda0b56a96e0eef66675294ba/raw/c73559ee19d92a54bb1603b77336f239dc9258dd/qiang-cui.json"
        response = requests.get(linkedin_profile_url, timeout=10)
    else:
        api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
        headers = {'Authorization': f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
        params = {
            'url': linkedin_profile_url,
        }
        response = requests.get(api_endpoint,
                                params=params,
                                headers=headers,
                                timeout=10)
    
    data = response.json()
    
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")
    
    return data

if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="https://www.linkedin.com/in/qiangcui0618/",
            mock=True
        )
    )