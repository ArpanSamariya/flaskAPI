import os
from flask import Flask,render_template,request


from flask_sqlalchemy import SQLAlchemy


project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "new.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)
class Data(db.Model):
	email = db.Column(db.String(150),unique=True,nullable=False,primary_key =True)
	password=db.Column(db.String(150),nullable=False)

	def __repr__(self):
		return "<User %r %r>" % (self.email , self.password)


@app.route("/" , methods=["GET","POST"] )
def home():
	if request.form:
		data = Data(email=request.form.get("email"),password=request.form.get("password"))
		db.session.add(data)
		db.session.commit()
	return render_template('home.html')  

if __name__ == "__main__":
	db.create_all()
	app.run(debug = True)