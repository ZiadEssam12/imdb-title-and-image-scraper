import requests
from bs4 import BeautifulSoup
url = "https://www.imdb.com/title/tt9018736/mediaviewer/rm2739621121"

querystring = {"ref_":"tt_ov_i"}

payload = ""
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "sec-ch-ua": '''"Microsoft Edge";v="123", "Not:A-Brand";v="8", "Chromium";v="123"''',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '''"Windows"''',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"
}

response = requests.get(url, headers=headers, params=querystring)

soup = BeautifulSoup(response.text, 'html.parser')
title=  soup.find('title').getText()
image = soup.find('meta', {'property': 'og:image'}).get('content')
print(title , image)