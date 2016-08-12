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

def get_tables(url):
    result = requests.get(url)
    page = result.text
    doc = soup(page)
    tables = [element.get('style') for element in doc.find_all('table') if element.get('width') == '969' \
    and element.get('border')== '0'] 
    return tables    
    
def getCunLiangFangTable(url=url):
    url = 'http://www.bjjs.gov.cn/tabid/2167/default.aspx'
    result = requests.get(url)
    page = result.text
    doc = soup(page)
    table = doc.find_all('table', attrs={'width': '969' })
    print(table)    

url = 'http://www.bjjs.gov.cn/tabid/2167/default.aspx'
result = requests.get(url)
page = result.text
doc = soup(page)
table = doc.find_all('table', attrs={'width': '969' })
print(table)   

    
if __name__ == '__main__':
        getCunLiangFangTable()
        pass
        print('Links in', url)
        for num, table in enumerate(get_tables(url), start=1):
            print(num, table)
        print()