from flask import Flask
app = Flask(__name__)

@app.route('/')
def test_site():
    	import pymongo
	conn=pymongo.Connection()  
	db = client.test_database	
	db.posts
	r=list(db.posts.find())
	r=str(r)
	render_template("temp.html")
	return json(r)

if __name__ == '__main__':
    app.run()
