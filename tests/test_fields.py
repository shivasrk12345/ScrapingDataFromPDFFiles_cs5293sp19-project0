import pytest
import sqlite3
#import pandas

from project0 import project0
myurl='http://normanpd.normanok.gov/filebrowser_download/657/2019-02-14%20Daily%20Arrest%20Summary.pdf'

def test_extractincidents():
    text = project0.fetchincidents(myurl)
    testdf=project0.extractincidents(text)
    assert len(testdf.columns) == 9
    #assert type(testdf)==pandas.core.frame.DataFrame


db = "normanpd.db"
def test_createdb():
    dbname=project0.createdb()
    assert dbname == db


def test_populatedb():
    sql = sqlite3.connect(db)
    cur = sql.cursor()
    cur.execute('select * from arrests order by random() limit 1')
    result = cur.fetchall()
    assert result is not None

def test_status():
    randomrow=project0.status(db)
    assert type(randomrow)==list
    assert type(randomrow[0])==tuple
    assert len(randomrow[0])>0

