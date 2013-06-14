'''
Created on Mar 1, 2013

@author: zhumeiqi
'''
from JsonParser import JsonParser,JsonError

        
def test_unit(str,Success,msg):
    jpaser=JsonParser()
    try:
        result = jpaser.load(str)
        if jpaser is None:
            if Success == False:
                print 'Test ' + msg + ' Success Result None'
                exit()
            else:
                print 'Test ' + msg + ' Fail Result None'
                exit()
    except JsonError,e:
        result = False;
    if result == True and Success == False:
        print 'Test ' + msg + ' Fail'
        exit()
    if result == False and Success == True:
        print 'Test ' + msg + ' Fail'
        exit()
    print 'Test ' + msg + ' Success'
    #return jpaser._dump_list()
    #jpaser.print_dict()
    return jpaser  
    #return jpaser._dump_list()
    
if __name__ == '__main__':
    #wrong type
#    testdata=13
#    test_unit(testdata,False,'Wrong Type')
    #array only
    testdata=r'''[1]'''
    test_unit(testdata,True,'Array Only')
    testdata=r'''[[["key","key"]]][]'''
    test_unit(testdata,False,'Array With Extra chars')
    #basic key value pair
    testdata=r'''{   "abc"  
    :    "abc"}'''
    test_unit(testdata,True,'key value pair')
    #quotes
    testdata=r'''{"controls": "\b\f\n\r\t"}'''
    test_unit(testdata,True,'Quotes')
    testdata=r'''{"controls": "\b\f\n\r\t\a"}'''
    test_unit(testdata,False,'Wrong quotes')
    #multi array
    testdata=r'''[1,2,3,4,[1,2,3,4]]'''
    test_unit(testdata,True,'multi elment array')
    
   # testdata=r'''{"special":"`1~!@#$%^&*()_+-={':[,]}|;.</>?"}'''
    testdata = r'''
{"root":
[
    "JSON Test Pattern pass1",
    {"object with 1 member":["array with 1 element"]},
    {},
    [],
    -42,
    true,
    false,
    null,
    {
        "integer": 1234567890,
        "real": -9876.543210,
        "e": 0.123456789e-12,
        "E": 1.234567890E+34,
        "":  -23456789012E666,
        "zero": 0,
        "one": 1,
        "space": " ",
        "quote": "\"",
        "backslash": "\\",
        "controls": "\b\f\n\r\t",
        "slash": "/ & \/",
        "alpha": "abcdefghijklmnopqrstuvwyz",
        "ALPHA": "ABCDEFGHIJKLMNOPQRSTUVWYZ",
        "digit": "0123456789",
        "special": "`1~!@#$%^&*()_+-={':[,]}|;.</>?",
        "hex": "\u0123\u4567\u89AB\uCDEF\uabcd\uef4A",
        "true": true,
        "false": false,
        "null": null,
        "array":[  ],
        "object":{  },
        "address": "50 St. James Street",
        "url": "http://www.JSON.org/",
        "comment": "// /* <!-- --",
        "# -- --> */": " ",
        " s p a c e d " :[1,2 , 3

,

4 , 5        ,          6           ,7        ],
        "compact": [1,2,3,4,5,6,7],
        "jsontext": "{\"object with 1 member\":[\"array with 1 element\"]}",
        "\/\\\"\uCAFE\uBABE\uAB98\uFCDE\ubcda\uef4A\b\f\n\r\t`1~!@#$%^&*()_+-=[]{}|;:',./<>?"
: "A key can be any string"
    },
    0.5 ,98.6
,
99.44
,

1066


,"rosebud"]}
'''
    paser = JsonParser()
    paser.load(testdata)
    d = paser.dumpDict()
    print d
    pass