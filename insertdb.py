import sqlite3
db=sqlite3.connect("mybookstore.db")
cur=db.cursor()
cur.execute('''DROP TABLE books''')
cur.execute('''CREATE TABLE books (
BookID INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT (50) NOT NULL,
author TET(20),
price REAL);''')
num = int(input("No. of books to be added: "))
for x in range(num):
    
    ttl=input("enter book's title: ")
    aut=input("enter name of author: ")
    pr=float(input("enter price: "))
    sql="INSERT INTO books (title, author, price) VALUES ('"+ttl+"','"+aut+"','"+str(pr)+"');"

    try:
        cur=db.cursor()
        cur.execute(sql)
        db.commit()
        print ("one record added successfully")
    except:
        print ("error in operation")
        db.rollback()
db.close()

