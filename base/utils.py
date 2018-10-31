import requests
from bs4 import BeautifulSoup as bs

def get_title(url):
    try:
        response=requests.get(url)
    except:
        return False
    code = response.status_code
    if code == 200:
        return bs(response.text,'html.parser').title.text
    else:
        return False
