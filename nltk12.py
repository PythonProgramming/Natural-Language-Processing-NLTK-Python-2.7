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

startingWord = 'good'
startingWordVal = -1

synArray = []

def main():
    for startingWord in wordz:
        print 'about to do:',startingWord
        time.sleep(1)
        try:
            page = 'http://thesaurus.com/browse/'+startingWord+'?s=t'
            sourceCode = opener.open(page).read()

            try:
                synoNym = sourceCode.split('<td valign="top">Synonyms:</td>')
                x=1
                while x < len(synoNym):
                    try:
                        synoNymSplit = synoNym[x].split('</span></td>')[0]
                        synoNyms = re.findall(r'\">(\w*?)</a>', synoNymSplit)
                        print synoNyms
                        for eachSyn in synoNyms:
                            query = "SELECT * FROM wordVals WHERE word =?"
                            c.execute(query, [(eachSyn)])
                            data = c.fetchone()

                            if data is None:
                                print 'not here yet, let us add it'
                                c.execute("INSERT INTO wordVals (word, value) VALUES (?,?)",
                                          (eachSyn, startingWordVal))
                                conn.commit()

                            else:
                                print 'word already here!'


                    except Exception, e:
                        print str(e)
                        print 'failed in 3rd try'

                    x+=1

            except Exception, e:
                print str(e)
                print 'failed 2nd try'


        except Exception, e:
            print str(e)
            print 'failed in the main loop'



main()

c.execute("INSERT INTO doneSyns (word, value) VALUES (?)",
          (startingWord))

conn.commit()
