from flask import Flask, render_template
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
mongo = PyMongo(app)
from pymongo import Connection
connection = Connection()
db = connection.test_database
connection = db.test_collection


@app.route('/')
def home_page():
	post = {"author":"Sadat","text":"cats"}
	posts = db.posts
	for post in posts.find():
		return render_template("index.html",name = posts.find())

if __name__=='__main__':  
   app.run(debug=True)
