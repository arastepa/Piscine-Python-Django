import sys
import requests
import dewiki 


def makeReq():
    if len(sys.argv) != 2:
        return
    subject = sys.argv[1]
    url = 'https://en.wikipedia.org/w/api.php'

    params = {
        'action': 'parse',
        'page': subject,
        'format': 'json',
        'prop': 'wikitext',
        'redirects': ''
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        raw_wikitext = data['parse']['wikitext']['*']
        text = dewiki.from_string(raw_wikitext).strip()
        file = open(f"{subject.replace(' ', '_')}.wiki", "w")
        file.write(text)

    except (requests.RequestException, KeyError) as e:
        print(e)



if __name__ == '__main__':
    makeReq()
