from dotenv import load_dotenv
import os
import ads

load_dotenv()

API_KEY = os.getenv('ADS_API_KEY')
ads.config.token = API_KEY
r = ads.RateLimits('SearchQuery')
papers = ads.SearchQuery(q="Polaris")
paper = list(papers)[0]
for attr in dir(paper):
    print("obj.%s = %r" % (attr, getattr(paper, attr)))
print(list(papers)[0].title)
print(r.limits)