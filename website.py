from flask import Flask, render_template, request
import json
from bson import json_util
from forms import Query

app = Flask(__name__)
app.config.from_object('config')
from pymongo import Connection
connection = Connection()
db = connection.test_database
posts = db.test_collection
val={}

@app.route('/')
def nav():
	n=1
	return render_template('navigation.html',n=n)

@app.route('/query', methods = ['GET', 'POST']) 
def query(): 
	form = Query() 
	documents = {} 
	posts = db.posts
	if request.method == "POST":
		a=form.query.data
		for cat in posts.find():
			x=cat.keys()
			y=cat.values()
			for i in range(len(x)):
				if x[i]==a:
					k=x[i]
					v=y[i]
					tempDict= {k:v}
					documents.update(tempDict) 
		cursor = posts.find(tempDict) 
		return render_template("index.html", name = documents) 
	return render_template('query.html', form= form)

@app.route('/all')
def all():
	posts = db.posts
	for cat in posts.find():
		x=cat.keys()
		y=cat.values()
		for i in range(len(x)):
			 val.update({x[i] : y[i]})
		json.dumps(val, default=json_util.default)
	return render_template("index.html",name = val)

if __name__=='__main__':  
   app.run(debug=True)

