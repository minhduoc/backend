import re
import  sqlite3
import requests
from dataStructure import dataStructure
from random_functions import api

class connect:
	def __init__(self):
		pass

def get_data(query):
	conn = sqlite3.connect("data/random_db.db")
	ldata = conn.execute(query).fetchall()
	conn.close()

	return ldata

def get_requests(url=""):
	# url = "https://api.github.com"
	# response = requests.get(url)
	# return response.text

	res = """
	  "key_1656556402982" => "key_1"
	  "data_type_1656556402982" => "normal"
	  "value_type_1656556402982" => "fullName"
	  "key_1656556402983" => "key_2"
	  "data_type_1656556402983" => "normal"
	  "value_type_1656556402983" => "email"
	  "option_1_1656556402983" => array:3 [▼0 => "hostmail"
	    1 => "outlook"
	    2 => "yahoo"
	  ]
	  "key_1656556402984" => "key_3"
	  "data_type_1656556402984" => "array"
	  "value_type_1656556402984" => "macAddress"
	  "array_option_1656556402984" => "3"
	  "option_1_1656556402984" => array:1 [▼0 => "A:A"
	  ]
	  "key_1656556461235" => "key_4"
	  "data_type_1656556461235" => "object"
	  "key_object_1656556461235" => "key_4_1"
	  "data_type_object_1656556461235" => "normal"
	  "value_type_object_1656556461235" => "date"
	  "date_start_object_1656556461235" => "2022-06-30"
	  "date_end_object_1656556461235" => "2022-07-02"
	  "date_format_object_1656556461235" => "mm-dd-yyyy"

		"""
	return res


def generate_json_format(url= ""):

	res = get_requests(url=url)
	data = re.sub("\[", "\n[", res)
	data = re.sub("\t", "", data)
	data = re.split("\n", data)

	tmp_data = {}
	obj_dataStructure = dataStructure()
	random = api()
	for i in range(len(data)):
		if isKeyname(data[i]):
			tmp_data.update({ "keyName": get_keyname(data[i]) })
			tmp_data.update({"dataType": get_datatype(data[i+1])})

			if tmp_data["dataType"] == "normal":
				tmp_data.update({ "valueType": get_valuetype(data[i+2])})
				apiName = "random_"+ get_valuetype(data[i+2])
				rand_func= getattr(random, apiName, "")

				obj_dataStructure.createCommonData(get_keyname(data[i]))
				obj_dataStructure.updateCommonData(get_keyname(data[i]), rand_func())

			elif tmp_data["dataType"] == "array":
				tmp_data.update({ "valueType": get_valuetype(data[i+2])})
				obj_dataStructure.createArrayData(get_keyname(data[i]))
				apiName = "random_" + get_valuetype(data[i + 2])
				rand_func = getattr(random, apiName, "")
				for index in range( int(get_array_element_number(data[i + 3]))):
					obj_dataStructure.updateArrayData(get_keyname(data[i]), rand_func())


			elif tmp_data["dataType"] == "object":
				sub_obj = {}
				obj_dataStructure.createObjectData(get_keyname(data[i]))
				sub_dataStructure = dataStructure()
				for j in range(i+2,len(data)):
					if isKeyObject(data[j]):
						sub_obj.update({"keyName": get_keyname(data[j])})
						sub_obj.update({"dataType": get_datatype(data[j + 1])})
						sub_obj.update({"valueType": get_valuetype(data[j + 2])})

						sub_obj.update({"parent": tmp_data["keyName"]})


						if sub_obj["dataType"] == "normal":
							sub_dataStructure.createCommonData(get_keyname(data[j]))
							apiName = "random_" + sub_obj["valueType"]
							rand_func = getattr(random, apiName, "")

							sub_dataStructure.updateCommonData(get_keyname(data[j]), rand_func())

						elif sub_obj["dataType"] == "array":
							sub_obj.update({"valueType": get_valuetype(data[i + 2])})
							sub_dataStructure.createArrayData(get_keyname(data[i]))
							apiName = "random_" + get_valuetype(data[i + 2])
							rand_func = getattr(random, apiName, "")
							for index in range(int(get_array_element_number(data[i + 3]))):
								sub_dataStructure.updateArrayData(get_keyname(data[i]), rand_func())
				obj_dataStructure.updateObjectData(get_keyname(data[i]), sub_dataStructure.data)

	obj_dataStructure.print_json()
	return obj_dataStructure



def get_value_from_response(row):
	return re.findall("=> .*", row)[0][4:-1]

def isKeyname(row):
	if re.findall("key_\d+\" =>", row):
		return True

def isKeyObject(row):
	if re.findall("key_object_\d+\" =>", row):
		return True

def get_keyname(row):
	return re.findall("=> .*", row)[0][4:-1]

def get_datatype(row):
	return re.findall("=> .*", row)[0][4:-1]

def get_valuetype(row):
	return re.findall("=> .*", row)[0][4:-1]

def get_array_element_number(row):
	return re.findall("=> .*", row)[0][4:-1]





