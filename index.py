from flask import Flask, render_template

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

@app.route('/chamonix')
def chamonix_html():
   return render_template('chamonix.html')

@app.route('/Ischgl')
def Ischgl_html():
   return render_template('Ischgl.html')

if __name__ == '__main__':
   app.run(debug = True)
