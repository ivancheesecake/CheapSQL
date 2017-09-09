from flask import Flask,render_template,url_for,redirect,jsonify,request
import sql_parser as parser

app = Flask(__name__)

@app.route('/')
def index():
	
	return render_template("index.html")

@app.route('/query',methods=['GET','POST'])
def query():

	resp = {}

	resp["query"] = request.form.get("query")

	resp["columns"] = ["StudNo","StudentName","Birthday","Degree","Major","UnitsEarned"]
	data = []

	for i in range(20):
		row = ["2010-42113","Ivan Marc H. Escamos","1994-06-06","MS Computer Science","Forest Resource Management","0"]
		data.append(row)

	resp["data"] = data
	resp["numrows"] = i+1

	# return "Hello"
	return jsonify(resp)

	# return str(parser.isValidSQL("SELECT studno FROM student"))
	# return render_template("index.html")


if __name__ == '__main__':

	app.run(debug=True,host='0.0.0.0')