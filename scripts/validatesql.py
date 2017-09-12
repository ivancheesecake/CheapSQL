
#	------------------------------------------------------
#python "D:\Djinn\Midgard\Geffen\Masters\CMSC 227\Project Code\CheapSQL-master\scripts\validatesql.py"
#	------------------------------------------------------

import shlex
import sys
from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree


#	------------------------------------------------------
#	Global variables
_install_dir = "D:\\Djinn\\Midgard\\Geffen\\Masters\\CMSC 227\\Project Code\\"

#	------------------------------------------------------

def loadTables(loc):
	return_list = list()
	if loc == "ALL_TABLES":
		
		return_list.append(("STUDENT","STUDENT","STUDENT_SCHEMA"))
		return_list.append(("STUDENTHISTORY","STUDENTHISTORY","STUDENTHISTORY_SCHEMA"))
		return_list.append(("COURSE", "COURSE", "COURSE_SCHEMA"))
		return_list.append(("COURSEOFFERING","COURSEOFFERING","COURSEOFFERING_SCHEMA"))
		return_list.append(("STUDCOURSE","STUDCOURSE","STUDCOURSE_SCHEMA"))
		
	elif loc == "STUDENT":
		return_list.append(("STUDENT","STUDENT","STUDENT_SCHEMA"))
	elif loc == "STUDENTHISTORY":
		return_list.append(("STUDENTHISTORY","STUDENTHISTORY","STUDENTHISTORY_SCHEMA"))
	elif loc == "COURSE":
		return_list.append(("COURSE", "COURSE", "COURSE_SCHEMA"))
	elif loc == "COURSEOFFERING":
		return_list.append(("COURSEOFFERING","COURSEOFFERING","COURSEOFFERING_SCHEMA"))
	elif loc == "STUDCOURSE":
		return_list.append(("STUDCOURSE","STUDCOURSE","STUDCOURSE_SCHEMA"))
	return return_list

#	------------------------------------------------------

def loadSchema(loc, withFlags):
	return_list = list()
	if withFlags:
		if loc == "ALL_TABLES":
			return_list.append(("STUDENT","STUDNO",False))
			return_list.append(("STUDENT","STUDENTNAME",False))
			return_list.append(("STUDENT","BIRTHDAY",False))
			return_list.append(("STUDENT","DEGREE",False))
			return_list.append(("STUDENT","MAJOR",False))
			return_list.append(("STUDENT","UNITSEARNED",False))
			return_list.append(("STUDENTHISTORY","STUDNO",False))
			return_list.append(("STUDENTHISTORY","DESCRIPTION",False))
			return_list.append(("STUDENTHISTORY","ACTION",False))
			return_list.append(("STUDENTHISTORY","DATEFILED",False))
			return_list.append(("STUDENTHISTORY","DATERESOLVED",False))
			
			
		elif loc == "STUDENT":
			return_list.append(("STUDENT","STUDNO",False))
			return_list.append(("STUDENT","STUDENTNAME",False))
			return_list.append(("STUDENT","BIRTHDAY",False))
			return_list.append(("STUDENT","DEGREE",False))
			return_list.append(("STUDENT","MAJOR",False))
			return_list.append(("STUDENT","UNITSEARNED",False))
		
		elif loc == "STUDENTHISTORY":
			return_list.append(("STUDENTHISTORY","STUDNO",False))
			return_list.append(("STUDENTHISTORY","DESCRIPTION",False))
			return_list.append(("STUDENTHISTORY","ACTION",False))
			return_list.append(("STUDENTHISTORY","DATEFILED",False))
			return_list.append(("STUDENTHISTORY","DATERESOLVED",False))
			
	else:
		if loc == "ALL_TABLES":
			return_list.append(("STUDENT","STUDNO"))
			return_list.append(("STUDENT","STUDENTNAME"))
			return_list.append(("STUDENT","BIRTHDAY"))
			return_list.append(("STUDENT","DEGREE"))
			return_list.append(("STUDENT","MAJOR"))
			return_list.append(("STUDENT","UNITSEARNED"))
			return_list.append(("STUDENTHISTORY","STUDNO"))
			return_list.append(("STUDENTHISTORY","DESCRIPTION"))
			return_list.append(("STUDENTHISTORY","ACTION"))
			return_list.append(("STUDENTHISTORY","DATEFILED"))
			return_list.append(("STUDENTHISTORY","DATERESOLVED"))
			
		elif loc == "STUDENT":
			return_list.append(("STUDENT","STUDNO"))
			return_list.append(("STUDENT","STUDENTNAME"))
			return_list.append(("STUDENT","BIRTHDAY"))
			return_list.append(("STUDENT","DEGREE"))
			return_list.append(("STUDENT","MAJOR"))
			return_list.append(("STUDENT","UNITSEARNED"))
		
		elif loc == "STUDENTHISTORY":
			return_list.append(("STUDENTHISTORY","STUDNO"))
			return_list.append(("STUDENTHISTORY","DESCRIPTION"))
			return_list.append(("STUDENTHISTORY","ACTION"))
			return_list.append(("STUDENTHISTORY","DATEFILED"))
			return_list.append(("STUDENTHISTORY","DATERESOLVED"))
			
	return return_list

#	------------------------------------------------------
	
def isValidAlias(candidate):
	#check for special characters and shit
	return True

#	------------------------------------------------------

def isValidTerm(someTerm):

	return True

#	------------------------------------------------------

def isValidTables(tables_string, selected_tables):

	#load tables
	table_list = loadTables("ALL_TABLES")
	
	
	#----------------------------------------------------

	isValid = False
	state = 0
	
	lexer = shlex.shlex(tables_string, posix=True)
	#lexer.whitespace += ','
	lexer_list = list(lexer)
	
	for i in range(0, len(lexer_list) ):
	#print lexer_list[i]
	
		if state == 0:
			table_alias = lexer_list[i].upper()
			result = next((i for i, v in enumerate(table_list) if v[0].upper() == table_alias), -1)
			
			if result != -1 :
				selected_tables.append(table_list[result])
				state = 1
			else:
				print "\n[ERROR] Expected a valid target table. Read the goddamn schema man, what the hell is " + str(lexer_list[i].upper()) + "?"
				return False
		
		#Check for comma or AS
		elif state == 1:
			if lexer_list[i] == ",":
				
				state = 0
			elif lexer_list[i].upper() == "AS":
				state = 2
			else:
				print "\n[ERROR] Expected ',' or AS keyword, but instead we got this shit : " + str(lexer_list[i].upper())
				return False
		
		#Check for the actual table
		elif state == 2:
			candidate_alias = lexer_list[i].upper()
			#check if alias is an existing alias or table name
			if isValidAlias(candidate_alias) :
			
				temp_tuple = selected_tables[-1]
				
				temp_t0 = candidate_alias
				temp_t1 = temp_tuple[1]
				temp_t2 = temp_tuple[2]

				temp_tuple = (temp_t0,temp_t1,temp_t2)
				
				

				
				selected_tables[-1] = temp_tuple
				
				state = 3
			else :
				print "\n[ERROR] Invalid alias : " + candidate_alias
		elif state == 3:
			if lexer_list[i] == ",":
				state = 0
			else :
				print "\n[ERROR] Expected ','"
				return False
		else :
			print "\n[ERROR] Unknown state : " + str(state)
			return False
	
	if (state == 3) or (state == 1) :
		return True
	
	return False

#	------------------------------------------------------

#	INCLUDE EARLY TERMINATE ';'

def isValidSchemaString(schema_string,target_schema):
	print schema_string
	
	#load tables
	table_list = loadTables("ALL_TABLES")
	#target_schema = loadSchema("ALL_TABLES", True)
	#----------------------------------------------------

	isValid = False
	state = 0
	
	#lexer = shlex.shlex(schema_string, posix=True)
	#lexer.whitespace += ','
	#lexer_list = list(lexer)
	
	lexer_list = shlex.split(columns_string)
	
	for i in range(0, len(lexer_list) ):
	
		term = lexer_list[i].upper()
		if state == 0:
			result = next((i for i, v in enumerate(table_list) if v[0].upper() == term), -1)
			if result != -1 :
				target_schema = loadSchema(term, True)
				target_table = term
				state = 1
			else:
				print "\n[ERROR] Invalid table name : " + term
				return False
		#begin parenthesis
		elif state == 1:
			if term == "(":
				state = 2
			else:
				print "\n[ERROR] Expected '('"
				return False
		#column name
		elif state == 2:
			result = next((i for i, v in enumerate(target_schema) if (v[0].upper() == target_table) and (v[1].upper() == term)), -1)
			if result != -1 :
				if target_schema[result][2] == True:
					print "\n[ERROR] Duplicate column : " + term
					return False
				else:
				
				
					temp_t0 = target_schema[result][0]
					temp_t1 = target_schema[result][0]
					temp_t2 = True
					target_schema[result] = (temp_t0,temp_t1,temp_t2)
					
					state = 3
			else:
				print "\n[ERROR] Invalid column : " + term
				return False
		#comma
		#end parenthesis
		elif state == 3:
			if term == ",":
				state = 2
			elif term == ")":
				isValid = True
			else:
				print "\n[ERROR] Expected ')'"
				return False

		
		else:
			return False
					
		
	
	return isValid
	
#	------------------------------------------------------
def isValidValuesString(values_string,target_schema):

	return False
#	------------------------------------------------------

def isValidColumns(columns_string, selected_tables, selected_columns):

	#load tables
	column_list = loadSchema("ALL_TABLES", False)
	
	#----------------------------------------------------
	
	isValid = False
	state = 0
	
	#lexer = shlex.shlex(columns_string, posix=True)
	#lexer.whitespace += ','
	#lexer_list = list(lexer)
	lexer_list = shlex.split(columns_string)
	
	for i in range(0, len(lexer_list) ):
	#print lexer_list[i]
	
		if state == 0:
			table_alias = lexer_list[i].upper()
			result = next((i for i, v in enumerate(selected_tables) if v[0].upper() == table_alias), -1)
			
			if result != -1 :
				source_table_index = result
				state = 1
			else:
				print "\n[ERROR] Expected a valid target table name/alias."
				return False
		elif state == 1:
			if lexer_list[i] == ".":
				state = 2
			else:
				print "\n[ERROR] Expected '.' ... it's not that hard man."
				return False
		elif state == 2:
			column_name = lexer_list[i].upper()
			result = next((i for i, v in enumerate(column_list) if ((v[0].upper() == selected_tables[source_table_index][1]) and (v[1].upper() == column_name))), -1)
			if result != -1 :
				selected_columns.append(column_list[result])
				state = 3
			else:
				print "\n[ERROR] Expected a valid column name : " + str(column_name)
				return False
		elif state == 3:
			if lexer_list[i] == ",":
				state = 0
			else:
				print "\n[ERROR] Expected ','"
				return False
		else:
			print "\n[ERROR] Unknown state : " + str(state)
			
	print str(state) + "!!!"
	if state == 3 :
		return True
	
	return False

#	------------------------------------------------------

def isValidConditions(conditions_string, selected_tables):

	#load tables
	column_list = loadSchema("ALL_TABLES", False)
	
	#----------------------------------------------------
	
	isValid = False
	state = 0
	pStack = Stack()
	eTree = BinaryTree("!")
	pStack.push(eTree)
	currentTree = eTree
	
	operatorList = ["=", "AND", "OR"]
	
	#lexer = shlex.shlex(conditions_string, posix=True)
	#lexer.whitespace += ';'
	#lexer_list = list(lexer)
	
	lexer_list = shlex.split(conditions_string)
	
	for i in range(0, len(lexer_list) ):
	
		#-----------
		
		term = lexer_list[i].upper()
		
		if term == "(":
			currentTree.insertLeft("")
			pStack.push(currentTree)
			currentTree = currentTree.getLeftChild()
		elif (term not in operatorList) and (term not in ["(",")",";"]):
		
			# Check if term is a valid column or value
			if state == 0:
				result = next((i for i, v in enumerate(selected_tables) if v[0].upper() == term), -1)
				if result != -1 :
					source_table_index = result
					state = 1
				else:
					if isValidTerm(term) :
						rootVal = term
						state = 99
					else:
						print "\n[ERROR] Expected a valid number or column name"
						return False
			elif state == 1:
				if term == ".":
					state = 2
				else:
					print "\n[ERROR] Expected '.'"
					return False
			elif state == 2:
				result = next((i for i, v in enumerate(column_list) if ((v[0].upper() == selected_tables[source_table_index][1]) and (v[1].upper() == term))), -1)
				
				if result != -1 :
					rootVal = column_list[result][0] + "." + column_list[result][1]
					state = 99
				else:
					print "\n[ERROR] Expected a valid column name : " + str(column_name)
					return False
			if state == 99:
				if not pStack.isEmpty():
					state = 0
					currentTree.setRootVal(rootVal)
					parent = pStack.pop()
					currentTree = parent
				else:
					print "\n[ERROR] Unbalanced operations"
					return False
			
		elif term in operatorList:
			currentTree.setRootVal(term)
			currentTree.insertRight("")
			pStack.push(currentTree)
			currentTree = currentTree.getRightChild()
		elif term == ")":
			if not pStack.isEmpty():
				currentTree = pStack.pop()
			else:
				print "\n[ERROR] Unbalanced operations"
				return False
		elif term == ";":
			i = len(lexer_list) + 1
		else:
			raise ValueError
	if not pStack.isEmpty():
		print "\n[ERROR] Unbalanced grouping"
		return False
	return True

#	------------------------------------------------------

def isValidSQL(input_sql):

	isValid = False
	state = 0
	columns_string = ""
	tables_string = ""
	conditions_string = ""
	schema_string = ""
	values_string = ""
	skipColumnCheck = False
	
	lexer = shlex.shlex(input_sql, posix=True)
	#lexer.whitespace += ','
	lexer_list = list(lexer)
	
	#----- Start statement selection -----

	if lexer_list[0].upper() == "SELECT":
		checkType = "SELECT"
		# start loop 
		for i in range(0, len(lexer_list) ):
			#print lexer_list[i]
			
			#	Columns
			if state == 0:
				if lexer_list[i].upper() == "FROM":
					state = 1
					
				elif lexer_list[i].upper() != "SELECT":
					columns_string += " "
					columns_string += lexer_list[i]
				
			#	Tables
			elif state == 1:
				if lexer_list[i].upper() == "WHERE":
					state = 2
				elif lexer_list[i].upper() != "FROM":
					tables_string += " "
					tables_string += lexer_list[i]
					
			elif state == 2:
				if lexer_list[i].upper() != "WHERE":
					conditions_string += " "
					conditions_string += lexer_list[i]
			
		# end loop
		
	elif lexer_list[0].upper() == "DELETE":
		checkType = "DELETE"
		# start loop 
		for i in range(0, len(lexer_list) ):
			#print lexer_list[i]
			
			#	Columns
			if state == 0:
				if lexer_list[i].upper() == "FROM":
					state = 1
					skipColumnCheck = True
			#	Tables
			elif state == 1:
				if lexer_list[i].upper() == "WHERE":
					state = 2
				elif lexer_list[i].upper() != "FROM":
					tables_string += " "
					tables_string += lexer_list[i]
				else:
					print "\n[ERROR] Duplicate keyword : " + lexer_list[i].upper() 
					return False
			elif state == 2:
				if lexer_list[i].upper() != "WHERE":
					conditions_string += " "
					conditions_string += lexer_list[i]
				else:
					print "\n[ERROR] Duplicate keyword : " + lexer_list[i].upper() 
					return False
			else:
				print "\n[ERROR] Unknown state : " + str(state)
				return False
		# end loop
	
	elif lexer_list[0].upper() == "INSERT":
		
		checkType = "INSERT"
		
		for i in range(0, len(lexer_list) ):
			#print lexer_list[i]
			
			#	Columns
			if state == 0:
				if lexer_list[i].upper() == "INTO":
					state = 1
			#	Tables
			elif state == 1:
				if lexer_list[i].upper() == "VALUES":
					state = 2
				elif lexer_list[i].upper() != "INTO":
					schema_string += " "
					schema_string += lexer_list[i]
				else:
					print "\n[ERROR] Duplicate keyword : " + lexer_list[i].upper() 
					return False
			elif state == 2:
				if lexer_list[i].upper() != "VALUES":
					values_string += " "
					values_string += lexer_list[i]
				else:
					print "\n[ERROR] Duplicate keyword : " + lexer_list[i].upper() 
					return False
			else:
				print "\n[ERROR] Unknown state : " + str(state)
				return False
		# end loop
		
	else:
		print "\n[ERROR] Unknown command : " + lexer_list[0].upper()
		return False
	#----- End statement selection -----
		

	
	if checkType == "INSERT":
		#Check INSERT
		target_schema = list()
		if isValidSchemaString(schema_string,target_schema):
			if isValidValuesString(values_string,target_schema):
				return True
			else:
				print "\n[ERROR] isValidValuesString failed"
				print "\n values_string : "
				print "\n" + values_string
				return False
		else:
			print "\n[ERROR] isValidSchemaString failed"
			print "\n schema_string : "
			print "\n" + schema_string
			return False
	else:
		selected_tables = list()
		selected_cloumns = list()

		#Check SELECT
		#Check DELETE
		if isValidTables(tables_string, selected_tables):
			if skipColumnCheck or isValidColumns(columns_string, selected_tables, selected_cloumns):
				if isValidConditions(conditions_string, selected_tables):
					return True
				else:
					print "\n[ERROR] isValidConditions failed"
					print "\n conditions_string : "
					print "\n" + conditions_string
					return False
			else:
				print "\n[ERROR] isValidColumns failed"
				print "\n columns_string : "
				print "\n" + columns_string
				return False
		else:
			print "\n[ERROR] isValidTables failed"
			print "\n tables_string : "
			print "\n" + tables_string
			return False
	return False
	
#	------------------------------------------------------
#	Main Program




input_sql_file  = open(_install_dir + "input.sql","r")
input_sql = input_sql_file.read()

if isValidSQL(input_sql):
	print "\n Is VALID"



#	------------------------------------------------------
