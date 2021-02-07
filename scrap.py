from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=5)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'

db = SQLAlchemy(app)

class User(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email



@app.route("/")
def home():
    return render_template('index.html', content="testing")


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)