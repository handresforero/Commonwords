import requests
from bs4 import BeautifulSoup
from collections import Counter
from string import punctuation

r = requests.get("http://en.wikipedia.org/wiki/Wolfgang_Amadeus_Mozart")

soup = BeautifulSoup(r.content)

text = (''.join(s.findAll(text=True))for s in soup.findAll('p'))

c = Counter((x.rstrip(punctuation).lower() for y in text for x in y.split()))

tuplaCommon = tuple(c.most_common())
print (tuplaCommon) # prints most common words staring at most common.