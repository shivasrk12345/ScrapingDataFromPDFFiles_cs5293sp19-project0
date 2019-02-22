#from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq
import PyPDF2 as pdf
import tempfile as tf
import pandas as pd
#import re
import sqlite3
def fetchincidents(URL):
    r = ureq(URL).read()
    #print(len(r))
    return r

def extractincidents(text):
    fp=tf.TemporaryFile()
    fp.write(text)
    fp.seek(0)
    pdfReader=pdf.PdfFileReader(fp)
    print('number of pages',pdfReader.getNumPages())
    # Get the first page text
    page1 = pdfReader.getPage(0).extractText()
    # replace space\n with space
    page1=page1.replace(' \n',' ')
    #replace -\n with -
    page1=page1.replace('-\n','-')
    page1=page1.replace('\nD - DUS','D - DUS')
    page1=page1.replace('Officer','Officer;')
    list=page1.split(';')
    #removing trash data
    list=list[:len(list)-1]

    #removing  leading newlines in each string in the list by using strip() function

    for i in range(len(list)):
        list[i]=list[i].strip()
    print(list)
    #converting into list of lists
    Resultlist=[sub.split('\n') for sub in list]
    print(Resultlist)
    for test in Resultlist:
        x=test[-1]
        y=test[-2]
        diff=12-len(test)
        if diff==3:
            test[7]=None
            test[8]=None
            test.append(None)
            test.append(y)
            test.append(x)
            print(test)
            print(len(test))
        elif diff==2:
            test[8]=None
            test[9]=None
            test.append(y)
            test.append(x)
        elif diff==1:
            test[9]=None
            test[10]=y
            test.append(x)
    for i in range(len(Resultlist)):
        print(i,Resultlist[i])
        print(len(Resultlist[i]))

    #creating a dataframe
    df=pd.DataFrame(Resultlist)
    df=df[1:]
    header=['Arrest Date / Time', 'Case Number', 'Arrest Location', 'Offense', 'Arrestee', 'Arrestee Birthday', 'Arrestee Address', 'City', 'State', 'Zip Code', 'Status', 'Officer']
    df.columns=header
    df['arrestee_address']=df.apply(lambda x:'%s_%s_%s_%s' % (x['Arrestee Address'],x['City'],x['State'],x['Zip Code']),axis=1)
    print(df['arrestee_address'])
    listofcolumns=['Arrest Date / Time', 'Case Number', 'Arrest Location', 'Offense', 'Arrestee', 'Arrestee Birthday','arrestee_address','Status', 'Officer']
    finaldf=df[listofcolumns]
    #print(finaldf)
    #print(finaldf['arrestee_address'])
    finaldf['arrestee_address']=finaldf['arrestee_address'].str.replace('_None','')
    #print(finaldf['arrestee_address'])
    for row in finaldf.iterrows():
        print(row)
    #print(finaldf['arrestee_address'])
    return finaldf
# database creation
def createdb():
    conn=sqlite3.connect('normanpd.db')
    c=conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS arrests (
    arrest_time TEXT,
    case_number TEXT,
    arrest_location TEXT,
    offense TEXT,
    arrestee_name TEXT,
    arrestee_birthday TEXT,
    arrestee_address TEXT,
    status TEXT,
    officer TEXT
)""")
    print('db created')
    conn.commit()
    conn.close()
    return 'normanpd.db'
def populatedb(db,incidents):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    for index, row in incidents.iterrows():
        x=(row['Arrest Date / Time'],row['Case Number'],row['Arrest Location'],row['Offense'],row['Arrestee'],row['Arrestee Birthday'],row['arrestee_address'],row['Status'],row['Officer'])
        c.execute('INSERT INTO ARRESTS VALUES(?,?,?,?,?,?,?,?,?)', x)
        conn.commit()
    c.close()
    conn.close()
def status(db):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute('select * from arrests order by random() limit 1')
    result = c.fetchall()
    resultuple=result[0]
    print('þ'.join(resultuple)+';')
    return result
