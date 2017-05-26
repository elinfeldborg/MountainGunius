from flask import Flask, render_template, request
import sqlite3 as sql
from flask_mail import Mail, Message

app = Flask(__name__, static_url_path = "",static_folder= "")

app.config.update(
	DEBUG=True,
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'mountaingenius17@gmail.com',
	MAIL_PASSWORD = 'elinelinelli'
	)
mail=Mail(app)

@app.route('/')
def index_html():
   return render_template('index.html')

@app.route('/index')
def index_home_html():
   return render_template('index.html')

@app.route('/elements')
def elements_html():
   return render_template('elements.html')

@app.route('/mayrhofen')
def mayrhofen_html():
   return render_template('mayrhofen.html')

@app.route('/stanton')
def stanton_html():
   return render_template('stanton.html')

@app.route('/ischgl')
def ischgl_html():
   return render_template('ischgl.html')

@app.route('/chamonix')
def chamonix_html():
   return render_template('chamonix.html')

@app.route('/alpedhuez')
def alpedhuez_html():
   return render_template('alpedhuez.html')

@app.route('/valthorens')
def valthorens_html():
   return render_template('valthorens.html')

@app.route('/champoluc')
def champoluc_html():
   return render_template('champoluc.html')

@app.route('/sestriere')
def sestriere_html():
   return render_template('sestriere.html')

@app.route('/canazei')
def canazei_html():
   return render_template('canazei.html')

@app.route('/disentis')
def disentis_html():
   return render_template('disentis.html')

@app.route('/davos')
def davos_html():
   return render_template('davos.html')

@app.route('/engelberg')
def engelberg_html():
   return render_template('engelberg.html')

@app.route('/orter_italien')
def orter_italien_html():
   return render_template('orter_italien.html')

@app.route('/orter_frankrike')
def orter_frankrike_html():
   return render_template('orter_frankrike.html')

@app.route('/orter_schweiz')
def orter_schweiz_html():
   return render_template('orter_schweiz.html')

@app.route('/orter_osterrike')
def orter_osterrike_html():
   return render_template('orter_osterrike.html')

@app.route('/thanks',methods = ["GET", "POST"])
def thanks():
   name = request.form["name"],
   email = request.form["email"]
   message = request.form["message"]
   text = "Användare: {}\nE-post: {}\nMeddelande: {}".format(name, email, message)
   msg = Message('Mountain Genius', sender='mountaingenius17@gmail.com', recipients= ['mountaingenius17@gmail.com'])
   msg.body = text
   mail.send(msg)
   return render_template("index.html")

@app.route('/tips',methods = ['POST', 'GET'])
def tips():
   print ("SELECT * FROM tips")
   con = None
   if request.method == 'POST':
      try:
         name = request.form['name']
         destination = request.form['destination']
         text = request.form['text']

         with sql.connect("db/MountainGenius.db") as con:
            cur = con.cursor()

            cur.execute("INSERT INTO tips (name,destination,text) VALUES (?,?,?)",(name,destination,text))

            con.commit()

      except:
         con.rollback()
         print("error in insert operation")

   if con is None:
      con = sql.connect("db/MountainGenius.db")
   con.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("SELECT * FROM tips order by id desc LIMIT 3")

   rows = cur.fetchall();
   con.close()
   return render_template("list.html",rows = rows)

if __name__ == '__main__':
   app.run(debug = True)
