from flask import Flask,render_template,request
import sys
import sqlite3
import sqlite3 as sql
'''
conn= sqlite3.connect('database.db')
conn.execute('create table books(name TEXT,link text)')
conn.close()

with sql.connect("database.db") as conn:
    cur=conn.cursor()
    cur.execute("insert into books values('A Python Book: Beginning Python, Advanced. Python, and Python Exercises.','https://www.davekuhlman.org/python_book_01.pdf')")
    cur.execute("insert into books values('Python Fundamentals','https://python.cs.southern.edu/pythonbook/pythonbook.pdf')")
    cur.execute("insert into books values('Think Python','https://www.greenteapress.com/thinkpython/thinkpython.pdf')")
    cur.execute("insert into books values('The Ultimate Beginners Guide','http://astronomi.erciyes.edu.tr/wp-content/uploads/astronom/pdf/Python%20-%20Andrew%20Johansen.pdf')")
    conn.commit()
'''
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/books')
def books():
    con=sql.connect("database.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select distinct name,link from books")
    rows=cur.fetchall()
    return render_template('books.html',rows=rows)
@app.route('/payment1')
def payment1():
    return render_template('payment1.html')
@app.route('/payment2')
def payment2():
    return render_template('payment2.html')
@app.route('/payment3')
def payment3():
    return render_template('payment3.html')
@app.route('/payment4')
def payment4():
    return render_template('payment4.html')
@app.route('/view1')
def view1():
    return render_template('view1.html')
@app.route('/view2')
def view2():
    return render_template('view2.html')
@app.route('/view3')
def view3():
    return render_template('view3.html')
@app.route('/view4')
def view4():
    return render_template('view4.html')
@app.route('/unsucessful')
def unsucessful():
    return render_template('unsucessful.html')
@app.route('/nores')
def nores():
    return render_template('nores.html')
if __name__=='__main__':
    app.run()
