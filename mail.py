from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

app.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'mountaingenius17@gmail.com',
	MAIL_PASSWORD = 'elinelinelli'
	)

mail=Mail(app)

@app.route('/')
def footer():
   return render_template('__footer.html')

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

if __name__ == '__main__':
   app.run(debug = True)
