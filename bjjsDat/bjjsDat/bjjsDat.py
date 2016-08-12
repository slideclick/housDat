url = 'http://www.bjjs.gov.cn/tabid/2167/default.aspx'
import requests
from bs4 import BeautifulSoup as soup
import sys
def get_links(url):
    import requests
    from bs4 import BeautifulSoup as soup
    result = requests.get(url)
    page = result.text
    doc = soup(page)
    links = [element.get('href') for element in doc.find_all('a')] 
    return links

if __name__ == '__main__':
        print('Links in', url)
        for num, link in enumerate(get_links(url), start=1):
            print(num, link)
        print()