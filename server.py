
#	For DJ: python "D:\Djinn\Midgard\Geffen\Masters\CMSC 227\Project Code\CheapSQL-master\server.py"



from flask import Flask,render_template,url_for,redirect,jsonify,request

import sys  
#	Change the long DIR to your local setting
# sys.path.append('D:/Djinn/Midgard/Geffen/Masters/CMSC 227/Project Code/CheapSQL-master/scripts')
import SQLValidator as parser

app = Flask(__name__)

@app.route('/')
def index():
	
	return render_template("index.html")

@app.route('/query',methods=['GET','POST'])
def query():

	resp = {}

	query = "INSERT INTO student (birthday, studNO, STUDENTNAME ) VALUES ('1985-12-01','2001-73310','DJ Sarroza')"

	query = request.form.get("query")
	print query

	# Parse the SQL string
	isValidQuery,error = parser.isValidSQL(query)
	
	# If valid SQL, proceed with the query
	if isValidQuery:

		resp["query"] = request.form.get("query")

		resp["columns"] = ["StudNo","StudentName","Birthday","Degree","Major","UnitsEarned"]
		data = []

		for i in range(20):
			row = ["2010-42113","Ivan Marc H. Escamos","1994-06-06","MS Computer Science","Forest Resource Management","0"]
			data.append(row)

		resp["data"] = data
		resp["numrows"] = i+1
		resp["valid_query"] = "True"

	# If not, return the error.
	else:
		error = error.replace("\n","<br />")
		resp["error"] = error

	return jsonify(resp)


if __name__ == '__main__':

	app.run(debug=True,host='0.0.0.0')