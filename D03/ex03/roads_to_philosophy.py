import sys
import requests
from bs4 import BeautifulSoup

def makeRequest(url, titles: list):
    response = requests.get(url)
    response.raise_for_status()
    res = BeautifulSoup(response.text, 'html.parser')
    titles.append(res.title.text)
    div = res.find(id = 'mw-content-text').select("p > a")
    for x in div:
        if x.get('href') != None and x['href'].startswith('/wiki') and \
        not x['href'].startswith('/wiki/Help:') and not x['href'].startswith('/wiki/Wikipedia:'):
            return (x['href'].split('/')[2].replace('_', ' '))
    print('it leads to dead end')
    sys.exit()
def roadsToPhilosophy():
    if len(sys.argv) != 2:
        return
    try:
        titles = []
        subject = sys.argv[1]
        first = subject
        while subject.lower() != 'philosophy':
            url = f"https://en.wikipedia.org/wiki/{subject.replace(' ', '_')}"
            subject = makeRequest(url, titles)
            print(subject)
            if subject in titles:
                print("It leads to an infinite loop !")
                return
        print(f"{len(titles)} roads from {first} to philosophy")

    except requests.exceptions.RequestException as e:
        print("An error occurred during the HTTP request:", e)
        return
    
if __name__ == '__main__':
    roadsToPhilosophy()