import os
import requests
from dotenv import load_dotenv
load_dotenv()

def scrape_linkedin_profile_summary(profile_url: str, mock: bool = True) -> dict:
    if mock:
        api_endpoint = os.getenv("MOCK_LINKEDIN_PROFILE_API_ENDPOINT")
        response = requests.get(api_endpoint)
    else:
        proxycurl_api_key = os.getenv("PROXYCURL_API_KEY")
        headers = {"Authorization": f"Bearer { proxycurl_api_key }"}
        api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
        params = {"linkedin_profile_url": profile_url}
        response = requests.get(api_endpoint, params=params, headers=headers)

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
    print(scrape_linkedin_profile_summary("www.linkedin.com/in/dror-russo-53b70714"))
