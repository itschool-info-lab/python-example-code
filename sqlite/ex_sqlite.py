# -*- coding: utf-8 -*-
import sqlite3

con = sqlite3.connect('example.db')

cur = con.cursor()

# 테이블 생성
cur.execute("CREATE TABLE lang (name, first_appeared)")

# 테이블 데이터 Insert
cur.execute("INSERT INTO lang VALUES ('C', 1972)")

# 테이블 데이터 Multiple Insert
insert_list = [
    ("Fortran", 1957),
    ("Python", 1991),
    ("Go", 2009),
]
cur.executemany("INSERT INTO lang VALUES (?, ?)", insert_list)

# DB Commit
con.commit()

# Select DB:
cur.execute("SELECT * FROM lang")
# One
print(cur.fetchone())
# All
print(cur.fetchall())

# DB Close
con.close()
