from flask import Flask, render_template
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

@app.route('/query', methods=['GET','POST'])
def query():
	form = Query()
	return render_template('query.html', form = form)

@app.route('/')
def home_page():
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

