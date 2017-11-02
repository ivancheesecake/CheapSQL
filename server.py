
#	For DJ: python "D:\Djinn\Midgard\Geffen\Masters\CMSC 227\Project Code\CheapSQL-master\server.py"



from flask import Flask,render_template,url_for,redirect,jsonify,request

import sys
import shlex

#	Change the long DIR to your local setting
# sys.path.append('D:/Djinn/Midgard/Geffen/Masters/CMSC 227/Project Code/CheapSQL-master/scripts')
#import SQLValidator as parser
import CheapSQLlib as SQL


app = Flask(__name__)

#	Global variables


@app.route('/')
def index():
	
	return render_template("index.html")

@app.route('/query',methods=['GET','POST'])
def query():
	
	resp = {}
	
	query = request.form.get("query")
	
	isValidQuery,checkType,outputList,error = SQL.isValidSQL(query)
	
	
	#print "\n\n isValidQuery : "
	#print isValidQuery
	
	#print "\n\n checkType    : "
	#print checkType
	
	#print "\n\n outputList   : "
	#print "\n"
	#print outputList[0]
	#print "\n"
	#print outputList[1]
	
	#print "\n\n error        : "
	#print error
	
	# If valid SQL, proceed with the query
	
	if isValidQuery:
	#if True:
		
		if checkType == "INSERT":
			# Execute INSERT
			resultFlag,error = SQL.executeInsert(outputList[0],outputList[1])
		elif checkType == "SELECT":
			# Execute SELECT
			selected_columns = list()
			result_list = list()
			resultFlag,selected_columns,result_list,error = SQL.executeSelect(outputList[0],outputList[1],outputList[2])
			
			resp["query"] = request.form.get("query")
			
			columns_list = list()
			for count in range(0,len(selected_columns)):
				columns_list.append(selected_columns[count][1])
				
			resp["columns"] = columns_list
				
			data = []
			
			for count in range(0,len(result_list)):
				#row = ["2010-42113","Ivan Marc H. Escamos","1994-06-06","MS Computer Science","Forest Resource Management","0"]
				row = SQL.semicolonSplit(result_list[count])
				data.append(row)
			
			resp["data"] = data
			resp["numrows"] = count+1
			resp["valid_query"] = "True"			
			
		else:
			print "\nserver.py: [ERROR] Unrecognized query type"
		
		
		#	Dummy shit


	# If not, return the error.
	else:
		print "[server] Invalid Query"
		error = error.replace("\n","<br />")
		resp["error"] = error

	return jsonify(resp)


if __name__ == '__main__':
	print "\t---------------------------------------"
	print "\tStarting CheapSQL Server v0.0.1"
	print "\t(c) 20017"
	print "\t---------------------------------------"
	app.run(debug=True,host='0.0.0.0')