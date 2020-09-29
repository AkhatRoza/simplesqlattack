#!/bin/python3 

import sys
import mysql.connector 

if len(sys.argv)<>2:
    print('Syntax:python testsqlattack.py <userid>')
else:
    mydb=mysql.connector.connect(user='xxxx',password='xxxx',host='127.0.0.1',database='PiDB')
    mycursor=mydb.cursor()
    get_data='Select * From Custom  list WHERE userid="%s"' % (sys.argv[1])
    multicur=mycursor.execute(get_data,multi=True)


    print("Your query:"+get_data)
    print('Results:\n')


    for cur in multicur:
        result=cur.fetchall()
        for row in results:
            if cur.with_rows:
                if len(cur.description)==4:
                    print '['+row[3]+']',row[0]+'/'+row[1],row[2]
                else:
                     print row[0]
         print '____________________________'
    mydb.close()
#import MYSQL libraries -check that there's a signle argument on the call
#verify  PORT USERID and PASSWORD
#Connect the Database which should be in the host machine 
#results being saved in the cursor 
#The printing code is general purpose and includes a loop. This allows for multiple responses in the query. I've coded it to detect four elements in a row and format the output according to our customer data.
#Usage python testsqlattack.py 'accountname" or TRUE#'
#Download symple database from INET or create by your self

 
