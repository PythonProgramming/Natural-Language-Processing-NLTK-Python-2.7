from __future__ import division
import sqlite3
import time

conn = sqlite3.connect('knowledgeBase.db')
conn.text_factory = str
c = conn.cursor()

negativeWords = []
positiveWords = []


sql = "SELECT * FROM wordVals WHERE value = ?"


def loadWordArrays():
    for negRow in c.execute(sql, [(-1)]):
        negativeWords.append(negRow[0])
    print 'negative words loaded'

    for posRow in c.execute(sql, [(1)]):
        positiveWords.append(posRow[0])
    print 'positive words loaded'



def testPositiveSentiment():
    readFile = open('positiveSentiment.txt','r').read()
    splitRead = readFile.split('\n')
    totalExamples = len(splitRead)
    posExamplesFound = 0
    
    for eachPosExample in splitRead:
        sentCounter = 0
        for eachPosWord in positiveWords:
            if eachPosWord in eachPosExample:
                sentCounter += 1

        for eachNegWord in negativeWords:
            if eachNegWord in eachPosExample:
                sentCounter -= 1
        #print eachPosExample
        #print sentCounter
        #print '____________________'
        #time.sleep(5)

        if sentCounter > 0:
            posExamplesFound += 1
    print ''
    print '________________________________'
    print ' Positive Sentiment Accuracy Results:'
    print 'found examples:', posExamplesFound
    print 'out of a total:', totalExamples
    print 'postivie accuracy:',posExamplesFound/totalExamples*100
    print '________________________________'



def testNegativeSentiment():
    readFile2 = open('negativeSentiment.txt','r').read()
    splitRead2 = readFile2.split('\n')
    totalExamples = len(splitRead2)
    negExamplesFound = 0
    
    for eachNegExample in splitRead2:
        sentCounter2 = 0
        for eachPosWord in positiveWords:
            if eachPosWord in eachNegExample:
                sentCounter2 += 1

        for eachNegWord in negativeWords:
            if eachNegWord in eachNegExample:
                sentCounter2 -= 8
        #print eachNegExample
        #print sentCounter2
        #print '____________________'
        #time.sleep(5)

        if sentCounter2 < 0:
            negExamplesFound += 1


    print ''        
    print ''
    print ''
    print '________________________________'        
    print ' Negative Sentiment Accuracy Results:'
    print 'found negative examples:', negExamplesFound
    print 'out of a total of :', totalExamples
    print 'negative accuracy:',negExamplesFound/totalExamples*100
    print '________________________________'
    



loadWordArrays()

testPositiveSentiment()
testNegativeSentiment()
