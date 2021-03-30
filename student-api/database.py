# -*- coding: utf-8 -*-
"""

@author: umutc
"""

import sqlite3

con = sqlite3.connect('database.db') 
cur = con.cursor() 


cur.execute('''DROP TABLE IF EXISTS students ''')

cur.execute('''CREATE TABLE students
             ([id] INTEGER PRIMARY KEY,
              [fname] VARCHAR(20) NOT NULL,
              [lname] VARCHAR(20) NOT NULL, 
              [dob] VARCHAR(10) NOT NULL,
              [amountdue] INTEGER)''')
             
con.commit()