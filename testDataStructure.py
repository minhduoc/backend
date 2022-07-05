from random_functions import api
from dataStructure import dataStructure


class testDataStructure():
	def __init__(self):
		global random_tool
		random_tool = api()

	def TEST_generate_common_data(self):
		print("######## TEST_generate_common_data ########")
		result = dataStructure()
		for i in range(10):

			key = "CommonData#"+ str(i+1)
			result.createCommonData(key)
			result.updateCommonData(key, random_tool.random_companyname())
		result.print_json()

	def TEST_generate_array_data(self):
		print("######## TEST_generate_array_data ########")
		result = dataStructure()
		key = "ArrayData"
		result.createArrayData(key)
		for i in range(10):
			result.updateArrayData(key, random_tool.random_companyname())
		result.print_json()

	def TEST_generate_object_data(self):
		print("######## TEST_generate_object_data ########")
		result = dataStructure()
		result.createCommonData("test")
		result.updateCommonData("test", random_tool.random_appname())

		result.createObjectData("Object Data")
		sub_obj = dataStructure()
		for i in range(10):
			key = "CommonData#"+ str(i+1)
			sub_obj.createCommonData(key)
			sub_obj.updateCommonData(key, random_tool.random_companyname())
		result.updateObjectData("Object Data", sub_obj.data)

		result.print_json()

	def TEST_generate_array_object_data(self):
		print("######## TEST_generate_array_object_data ########")
		result = dataStructure()
		key = "ArrayData"
		result.createArrayData(key)
		for i in range(10):
			sub_object = dataStructure()
			sub_object.createCommonData("SubName")
			sub_object.updateCommonData("SubName", random_tool.random_fullname())
			sub_object.createCommonData("SubAttr")
			sub_object.updateCommonData("SubAttr", random_tool.random_phonenumber())

			result.updateArrayData(key, sub_object.data)
		result.print_json()


test_dataStructure_obj = testDataStructure()
test_dataStructure_obj.TEST_generate_common_data()
test_dataStructure_obj.TEST_generate_array_data()
test_dataStructure_obj.TEST_generate_object_data()
test_dataStructure_obj.TEST_generate_array_object_data()

