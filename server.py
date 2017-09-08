from flask import Flask,render_template,url_for,redirect,jsonify,request

app = Flask(__name__)

@app.route('/')
def index():
	
	return render_template("index.html")

@app.route('/query',methods=['GET','POST'])
def query():

	resp = {}

	resp["table_name"] = "STUDENT"
	resp["columns"] = ["StudNo","StudentName","Birthday","Degree","Major","UnitsEarned"]
	data = []

	for i in range(10):
		row = {"2010-42113","Ivan Marc H. Escamos","1994-06-06","MS Computer Science","Forest Resource Management","0"}
		data.append(row)

	resp["data"] = data

	# return "Hello"
	return jsonify(resp)	
	# return render_template("index.html")


if __name__ == '__main__':

	app.run(debug=True,host='0.0.0.0')