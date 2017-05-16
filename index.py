from flask import Flask, render_template
import sqlite3

conn = sqlite3.connect('db/MountainGenius.db')
print ("Opened database successfully");


app = Flask(__name__)

@app.route('/')
def index_html():
   return render_template('index.html')

if __name__ == '__main__':
   app.run(debug = True)
