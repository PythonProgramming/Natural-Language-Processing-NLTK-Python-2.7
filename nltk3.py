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
        page = 'http://feeds.huffingtonpost.com/huffingtonpost/raw_feed'
        sourceCode = opener.open(page).read()
        #print sourceCode

        try:
            titles = re.findall(r'<title>(.*?)</title>',sourceCode)
            links = re.findall(r'<link.*?href=\"(.*?)\"',sourceCode)
            #for title in titles:
                #print title
            for link in links:
                if '.rdf' in link:
                    pass
                else:
                    print 'let\'s visit:', link
                    print ' _____________________________________'
                    linkSource = opener.open(link).read()
                    #content = re.findall(r'<p>(.*?)</p>',linkSource)
                    #content = re.findall(r'<p>((.|\n)*)<p>___</p>',linkSource)
                    content = re.findall(r'<p>(.*?)</p>',linkSource)
                    linesOfInterest = re.findall(r'<p>(.*?)</p>',str(content))
                    print 'Content:'
                    for theContent in content:
                        print theContent

                    time.sleep(3)
                    
                    
        except Exception, e:
            print str(e)
        

    except Exception,e:
        print str(e)
        pass

main()
