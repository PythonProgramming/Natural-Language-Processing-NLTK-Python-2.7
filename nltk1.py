import time
import urllib2
from urllib2 import urlopen
import re
import cookielib, urllib2
from cookielib import CookieJar
import datetime

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

def main():
    try:
        page = 'http://www.huffingtonpost.com/feeds/index.xml'
        sourceCode = opener.open(page).read()
        #print sourceCode

        try:
            titles = re.findall(r'',sourceCode)
            links = re.findall(r'(.*?)',sourceCode)
            for title in titles:
                print title
            for link in links:
                print link
        except Exception, e:
            print str(e)

    except Exception,e:
        print str(e)
        pass

main()
