# -*- coding: UTF-8 -*-
# 12345 这里写个中文 abcdefg
# 12345 abcdefg
# http://www.pythontutor.com/ 


# python.exe -m doctest  aTemplate.py # aTemplate.py is argv to doctest.script
# %run aTemplate.py

'''
>>> 1
1
'''
# from __future__ import print_function
import inspect
import sys
import pprint
import functools
import argparse
import re
###############################
PREFIX = ''
def trace(fn):
    """A decorator that prints a function's name, its arguments, and its return
    values each time the function is called. For example,

    @trace
    def compute_something(x, y):
        # function body
    """
    @functools.wraps(fn)
    def wrapped(*args, **kwds):
        global PREFIX
        reprs = [repr(e) for e in args] 
        reprs += [repr(k) + '=' + repr(v) for k, v in kwds.items()]
        log('{0}({1})'.format(fn.__name__, ', '.join(reprs)) + ':')
        PREFIX += '    '
        try:
            result = fn(*args, **kwds)
            PREFIX = PREFIX[:-4]
        except Exception as e:
            log(fn.__name__ + ' exited via exception')
            PREFIX = PREFIX[:-4]
            raise
        # Here, print out the return value.
        log('{0}({1}) -> {2}'.format(fn.__name__, ', '.join(reprs), result))
        return result
    return wrapped

def log(message):
    """Print an indented message (used with trace)."""
    if type(message) is not str:
        message = str(message)
    print(PREFIX + re.sub('\n', '\n' + PREFIX, message))
###############################
#@trace
def _test(fname='null'):
    print('{0} calledBy {1}'.format(inspect.stack()[0][3],inspect.stack()[1][3]))   
###############################
def get_links(url):
    import requests
    from bs4 import BeautifulSoup as soup
    result = requests.get(url)
    page = result.text
    doc = soup(page)
    links = [element.get('href') for element in doc.find_all('a')] 
    return links
    
def getHref(fname='null'):
    for url in fname:
        print('Links in', url)
        for num, link in enumerate(get_links(url), start=1):
            print(num, link)
        print()    
    
    
if __name__ == "__main__":
    regExp=r'\s(\w)+\x20(\w{5})'
    reObj=re.compile(regExp,re.I)
    ####################
    f= open('aTemplate.py',encoding='utf-8')
    txt = f.read()
    lines = txt.split('\r\n')
    #print([ ln for ln in (ln.strip() for ln in lines)])
    f.close()    
    ####################
    mObj = reObj.findall(txt)
    if mObj:
        print(mObj)
    ####################    

    
    f= open('aTemplate.py',encoding='utf-8')
    print(f.readline());
    testRe= f.readline()
    print(testRe,end='');f.close()
    
    ####################

    mObj = reObj.search(testRe)
    if mObj:
        print(mObj.group())
        print(mObj.group(1))
        print(mObj.groups())
    
    #####################
    
    f= open('aTemplate.py','rb')
    print(f.readline());f.close()
    
    for ln in open('aTemplate.py',encoding='utf-8'):
        #print(ln)
        pass# who close it?
    with open('aTemplate.py',encoding='utf-8') as f:
        for ln in f.readlines():
            pass
            
    if len(sys.argv) > 1 :getHref(sys.argv[1:])#not use [1]
       
    import doctest
    doctest.testmod() 
    import unittest #    unittest.main()
    import argparse