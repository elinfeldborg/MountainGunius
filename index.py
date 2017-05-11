from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage_html():
    '''This is the start page '''
   return render_template('homepage.html')

@app.route('/stAnton')
def stAnton_html():
   return render_template('stAnton.html')

@app.route('/contact')
def contact_html():
   return render_template('contact.html')

if __name__ == '__main__':
   app.run(debug = True)
