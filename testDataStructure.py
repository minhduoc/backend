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
			result.updateCommonData(key, random_tool.random_companyName())
		result.print_json()

	def TEST_generate_array_data(self):
		print("######## TEST_generate_array_data ########")
		result = dataStructure()
		key = "ArrayData"
		result.createArrayData(key)
		for i in range(10):
			result.updateArrayData(key, random_tool.random_companyName())
		result.print_json()

	def TEST_generate_object_data(self):
		print("######## TEST_generate_object_data ########")
		result = dataStructure()
		result.createCommonData("test")
		result.updateCommonData("test", random_tool.random_appName())

		result.createObjectData("Object Data")
		sub_obj = dataStructure()
		for i in range(10):
			key = "CommonData#"+ str(i+1)
			sub_obj.createCommonData(key)
			sub_obj.updateCommonData(key, random_tool.random_companyName())
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
			sub_object.updateCommonData("SubName", random_tool.random_fullName())
			sub_object.createCommonData("SubAttr")
			sub_object.updateCommonData("SubAttr", random_tool.random_phoneNumber())

			result.updateArrayData(key, sub_object.data)
		result.print_json()


	# result = dataStructure()
	# random_tool = api()
	#
	# ##########################################################
	# # Generate Common Data
	# key = "Company Name"
	# result.createCommonData(key)
	# result.updateCommonData(key, random_tool.random_companyName())
	# ##########################################################
	# # Generate Array Data
	# key = "Groups"
	# arr_len = 3
	# result.createArrayData(key)
	# for i in range(arr_len):
	# 	arr_data = random_tool.random_appName()
	# 	result.updateArrayData(key, arr_data)
	# ##########################################################
	# # Generate Object Data
	# key = "Contact"
	# result.createObjectData(key)
	# sub_obj = dataStructure()
	#
	# # Generate Common Data
	# sub_key = "Phone Number"
	# sub_obj.createCommonData(sub_key)
	# sub_obj.updateCommonData(sub_key, random_tool.random_phoneNumber())
	#
	# # Generate Common Data
	# sub_key = "Email"
	# sub_obj.createCommonData(sub_key)
	# sub_obj.updateCommonData(sub_key, random_tool.random_email())
	#
	# # Generate Common Data
	# sub_key = "Address"
	# sub_obj.createCommonData(sub_key)
	# sub_obj.updateCommonData(sub_key, random_tool.random_streetNameAndAddress())
	#
	# result.updateObjectData(key, sub_obj.data)
	#
	# ##########################################################
	#
	# # Generate Array Object Data
	# key = "Employee"
	# result.createArrayData(key)
	# arr_len = 2
	# for i in range(arr_len):
	# 	sub_obj = dataStructure()
	# 	# Generate Common Data
	# 	sub_key = "Name"
	# 	sub_obj.createCommonData(sub_key)
	# 	sub_obj.updateCommonData(sub_key, random_tool.random_fullName())
	#
	# 	# Generate Common Data
	# 	sub_key = "Age"
	# 	sub_obj.createCommonData(sub_key)
	# 	sub_obj.updateCommonData(sub_key, random_tool.randomAge())
	#
	# 	# Generate Common Data
	# 	sub_key = "Gender"
	# 	sub_obj.createCommonData(sub_key)
	# 	sub_obj.updateCommonData(sub_key, random_tool.random_gender())
	#
	# 	result.updateArrayData(key, sub_obj.data)
	#
	# result.print_json()

test_dataStructure_obj = testDataStructure()
test_dataStructure_obj.TEST_generate_common_data()
test_dataStructure_obj.TEST_generate_array_data()
test_dataStructure_obj.TEST_generate_object_data()
test_dataStructure_obj.TEST_generate_array_object_data()

