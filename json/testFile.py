'''
Created on Mar 2, 2013

@author: zhumeiqi
'''
from JsonParser import JsonParser,JsonError
if __name__ == '__main__':
    paser = JsonParser()
    paser2 = JsonParser()
    paser3 = JsonParser()
    paser4 = JsonParser()
    paser.loadJson('test.json')
    d1 = paser.dumpDict()
    paser2.loadDict(d1) 
    paser2.dumpJson('test_r.json')
    paser3.loadJson('test_r.json')
    d3 = paser3.dumpDict()
    print paser.dump()
    print d1
    print d3
   
    pass