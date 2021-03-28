# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 14:06:13 2021

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