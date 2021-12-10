#import requests
#from bs4 import BeautifulSoup
#from collections import Counter
#from string import punctuation

#r = requests.get("http://en.wikipedia.org/wiki/Wolfgang_Amadeus_Mozart")

#soup = BeautifulSoup(r.content)

#text = (''.join(s.findAll(text=True))for s in soup.findAll('p'))

#c = Counter((x.rstrip(punctuation).lower() for y in text for x in y.split()))
#print (c.most_common()) # prints most common words staring at most common.

import pywebio
from pywebio.input import input, TEXT 
from pywebio.output import put_text, put_html, put_markdown, put_table
from pywebio import start_server
import argparse

def bmi():
    url = input("Ingrese la URL：", type=TEXT)
    #weight = input("Ingrese la URL：")
    
    import requests
    from bs4 import BeautifulSoup
    from collections import Counter
    from string import punctuation
    
    r = requests.get(url)
    
    soup = BeautifulSoup(r.content)
    
    text = (''.join(s.findAll(text=True))for s in soup.findAll('p'))
    
    c = Counter((x.rstrip(punctuation).lower() for y in text for x in y.split()))
    
    common = c.most_common()
    
    for common in common:
        
        put_markdown('# **Resultados**')
        put_text('Prueba solicitada por Woobsing')
        #put_html('<br><br>')
        
        
        #put_markdown('Your BMI: `%.1f`. Category: `%s`' % (BMI, status))
        put_html('<hr>')
        put_table([
        ['Palabras'],
        [c.most_common()],
        ])

        break

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()
    
    start_server(bmi, port=args.port)
    #pywebio.start_server(bmi, port=80)
