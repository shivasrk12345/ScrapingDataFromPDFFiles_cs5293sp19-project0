# cs5293sp19-project0
Norman, Oklahoma police department reports of incidents arrests and other activities 
== 
The website contains three types of summaries arrests, incidents, and case summaries.
The main aim of our code is to extract the data from the PDF files in the [oklahoma police department](http://normanpd.normanok.gov/content/daily-activity) and extract the data from PDF and push the data into the sqlite3 database and display a random record which is separated by an *thorn*(þ).

---
#Author
*Siva Rama Krishna Ganta*
Author Email: shivasrk1234@ou.edu
Packages used: urllib, PyPDF2, tempfile, sqlite3, argparse, pandas

---
#Structure 
.
├── COLLABORATORS
├── LICENSE
├── Pipfile
├── Pipfile.lock
├── README.md
├── docs
├── project0
│   ├── main.py
│   └── project0.py
├── setup.cfg
├── setup.py
└── tests
    ├── test_download.py
    └── test_fields.py
 
#Setup Instructions
Installed urllib  package to scrape data from url’s
Installed pypdf2 to extract text from pdf file.
Created database to store the extracted text.
Created cs5293sp19-project0 github repository to store the project0.
We perform cloning to store the data.

*How to Run:*
--
To run this u need to pass the following commands in command line as follows:
python main.py --arrests "pdf url"
`python main.py --arrests " http://normanpd.normanok.gov/filebrowser_download/657/2019-02-18%20Daily%20Arrest%20Summary.pdf"`
output:
retrieves a string in which the fields are separated by thorn(þ)
`2/12/2019 20:11þ2019-00012021þ1330 E LINDSEY STþPUBLIC INTOX / CONSUMING INTOX BEV - SPIRTSþDONALD WAYNE WRIGHTþ5/1/1965þHOMELESSþFDBDC (Jail)þ1632 - Hudson`

----
#External Resources 
https://www.geeksforgeeks.org
http://echrislynch.com/2018/07/13/turning-a-pdf-into-a-pandas-dataframe/
tutorials point
Stackoverflow
---


#Assumptions
This  code is hard coded for solving only the fields which have only the same format as of the pdf files in the  [oklahoma police department](http://normanpd.normanok.gov/content/daily-activity)
By observing all the pdf files , I came to know that empty spaces in the pdf files are  occuring only in the city, sate, zipcode columns only.

So I am assuming that the empty spaces  occur only in the city, sate, zipcode columns .
And the structure of the database is of the form :
`CREATE TABLE arrests (
    arrest_time TEXT,
    case_number TEXT,
    arrest_location TEXT,
    offense TEXT,
    arrestee_name TEXT,
    arrestee_birthday TEXT,
    arrestee_address TEXT,
    status TEXT,
    officer TEXT
);`

---

#Bugs
1. This version only is able to handle two lines in a single cell.
2. All cases that were found with three lines were hardcoded to match the format of the given file.
3. This program can handle only these errors `replace('Officer', 'Officer;').replace(' \n', ' ').replace('\n',',').replace( '- \n', ' ').replace('\nD - DUS','D - DUS')`

---

#Description of the Functions:
Extractincidents(): 
--
This function takes the input from the user and opens the url and reads the data in bytes format and returns it.

---
Fetchincidents():
--
It is used to read data from  downloaded pdf file and extract features from it.
1. In this , we used PYPDF2 module to read data and extract text from pdf file 
2. Performed cleaning on extracted text.
3. Converted the data to dataframe and performed operations and cleaning

---
Createdb():
--
The createdb() function creates an SQLite database file named normanpd.db and inserts a table with the schema below.

CREATE TABLE arrests (
    arrest_time TEXT,
    case_number TEXT,
    arrest_location TEXT,
    offense TEXT,
    arrestee_name TEXT,
    arrestee_birthday TEXT,
    arrestee_address TEXT,
    status TEXT,
    officer TEXT
);

---
Populatedb():
--
The function populatedb(db, incidents) function takes the rows created in the extractincidents() function and adds it to the normanpd.db database.

---
Status():
--
In this function, to check the status of database, we are retrieving random row from the database.


