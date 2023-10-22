from dotenv import load_dotenv
import os
import ads
import requests
from urllib.parse import urlencode
import json

load_dotenv()
API_KEY = os.getenv('ADS_API_KEY')
ads.config.token = API_KEY
r = ads.RateLimits('SearchQuery')

def search_for_papers(search_query):
    papers = ads.SearchQuery(q=search_query)
    titles = []
    bibcodes = []
    for paper in papers:
        titles.append(paper.title)
        bibcodes.append(paper.bibcode)
    return {"titles": titles, "bibcodes": bibcodes}

def get_abstracts(paper_stats):
    custom_format="%B\n"
    # create a dictionary with the payload values
    payload = {'bibcode': paper_stats["bibcodes"],
               'format': custom_format}

    # the json library offers an easy way to convert between JSON or dictionaries and their serialized strings
    serialized_payload = json.dumps(payload)

    results = requests.post("https://api.adsabs.harvard.edu/v1/export/custom", 
                            headers={'Authorization': 'Bearer ' + API_KEY},
                            data=serialized_payload)
    abstract_strings = results.json()['export']
    abstract_array = abstract_strings.split("\n")
    abstract_array = list(filter(None, abstract_array))
    return abstract_array

def get_abstracts_of_query(search_query):
    return get_abstracts(search_for_papers(search_query))
