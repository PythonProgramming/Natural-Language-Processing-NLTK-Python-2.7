import time
import urllib2
from urllib2 import urlopen
import re
import cookielib, urllib2
from cookielib import CookieJar
import datetime
import sqlite3


cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0')]


conn = sqlite3.connect('knowledgeBase.db')
c = conn.cursor()


def createDB():
    c.execute("CREATE TABLE knowledgeBase (unix REAL, datestamp TEXT, namedEntity TEXT, relatedWord TEXT)")  
    c.commit()




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
                    linesOfInterest = re.findall(r'<p>(.*?)</p>',str(linkSource))
                    print 'Content:'
                    for eachLine in linesOfInterest:
                        if '<img width' in eachLine:
                            pass
                        elif '<a href=' in eachLine:
                            pass
                        else:
                            print eachLine

                    time.sleep(1)
                    

        except Exception, e:
            print str(e)

    except Exception,e:
        print str(e)
        pass

createDB()
