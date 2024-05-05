import requests
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.environ.get("GITHUB_ACCESS_TOKEN")
class GithubSearch:
    def __init__(self):
        pass
    
    def search_github(self, query):     
        base_url = "https://api.github.com"
        endpoint = "/search/code"
        params = {
            "q": f"{query}.csv in:path",
            "per_page": 15,
        }
        headers = {
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"Bearer {api_key}"
        }
        response = requests.get(base_url + endpoint, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data.get("items", [])

    def format_items(self, items):
        formatted_results = []
        for item in items:
            repo = item["repository"]["full_name"]
            subpath = item["path"]
            fullurl = item["html_url"].replace("/blob/", "/raw/")
            
            response = requests.get(fullurl, stream=True)
            if response.status_code == 200:
                lines_count = 0
                content = ''
                for line in response.iter_lines():
                    if lines_count >= 3:
                        break
                    content += line.decode('utf-8', errors="ignore") + "\n"
                    lines_count += 1
            else:
                content = ""
            
            result = {
                "repo": repo,
                "subpath": subpath,
                "fullurl": fullurl,
                "text": content,
            }
            formatted_results.append(result)
        return formatted_results
    
    

