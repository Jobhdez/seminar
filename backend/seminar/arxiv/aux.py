import json
import requests
import xmltodict

def get_research_papers(url):
    """
    Gets the research papers by calling the Arxiv API.
    
    @param url: the URL corresponding to the Arxiv API
    @return: JSON containing the research papers
    """
    response = requests.get(url)
    data_dict = xmltodict.parse(response.text)
    json_data = json.dumps(data_dict)
    json_data = json.loads(json_data)

    return json_data['feed']['entry']
