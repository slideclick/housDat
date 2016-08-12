url = 'http://www.bjjs.gov.cn/tabid/2167/default.aspx'
import requests
from bs4 import BeautifulSoup as soup
import sys
    

url = 'http://www.bjjs.gov.cn/tabid/2167/default.aspx'
result = requests.get(url)
page = result.text
doc = soup(page)
tables = doc.find_all('table', attrs={'width': '969'  ,'cellspacing':"5" ,'cellpadding':"0",  'border':"0"
,'style':'border-left: #DBBF93 solid 1px;\r\n        border-right: #DBBF93 solid 1px;'})
for table in tables:
    rows = table.findAll(lambda tag: tag.name=='tr')
    #print(rows)
    for row in rows:
        td = row.findAll(lambda tag: tag.name=='td')
        for t in td:
            innerTable = t.find_all('table')
            if innerTable:
                print (innerTable)
#print(tables)   

    
