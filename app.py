import MySQLdb
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
from flask import Flask, render_template, url_for, request
import re
import random
from Dash_application import create_dash_application
import json
import dash
import dash_cytoscape as cyto
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from graphviz import Digraph
import PyPDF2 as p2
from io import StringIO
import subprocess as sp
import mysql.connector
import pdftitle as pd
from PyPDF2 import PdfFileReader
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
import glob, os
from textblob import TextBlob




app = Flask(__name__)

app.secret_key = 'your secret key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'digitalibrary'

mysqli = MySQL(app)



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/test')
def test():
    return render_template('index.html')

@app.route('/search', methods=['GET','POST'])
def search():
    global string
    if request.method == 'POST':
        """
        message = request.form['papername']
        searching = message
        print(searching)
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="digitalibrary"
        )

        mycursor = mydb.cursor()

        sql = "Select PaperName from cittingpaper where PaperName=%s"
        val1 = (searching,)
        mycursor.execute(sql, val1)
        result = mycursor.fetchone()
        print("Result Value:", result)
        if result == 'None':
            return render_template('index.html', msg="Paper Not Found")
        # print(result)
        name = ''
        if (len(name) > 0):
            name = result[0]

        val = (searching,)

        sql1 = "SELECT CitationContext FROM citationcontext WHERE PaperName=%s"
        mycursor.execute(sql1, val)
        # sql1 = "Select CitationContext from citationcontext  where PaperName='Evaluating the Impact of Cyber Attacks on Missions'"
        citations = mycursor.fetchall()

        #print("Citations", citations)
        print("Length of Citations", len(citations))

        #for sen in citations:
        #   print("sen  :", sen)

        Sentiments = []
        for sen in citations:
            string = ''.join(sen)
            # print("string :", string)
            # print("Sen Type", type(string))
            text = TextBlob(string)
            # print("Text type", type(text))
            pol = text.sentiment.polarity
            Subject = text.sentiment.subjectivity
            # print("\n", sen)
            if pol > 0:
                Sentiments.append("Positive")
                # print("Sentiments    ", result)
            elif pol == 0:
                Sentiments.append("Neutral")
                # print("Sentiments    ", result)
            elif pol < 0:
                Sentiments.append("Negative")

        sql2 = "SELECT ReferencePaper FROM citedpaper WHERE CitingPaperName=%s"
        val2 = (searching,)
        mycursor.execute(sql2, val2)
        # sql1 = "Select CitationContext from citationcontext  where PaperName='Evaluating the Impact of Cyber Attacks on Missions'"
        references = list(mycursor.fetchall())

        print("references :", references)
        print("Sentiments :", Sentiments)
        # print("Length of references", len(references))

     # Code used to Generate Interactive Graph by calling __init__.py file
    paperName=message

    IndexVal = []
    Long = []
    Lat = []
    NodesList = []
    SourceList = []
    TargetList = []
    lastvalofFirstreferenceslist = 0
    NodesList.append(paperName)  # adding Citing Paper 1 to create Node list
    #NodesList.append(paperName2)  # adding Citing Paper 2 to create Node list
    for i in range(len(references)):  # adding Citing Paper 1 references to create Node list
        SourceList.append(1)  # adding Citing Paper 1 Name to create Source For target list
        NodesList.append(references[i])
        TargetList.append(i + 2)  # adding Citing Paper 1 references to create Edges list
        lastvalofFirstreferenceslist = i + 3
    Sourcelength = len(SourceList)
    #SourceList.append(SourceList[Sourcelength - 1])
    #TargetList.append(len(TargetList) + 2)
    for i in range(len(NodesList)):
        #trying=i+1
        #print(type(trying))
        #conval=str(trying)
        IndexVal.append(str(i+1))

    # print(IndexVal)

    for j in range(len(NodesList)):
        n = random.randint(1, 80)
        # print('J',n)
        Long.append(n)
    # print(Long)

    for k in range(len(NodesList)):
        no = random.randint(1, 80)
        # print('val', no)
        Lat.append(-+no)
    # print(Lat)
    """

    paperName = "Systematic diagonal and vertical errors in antisaccades and memory-guided saccades"
    References = [('Abel, L A, & Douglas, J (2007) Effects of age on ',),
                  ('latency and error generation in internally mediated ',),
                  ('saccades Neurobiol Aging, 28(4), 627637 ',), ('This article is licensed under a',),
                  ('Creative Commons Attribution 40 International license',),
                  ('\x0cJournal of Eye Movement Research ',), ('Becker, W (1989) Metrics In R H Wurtz & M E ',),
                  ('Goldberg (Eds), The Neurobiology of Saccadic Eye ',),
                  ('Movements (pp 1368) Amsterdam: Amsterdam ',), ('Bell, A H, Everling, S, & Munoz, D P (2000) ',),
                  ('Influence of Stimulus Eccentricity and Direction on ',),
                  ('Characteristics of Pro and Antisaccades in Non',),
                  ('Human Primates J Neurophysiol, 84, 25952604 ',),
                  ('Dafoe, J M, Armstrong, I T, & Munoz, D P (2007) ',),
                  ('The influence of stimulus direction and eccentricity ',),
                  ('on pro and antisaccades in humans Exp Brain Res, ',),
                  ('Everling, S, & Fischer, B (1998) The antisaccade: a ',),
                  ('review of basic research and clinical studies ',),
                  ('Funahashi, S, Bruce, C J, & GoldmanRakic, P S ',),
                  ('(1990) Visuospatial coding in primate prefrontal ',),
                  ('neurons revealed by oculomotor paradigms J ',), ('Gnadt, J W, Bracewell, R M, & Andersen, R A ',),
                  ('(1991) Sensorimotor transformation during eye ',),
                  ('movements to remembered visual targets Vision Res, ',),
                  ('Goffart, L, Quinet, J, Chavane, F, & Masson, G S ',),
                  ('(2006) Influence of background illumination on ',),
                  ('fixation and visually guided saccades in the rhesus ',), ('monkey Vision Res, 46(12), 149162 ',),
                  ('Gourtzelidis, P, Smyrnis, N, Evdokimidis, I, & Balogh, ',),
                  ('A (2001) Systematic errors of planar arm ',),
                  ('movements provide evidence for space categorization ',),
                  ('effects and interaction of multiple frames of ',), ('reference Exp Brain Res, 139(1), 5969 ',),
                  ('Hallett, P (1978) Primary and secondary saccades ',),
                  ('to goals defined by instructions Vision Res, 18, ',),
                  ('Hallett, P, & Adams, B (1980) The predictability of ',),
                  ('saccadic latency in a novel voluntary oculomotor ',),
                  ('Huttenlocher, J, Hedges, L V, & Duncan, S (1991) ',),
                  ('Categories and particulars: prototype effects in ',),
                  ('estimating spatial location Psychol Rev, 98(3), 352',),
                  ('Hutton, S, & Ettinger, U (2006) The antisaccade task as ',),
                  ('a research tool in psychopathology: a critical review ',),
                  ('Abegg M, Lee H, & Barton J S (2010) ',),
                  ('Systematic bias in antisaccades and memoryguided saccades ',),
                  ('Kapoula, Z (1985) Evidence for a range effect in the ',),
                  ('saccadic system Vision Res, 25(8), 11551157 ',),
                  ('Koehn, J D, Roy, E, & Barton, J J S (2008) The ',),
                  ('‘diagonal effect’: a systematic error in oblique ',),
                  ('antisaccades  J Neurophysiol, 100, 587597 ',), ('Krappmann, P (1998) Accuracy of visually and ',),
                  ('memoryguided antisaccades in man Vision Res, 38, ',),
                  ('Lueck, C, Tanyeri, S, Crawford, T, Henderson, L, ',), ('& Kennard, C (1990) Antisaccades and ',),
                  ('remembered saccades in Parkinson’s disease J ',), ('Neurol Neurosurg Psychiatry, 53, 284288 ',),
                  ('Mantas, A, Evdokimidis, I, & Smyrnis, N (2008) ',),
                  ('Perception action interaction: the oblique effect in the ',),
                  ('evolving trajectory of arm pointing movements Exp ',),
                  ('Munoz, D, & Everling, S (2004) Look away: the anti',),
                  ('saccade task and the voluntary control of eye ',),
                  ('movement Nature Reviews Neurosci, 5, 218228 ',),
                  ('Smyrnis, N, Gourtzelidis, P, & Evdokimidis, I (2000) ',),
                  ('A systematic directional error in 2D arm movements ',),
                  ('increases with increasing delay between visual target ',),
                  ('presentation and movement execution Exp Brain Res, ',),
                  ('Smyrnis, N, Mantas, A, & Evdokimidis, I (2007) ',),
                  ('"Motor oblique effect": perceptual direction ',),
                  ('discrimination and pointing to memorized visual ',),
                  ('targets share the same preference for cardinal ',),
                  ('orientations J Neurophysiol, 97(2), 10681077 ',),
                  ('Stanford, T R, & Sparks, D L (1994) Systematic errors ',),
                  ('for saccades to remembered targets: evidence for a ',),
                  ('dissociation between saccade metrics and activity in ',),
                  ('the superior colliculus Vision Res, 34(1), 93106 ',),
                  ('Tatler, B W, & Hutton, S B (2007) Trial by trial ',),
                  ('effects in the antisaccade task Exp Brain Res, 179(3), ',),
                  ('Theleritis, C, Smyrnis, N, Mantas, A, & Evdokimidis, I ',),
                  ('(2004) The effects of increasing memory load on the ',),
                  ('directional accuracy of pointing movements to ',),
                  ('remembered targets Exp Brain Res, 157(4), 518525 ',),
                  ('Van Beers, R J (2007) The sources of variability in ',),
                  ('saccadic eye movements J Neurosci, 27(33), 8757',), ('This article is licensed under a',),
                  ('Creative Commons Attribution 40 International license',),
                  ('\x0cJournal of Eye Movement Research ',), ('Abegg M, Lee H, & Barton J S (2010) ',),
                  ('Systematic bias in antisaccades and memoryguided saccades ',),
                  ('White, J M, Sparks, D L, & Stanford, T R (1994) ',),
                  ('Saccades to remembered target locations: an analysis ',),
                  ('of systematic and variable errors Vision Res, 34(1), ',), ('This article is licensed under a',),
                  ('Creative Commons Attribution 40 International license',)]
    Sentiments = ['Positive', 'Nuetral', 'Positive', 'Nuetral', 'Negative', 'Negative', 'Nuetral', 'Negative',
                  'Nuetral', 'Negative', 'Positive', 'Negative', 'Nuetral', 'Nuetral', 'Nuetral', 'Nuetral', 'Nuetral',
                  'Nuetral', 'Nuetral', 'Nuetral', 'Nuetral', 'Nuetral', 'Positive', 'Nuetral', 'Positive', 'Negative',
                  'Nuetral', 'Negative', 'Negative', 'Nuetral', 'Nuetral', 'Positive', 'Nuetral', 'Negative', 'Nuetral',
                  'Nuetral', 'Nuetral', 'Nuetral', 'Negative', 'Positive', 'Positive', 'Nuetral', 'Nuetral', 'Negative',
                  'Positive', 'Positive', 'Nuetral', 'Nuetral', 'Negative', 'Nuetral', 'Nuetral', 'Nuetral', 'Positive',
                  'Positive', 'Nuetral', 'Nuetral', 'Nuetral', 'Positive', 'Positive', 'Nuetral', 'Positive', 'Nuetral',
                  'Positive', 'Nuetral', 'Nuetral', 'Nuetral', 'Negative', 'Nuetral', 'Nuetral', 'Positive', 'Negative',
                  'Negative', 'Positive', 'Nuetral', 'Nuetral', 'Positive', 'Positive', 'Nuetral', 'Positive',
                  'Nuetral', 'Nuetral', 'Nuetral', 'Negative', 'Nuetral', 'Nuetral', 'Nuetral', 'Positive', 'Nuetral',
                  'Nuetral', 'Nuetral', 'Nuetral', 'Nuetral', 'Nuetral', 'Nuetral', 'Nuetral', 'Nuetral', 'Negative',
                  'Negative', 'Nuetral', 'Nuetral', 'Nuetral', 'Negative', 'Nuetral', 'Nuetral', 'Nuetral', 'Positive',
                  'Nuetral', 'Nuetral', 'Nuetral', 'Nuetral', 'Nuetral', 'Negative', 'Nuetral', 'Nuetral', 'Nuetral',
                  'Positive', 'Nuetral', 'Nuetral', 'Nuetral', 'Nuetral', 'Nuetral', 'Nuetral', 'Positive', 'Nuetral',
                  'Positive', 'Nuetral', 'Nuetral', 'Positive', 'Nuetral', 'Negative', 'Nuetral', 'Nuetral', 'Nuetral',
                  'Positive', 'Positive', 'Nuetral', 'Positive', 'Nuetral', 'Positive', 'Nuetral', 'Nuetral', 'Nuetral',
                  'Nuetral', 'Positive', 'Nuetral', 'Positive', 'Nuetral', 'Nuetral', 'Nuetral', 'Positive', 'Negative',
                  'Nuetral']

    NodesList = []
    SourceList = []
    TargetList = []
    IndexVal = []
    Long = []
    Lat = []

    lastvalofFirstreferenceslist = 0
    NodesList.append(paperName)  # adding Citing Paper 1 to create Node list
    # NodesList.append(paperName2)    # adding Citing Paper 2 to create Node list
    for i in range(len(References)):  # adding Citing Paper 1 references to create Node list
        SourceList.append(1)  # adding Citing Paper 1 Name to create Source For target list
        NodesList.append(References[i])
        TargetList.append(i + 2)  # adding Citing Paper 1 references to create Edges list
        lastvalofFirstreferenceslist = i + 3
    # Sourcelength=len(SourceList)
    # SourceList.append(SourceList[Sourcelength-1])
    # TargetList.append(len(TargetList)+2)
    for i in range(len(NodesList)):
        IndexVal.append(str(1 + i))

    # print(IndexVal)

    for j in range(len(NodesList)):
        n = random.randint(1, 50)
        # print('J',n)
        Long.append(n)
    # print(Long)

    for k in range(len(NodesList)):
        no = random.randint(1, 50)
        # print('val', no)
        Lat.append(-+no)
    # print(Lat)
    print(len(IndexVal))
    print(len(NodesList))
    print(len(SourceList))
    print(len(TargetList))
    print(len(Sentiments))
    print(len(Long))
    print(len(Lat))

    print(IndexVal)
    print(NodesList)
    print(SourceList)
    print(TargetList)

    dash = create_dash_application(app, IndexVal, NodesList, SourceList, TargetList, Sentiments, Long, Lat)

    # dash=create_dash_application(app)
    @dash.callback(Output('cytoscape-tapNodeData-json', 'children'),
                   Input('cytoscape-event-callbacks-1', 'tapNodeData'))
    def displayTapNodeData(data):
        return json.dumps(data, indent=2)

    return dash.index()

@app.route('/register', methods =['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form :
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cursor = mysqli.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = % s', (username, ))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        elif not username or not password or not email:
            msg = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s, % s)', (username, password, email, ))
            mysqli.connection.commit()
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('register.html', msg = msg)

@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysqli.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = % s AND password = % s', (username, password,))
        account = cursor.fetchone()
        cursor.close()
        if account:
            session['loggedin'] = True
            session['id'] = account['Id']
            session['username'] = account['username']
            msg = 'Logged in successfully !'
            return render_template('Admin.html', msg=msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg=msg)


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/Extract', methods=['GET','POST'])
def Extract():
    if request.method == 'POST':
        message = request.form['message']
        path = message
        os.chdir(path)
        for file in glob.glob("*.pdf"):
            print("\n\n*******************************", file, "************************************")

            #  This is the code to Check Weather the file is Square braces or Auhtor name syntax
            def convert_pdf_to_string(file_path):
                output_string = StringIO()
                with open(file_path, 'rb') as in_file:
                    parser = PDFParser(in_file)
                    doc = PDFDocument(parser)
                    rsrcmgr = PDFResourceManager()
                    device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
                    interpreter = PDFPageInterpreter(rsrcmgr, device)
                    for page in PDFPage.create_pages(doc):
                        interpreter.process_page(page)

                return (output_string.getvalue())

            sen = convert_pdf_to_string(file)
            sen = sen.replace('etc.', ' ')
            sen = sen.replace('e.g.', '')
            sen = sen.replace('i.e.', '')
            # sen=sen.replace('et al.','et  al')
            s = sen.split('.')

            Square = 'False'
            for i in range(len(s)):
                if (bool(re.search(r'\[\d+\]', s[i]))):
                    Square = 'True'
                    break;
            print(Square)

            # -****************** Ended Code for File Syntax Check **********************
            if (Square == 'True'):

                # ***********  This has the code if file is square Braced  ********************

                def convert_pdf_to_string(file_path):

                    output_string = StringIO()
                    with open(file_path, 'rb') as in_file:
                        parser = PDFParser(in_file)
                        doc = PDFDocument(parser)
                        rsrcmgr = PDFResourceManager()
                        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
                        interpreter = PDFPageInterpreter(rsrcmgr, device)
                        for page in PDFPage.create_pages(doc):
                            interpreter.process_page(page)

                    return (output_string.getvalue())

                sen = convert_pdf_to_string(file)
                sen = sen.replace('etc.', ' ')
                sen = sen.replace('e.g.', '')
                sen = sen.replace('i.e.', '')
                # sen=sen.replace('et al.','et  al')
                s = sen.split('.')
                senList = []
                obj = []
                sentiments = []
                result = ""
                occur = 'REFERENCES'
                occur1 = 'References'
                occ='EFERENCES'
                # sentence=[]
                Square = 'False'
                for i in range(len(s)):
                    if (bool(re.search(r'\[\d+\]', s[i]))):
                        Square = 'True'
                        break;
                # print(Square)

                for i in range(len(s)):
                    if '[' in s[i] and ']' in s[i]:
                        if (re.search(occur, s[i]) or re.search(occur1, s[i]) or re.search(occ,s[i])):
                            break;
                        if s[i].index('[') == 0:
                            senList.append(s[i - 1])
                        else:
                            senList.append(s[i])
                refinedCitations = []
                for sen in senList:
                    match = re.findall(r'(?:\A|(?<=.))[^.]*[[0-5][0-9]][^.]*(?:.|\Z)', sen)
                    refinedCitations.append(''.join(match))

                print("***************           Citations     *************************")
                print(type(refinedCitations))
                for cit in refinedCitations:
                    print('\n', cit)
                print("***************           Citations    Ended     *************************")

                # The above code is just for Citations and refining the pure Citation Sentences from the list.

                subpath = (path + file)


                var = subpath

                title = sp.getoutput("pdftitle -p " + var)
                print("title is :",title)

                # title extracting code
                # creationdate = str(info["/CreationDate"])
                # Code for creating Connection between database and application

                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="digitalibrary"
                )

                mycursor = mydb.cursor()

                sql = "INSERT INTO cittingpaper ( PaperName,AuthorName,CreationDate) VALUES (%s, %s ,%s)"
                Val = (title, "Author", "Date")
                mycursor.execute(sql, Val)

                mydb.commit()

                filteredCitations = list(filter(None, refinedCitations))
                for sen in filteredCitations:
                    sql = "INSERT INTO citationcontext ( PaperName,CitationContext, Sentiments, Subjectivity ) VALUES (%s,%s,%s,%s)"

                    text = TextBlob(sen)
                    pol = text.sentiment.polarity
                    Subject = text.sentiment.subjectivity
                    if pol > 0:
                        result = "Positive"
                    elif pol == 0:
                        result = "Neutral"
                    elif pol < 0:
                        result = "Negative"

                    val = (title,sen, result, Subject)
                    mycursor.execute(sql, val)

                    mydb.commit()

                    print(mycursor.rowcount, "record inserted for Citation Context.")
                mydb.close()

                # The below code is just for picking references from the document.

                def convert_pdf_to_string(file_path):
                    output_string = StringIO()
                    with open(file_path, 'rb') as in_file:
                        parser = PDFParser(in_file)
                        doc = PDFDocument(parser)
                        rsrcmgr = PDFResourceManager()
                        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
                        interpreter = PDFPageInterpreter(rsrcmgr, device)
                        for page in PDFPage.create_pages(doc):
                            interpreter.process_page(page)

                    return (output_string.getvalue())

                sen = convert_pdf_to_string(file)
                sen = sen.replace('etc.', ' ')
                sen = sen.replace('e.g.', '')
                sen = sen.replace('.', '')
                sen = sen.replace(':', '')
                s = sen.split('\n')
                References = []
                test = ''
                # or re.search(occur1, s[i])
                occur = "References"
                occur1 = "EFERENCES"
                for n in range(len(s)):
                    # print(s[i])

                    if (re.search(occur, s[n]) or re.search(occur1, s[n])):
                        test = 'true'
                        # senList.append(s[i])
                    if (test == 'true'):
                        #match = re.findall(r'(?:\A|(?<=))[^.]*[[0-5][0-9]][^”]*(?:.|\Z)', s[n], re.MULTILINE)
                        References.append(s[n])
                        # print("Printing in Loop",s[i])

                RefinedReferences = []
                """
                for i in range(0, len(References), 2):
                    RefinedReferences.append(References[i] + References[i + 1])
                  """
                print("\n\n***************          RefinedReferences          ********************")
                RefinedReferences = list(filter(None, References))
                for ref in RefinedReferences:
                    print(ref)
                print(type(RefinedReferences))

                print("***************          References    Ended      ********************")

                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="digitalibrary"
                )
                mycursor = mydb.cursor()
                for o in RefinedReferences:
                  if(len(o)>30):
                    sql = "INSERT INTO citedpaper (CitingPaperName	,ReferencePaper) VALUE (%s,%s)"
                    val = (title,o)
                    mycursor.execute(sql, val)

                    mydb.commit()

                    print(mycursor.rowcount, "record inserted for Cited Paper")
                mydb.close()

                # *************** Ending Code for Square Braces Syntax ********************

            elif Square == 'False':
                # ************** This carries code if The File has Author Name Syntrax *****************

                path = file

                def convert_pdf_to_string(file_path):

                    output_string = StringIO()
                    with open(file_path, 'rb') as in_file:
                        parser = PDFParser(in_file)
                        doc = PDFDocument(parser)
                        rsrcmgr = PDFResourceManager()
                        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
                        interpreter = PDFPageInterpreter(rsrcmgr, device)
                        for page in PDFPage.create_pages(doc):
                            interpreter.process_page(page)

                    return (output_string.getvalue())

                sen = convert_pdf_to_string(path)
                sen = sen.replace('etc.', ' ')
                sen = sen.replace('e.g.', '')
                sen = sen.replace('.', '')
                sen = sen.replace('-', '')
                s = sen.split('\n')
                RefList = []
                obj = []
                sentiments = []
                test = ''
                occur = "References"
                occur1 = 'EFERENCES'
                for i in range(len(s)):
                    # print(s[i])
                    if (re.search(occur, s[i]) or re.search(occur1, s[i])):
                        test = 'true'
                        # senList.append(s[i])
                    if (test == 'true'):
                        # s=sen.replace('.','')
                        RefList.append(s[i])
                        # print("Printing in Loop",s[i])

                print("*********************    references  ********************************")
                for sen in RefList:
                    print('\n', sen)
                print("*********************    references  Ended   ********************************")

                firstKeywords = []
                for sen in RefList:
                    match = re.findall(r'^(.[a-z\s/A-Z]+?),', sen)

                    if len(match) < 10:
                        firstKeywords.append(''.join(match))
                refinedReferences=list(filter(None,RefList))

                def convert_pdf_to_string(file_path):

                    output_string = StringIO()
                    with open(file_path, 'rb') as in_file:
                        parser = PDFParser(in_file)
                        doc = PDFDocument(parser)
                        rsrcmgr = PDFResourceManager()
                        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
                        interpreter = PDFPageInterpreter(rsrcmgr, device)
                        for page in PDFPage.create_pages(doc):
                            interpreter.process_page(page)

                    return (output_string.getvalue())

                sen = convert_pdf_to_string(path)
                sen = sen.replace('etc.', ' ')
                sen = sen.replace('e.g.', '')
                sen = sen.replace('al.', 'al')
                s = sen.split('.')
                Citations = []
                for first in firstKeywords:
                    if first != '':
                        for n in range(len(s)):
                            # print(s[n])
                            # print("Sentences",s[n])
                            if first in s[n]:
                                # print("First name value:",first)
                                # print('\n',s[n])
                                Citations.append(s[n])
                                # print(Citations)
                            # else:
                            #   continue
                """
                print("**********************   Citations *************************")
                # for cit in Citations:
                # print('\n',cit)
                for cit in Citations:
                    print(cit)

                print("**********************   Citations *************************")
                """

                # code for making graph and text analysis
                Sentiments = []
                var = path
                title = sp.getoutput("pdftitle -p" + var)
                print('Title of paper is: ',title)
                if len(title) == 0:
                    title = "No Title"

                # if title
                # print("title :", title)

                # print("Citation Context\n")
                # for Sen in senList:
                # print("\n", Sen)

                # print("References")
                # for o in obj:
                # print("\n", o)

                # print("\n Polarity")
                for sen in Citations:
                    text = TextBlob(sen)
                    pol = text.sentiment.polarity
                    Subject = text.sentiment.subjectivity
                    # print("\n", sen)
                    if pol > 0:
                        Sentiments.append("Positive")
                        # print("Sentiments    ", result)
                    elif pol == 0:
                        Sentiments.append("Nuetral")
                        # print("Sentiments    ", result)
                    elif pol < 0:
                        Sentiments.append("Negative")
                        # print("Sentiments    ", result)

                        # trying to draw the graph using the sentiments and paper Title
                        """
                References = []
                print("References")
                for o in obj:
                    References.append(re.findall(r'([^“]*)”', o))

               """

                # ************** Ended Code for Author name Syntax *****************

                Sentiments = []
                var = path
                title = sp.getoutput("pdftitle -p" + var)
                if len(title) == 0:
                    title = "No Title"

                for sen in Citations:
                    text = TextBlob(sen)
                    pol = text.sentiment.polarity
                    Subject = text.sentiment.subjectivity
                    # print("\n", sen)
                    if pol > 0:
                        Sentiments.append("Positive")
                        # print("Sentiments    ", result)
                    elif pol == 0:
                        Sentiments.append("Neutral")
                        # print("Sentiments    ", result)
                    elif pol < 0:
                        Sentiments.append("Negative")
                        # print("Sentiments    ", result)

                        # trying to draw the graph using the sentiments and paper Title
                        """
                References = []
                print("References")
                for o in obj:
                    References.append(re.findall(r'([^“]*)”', o))

               """

                        # Code for Inserting Records in Database

                        # Code for extracting the metadata of the pdf
                with open(path, 'rb') as f:
                    pdf = PdfFileReader(f)
                    info = pdf.getDocumentInfo()
                    author = info.author
                    creator = info.creator
                    producer = info.producer
                    subject = info.subject
                    # for getting the title of pdf paper using shell command
                    var = path

                    title = sp.getoutput("pdftitle -p " + var)

                    # title extracting code
                    creationdate = str(info["/CreationDate"])
                    # Code for creating Connection between database and application
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="digitalibrary"
                )

                mycursor = mydb.cursor()

                print(type(title))
                print(creationdate)

                sql = "INSERT INTO cittingpaper ( PaperName,AuthorName,CreationDate) VALUES (%s, %s, %s)"
                Val = (title, author, creationdate)
                mycursor.execute(sql, Val)

                mydb.commit()

                print(mycursor.rowcount, "record inserted. for citting paper")

                # Code for inserting the Citation Context

                for sen in Citations:
                    sql = "INSERT INTO citationcontext ( PaperName,CitationContext,Sentiments,Subjectivity ) VALUES (%s, %s, %s, %s)"
                    text = TextBlob(sen)
                    pol = text.sentiment.polarity
                    Subject = text.sentiment.subjectivity
                    if pol > 0:
                        result = "Positive"
                    elif pol == 0:
                        result = "Neutral"
                    elif pol < 0:
                        result = "Negative"

                    val = (title, sen, result, Subject)
                    mycursor.execute(sql, val)

                    mydb.commit()

                    print(mycursor.rowcount, "record inserted for Citation Context.")

                    # Code for inserting the References

                for o in refinedReferences:
                    if len(o) > 30:
                        sql = "INSERT INTO citedpaper (CitingPaperName,ReferencePaper) VALUES (%s,%s)"
                        val = (title,o)
                        mycursor.execute(sql, val)

                        mydb.commit()

                        print(mycursor.rowcount, "record inserted for Cited Paper")

                # Ending code for Insertaion of Data in DB

        """PaperTitle = "Practical attack graph generation for network defense"
        selist = ['Attack Intrusion', 'Intro To Management', 'Final Year Project', 'Block Chain',
                  'Topological analysis of network attack vulnerability', 'Two formal analyses of attack graphs',
                  'An ontology- and Bayesian-based approach for determining threat',
                  'Measuring network security using dynamic Bayesian 4th ACM Workshop of network',
                  'Software Automated Testing', 'Intoduction to Management']
        Sentiments = ['Negative', 'Positive', 'negative', 'Neutral', 'Positive', 'Positive', 'Neutral', 'Positive',
                      'Negative', 'Neutral']
        w = Digraph()
        for Se, senti in zip(selist, Sentiments):
            if senti == 'Negative':
                {
                    w.edge(PaperTitle, Se, color='Red', label=senti)
                }
            elif senti == 'Positive':
                {
                    w.edge(PaperTitle, Se, color='Green', label=senti)
                }
            else:
                w.edge(PaperTitle, Se, color='Black', label=senti)

        u = w.unflatten(stagger=7)
        u.view()
        """
    #msg="Record Inserted Successfully"
    return render_template('Admin.html',prediction="Record Inserted Successfully")