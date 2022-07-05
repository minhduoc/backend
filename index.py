import pprint
from flask import Flask
from flask_cors import CORS, cross_origin
from random_functions import api
from dataStructure import dataStructure
import re
from flask import Flask, jsonify, request

class connect:
	def __init__(self):
		pass





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
			tmpKey = tmp_data["keyName"]
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


def generate_json_format(d):


	data = re.sub("%5B", "[", d)
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

			elif element["dataType"] == "object":
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
	rand_func = getattr(random, apiName, "")
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

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

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




     
@app.route("/data/render", methods = ["POST"])
@cross_origin()
def render_data():
	data = request.form.get('dataForm')
	result = []
	number_of_row = re.split("&",data)[0]
	re.findall("number_of_row=*d&", data)

	for i in range(int(re.findall("=\d*", number_of_row)[0][1:])):
		element = generate_json_format(data).format_data()

		result.append(element)
		
	return pprint.pformat(result, indent=6, sort_dicts=False).replace("'", '"')





if __name__ == "__main__":
	app.run()