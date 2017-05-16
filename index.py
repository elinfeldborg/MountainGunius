from flask import Flask, render_template
import sqlite3

conn = sqlite3.connect('db/MountainGenius.db')
print ("Opened database successfully");


app = Flask(__name__)

@app.route('/')
def homepage_html():
   return render_template('homepage.html')

@app.route('/stAnton')
def stAnton_html():
   return render_template('stAnton.html')

@app.route('/contact')
def contact_html():
   return render_template('contact.html')

@app.route('/test')
def test():
   conn.execute('select * from test')

if __name__ == '__main__':
   app.run(debug = True)
