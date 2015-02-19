import time
import re
import datetime
import sqlite3

conn = sqlite3.connect('knowledgeBase.db')
conn.text_factory = str
c = conn.cursor()
visitedLinks = []
wordUsed = 'Americans'
sql = "SELECT * FROM knowledgeBase WHERE namedEntity =?"


def analyze():
    for row in c.execute(sql, [(wordUsed)]):
        print row

analyze()
