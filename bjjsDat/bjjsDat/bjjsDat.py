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
            innerTables = t.find_all('table')
            if innerTables:
                for innerTable in innerTables:
                    rows = innerTable.findAll(lambda tag: tag.name=='tr')
                    for row in rows:
                        td = row.findAll(lambda tag: tag.name=='td')
                        for t in td:
                            spanElem = t.select('span')
                            if(spanElem):
                                print (spanElem[0])
                            else:                            print (t.renderContents().decode('utf-8').strip())
#print(tables)   

    
