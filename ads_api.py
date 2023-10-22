from dotenv import load_dotenv
import os
import ads
import requests
from urllib.parse import urlencode
import json

load_dotenv()
API_KEY = os.getenv('ADS_API_KEY')
ads.config.token = "ej3lm4nBdAJ0t9NYJnRGOMaF92fIuo1q7g3d6r5N"
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

    if payload["bibcode"] != [] : 
        # the json library offers an easy way to convert between JSON or dictionaries and their serialized strings
        serialized_payload = json.dumps(payload)
        results = requests.post("https://api.adsabs.harvard.edu/v1/export/custom", 
                                headers={'Authorization': 'Bearer ' + API_KEY},
                                data=serialized_payload)
        abstract_strings = results.json()['export']
        abstract_array = abstract_strings.split("\n")
        abstract_array = list(filter(None, abstract_array))
        return abstract_array
    return []

def get_abstracts_of_query(search_query):
    paper_stats = search_for_papers(search_query)
    return {"abstracts": get_abstracts(paper_stats)}

def summarize_texts(texts, tokenizer, model):
    summaries = []
    for text in texts:
        inputs = tokenizer.encode(text, return_tensors="pt", truncation=True, max_length=1024)
        summary_ids = model.generate(inputs, max_length=150, num_beams=4, length_penalty=2.0, early_stopping=True)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        summaries.append(summary)
        return summaries # just take the first summary
    return summaries

# def get_abstract_summaries_of_query(search_query, tokenizer, model):
#     abstracts_data = get_abstracts_of_query(search_query)
#     abstracts = abstracts_data["abstracts"]
#     summaries = summarize_texts(texts, tokenizer, model)
#     return {"abstract_summaries": summaries}