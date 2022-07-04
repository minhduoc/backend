from flask import Flask, jsonify
import re
import requests
from dataStructure import dataStructure
from random_functions import api

class connect:
	def __init__(self):
		pass

# def get_data(query):
# 	conn = sqlite3.connect("data/random_db.db")
# 	ldata = conn.execute(query).fetchall()
# 	conn.close()
#
# 	return ldata

def get_requests(url=""):
	# url = "https://api.github.com"
	if not url:
		return ""
	response = requests.get(url)
	return response.text







def createField(data):
	lField = []
	tmp_data = {}
	tmpKey = ""
	for i in range(len(data)):


		if isKeyObject(data[i]):
			tmp_data.update({"keyName": get_keyname(data[i])})
			tmp_data.update({"dataType": get_datatype(data[i + 1])})
			key_parent = tmpKey
			try:
				tmp_data.update({"valueType": get_valuetype(data[i + 2])})
			except:
				pass

			option = []
			try:
				for j in range(i + 3, i + 6):
					if isOption(data[j]):
						option.append(get_option(data[j]))
			except:
				pass

			if option:
				tmp_data.update({"option": option})

			tmp_data.update({"parent": key_parent})

		elif isKeyname(data[i]):
			tmp_data.update({"keyName": get_keyname(data[i])})
			tmp_data.update({"dataType": get_datatype(data[i + 1])})
			key_parent = "root"
			tmpKey= tmp_data["keyName"]
			try:
				tmp_data.update({"valueType": get_valuetype(data[i + 2])})
			except:
				pass

			option = []
			try:
				for j in range(i + 1, i + 6):
					if isOption(data[j]):
						option.append(get_option(data[j]))
			except:
				pass

			if option:
				tmp_data.update({"option": option})

			tmp_data.update({"parent": key_parent})



		if tmp_data:
			lField.append(tmp_data)


			tmp_data = {}

	return lField


def generate_json_format(url):
	res = get_requests(url=url)

	if not res:
		return ""

	data = re.sub("%5B", "[", res)
	data = re.sub("%5D", "]", data)
	data = re.sub("%20", " ", data)
	data = re.sub("%3A", ":", data)
	data = re.sub("%2C", ",", data)

	data = re.split("&", data)

	obj_dataStructure = dataStructure()

	lField = createField(data)

	for element in lField:
		if element["parent"] == "root":
			if element["dataType"] == "normal":
				obj_dataStructure.createCommonData(element["keyName"])
				rand_func = get_random_function(element)
				obj_dataStructure.updateCommonData(element["keyName"], rand_func())

			elif element["dataType"] == "array":
				obj_dataStructure.createArrayData(element["keyName"])
				rand_func = get_random_function(element)
				for i in range(int(element["option"][0])):
					obj_dataStructure.updateArrayData(element["keyName"], rand_func())

			elif  element["dataType"] == "object":
				obj_dataStructure.createObjectData(element["keyName"])
				subobj = dataStructure()
				for tmp in lField:
					if tmp["parent"] == element["keyName"]:
						if tmp["dataType"] == "normal":
							subobj.createCommonData(tmp["keyName"])
							rand_func = get_random_function(tmp)
							subobj.updateCommonData(tmp["keyName"], rand_func())

						elif tmp["dataType"] == "array":
							subobj.createArrayData(tmp["keyName"])
							rand_func = get_random_function(tmp)
							for i in range(int(tmp["option"][0])):
								subobj.updateArrayData(tmp["keyName"], rand_func())
					if subobj.data:
						obj_dataStructure.updateObjectData(element["keyName"], subobj.data)
						break

			elif element["dataType"] == "arrobj":
				obj_dataStructure.createArrayData(element["keyName"])

				for i in range(int(element["option"][0])):
					subobj = dataStructure()
					for tmp in lField:
						if tmp["parent"] == element["keyName"]:
							if tmp["dataType"] == "normal":
								subobj.createCommonData(tmp["keyName"])
								rand_func = get_random_function(tmp)
								subobj.updateCommonData(tmp["keyName"], rand_func())

							elif tmp["dataType"] == "array":
								subobj.createArrayData(tmp["keyName"])
								rand_func = get_random_function(tmp)
								for i in range(int(tmp["option"][0])):
									subobj.updateArrayData(tmp["keyName"], rand_func())
					if subobj.data:
						obj_dataStructure.updateArrayData(element["keyName"], subobj.data)

	return obj_dataStructure



def get_random_function(element):
	random = api()
	apiName = "random_" + element["valueType"].lower()
	apiName = re.sub(" ", "", apiName)
	rand_func= getattr(random, apiName, "")
	return rand_func

def get_value_from_response(row):
	return re.findall("=.*", row)[0][1:]

def isKeyname(row):
	if re.findall("key_\S+=", row):
		return True

def isKeyObject(row):
	if re.findall("key_object_\S+=", row):
		return True
	else:
		return False

def isOption(row):
	if re.findall("option_\S+=", row):
		return True
	else:
		return False

def get_keyname(row):
	if re.findall("key_\S+=", row):
		return re.findall("=.*", row)[0][1:]
	else:
		return ""

def get_datatype(row):
	if re.findall("data_type_\S+=", row):
		return re.findall("=.*", row)[0][1:]
	else:
		return ""

def get_option(row):
	if re.findall("option_\S+=", row):
		return re.findall("=.*", row)[0][1:]
	else:
		return ""

def get_valuetype(row):
	if re.findall("value_type_\S+=", row):
		return re.findall("=.*", row)[0][1:]
	else:
		return ""

def get_array_element_number(row):
	if re.findall("array_option_\S+=", row):
		return re.findall("=.*", row)[0][1:]
	else:
		return ""










app = Flask(__name__)

# @app.route("/get", methods = ["GET"])
# def get_from_db():
#
# 	ldata = get_data("SELECT value FROM animalName")
# 	data = []
# 	for row in ldata:
# 		data.append(row)
#
# 	return jsonify(data)


# @app.route("/add", methods =["POST"])
# def insert_db():
# 	pass

@app.route("/request", methods = ["GET"])
def test_request():
	return "number_of_row=100&format_file=JSON&sql_table_name=&key_1656900689104=key_1&data_type_1656900689104=normal&value_type_1656900689104=username&key_1656900689105=key_2&data_type_1656900689105=normal&value_type_1656900689105=Email&option_1_1656900689105%5B%5D=hostmail&option_1_1656900689105%5B%5D=gmail&key_1656900689106=key_3&data_type_1656900689106=array&value_type_1656900689106=firstname&array_option_1656900689106=2&key_1656900714010=key_4&data_type_1656900714010=arrobj&array_option_1656900714010=3&key_object_1656900714010=key_4_1&data_type_object_1656900714010=normal&value_type_object_1656900714010=Number&option_1_object_1656900714010=1&option_2_object_1656900714010=4&key_object_1656900731177=key_4_2&data_type_object_1656900731177=array&value_type_object_1656900731177=MAC%20Address&array_option_object_1656900731177=5&option_1_object_1656900731177%5B%5D=A%3AA&option_1_object_1656900731177%5B%5D=A-A&key_1656900745706=key_5&data_type_1656900745706=object&key_object_1656900745706=key_5_1&data_type_object_1656900745706=normal&value_type_object_1656900745706=Fullname&key_object_1656900780210=key_5_2&data_type_object_1656900780210=array&value_type_object_1656900780210=Random%20List&array_option_object_1656900780210=2&option_1_object_1656900780210=item1%2C%20item2%2C%20item3"


@app.route("/export", methods = ["GET"])
def render_data(url = "http://127.0.0.1:5000//request"):
	if not url:
		return ""
	data = generate_json_format(url).print_json()

	data = re.sub("\n", "<br>", data)
	data = re.sub(" ", "&nbsp;", data)

	return data

if __name__ == "__main__":
	app.run()