from flask import Flask, render_template
import sqlite3

conn = sqlite3.connect('db/MountainGenius.db')
print ("Opened database successfully");


app = Flask(__name__)

@app.route('/')
def homepage_html():
   return render_template('homepage.html')

@app.route('/homepage')
def homepage__html():
   return render_template('homepage.html')

@app.route('/stAnton')
def stAnton_html():
   return render_template('stAnton.html')

@app.route('/contact')
def contact_html():
   return render_template('contact.html')

<<<<<<< HEAD
@app.route('/test')
def test():
   conn.execute('select * from test')
=======
@app.route('/chamonix')
def chamonix_html():
   return render_template('chamonix.html')

@app.route('/Ischgl')
def Ischgl_html():
   return render_template('Ischgl.html')

@app.route('/mayrhofen')
def mayrhofen_html():
   return render_template('mayrhofen.html')
>>>>>>> origin/master

if __name__ == '__main__':
   app.run(debug = True)

   '''
hej
'''
