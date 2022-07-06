from random_functions import api
import re

class generateTestcase():

	def __init__(self):
		global random_tool
		random_tool = api()

	def create_file_test(self):
		print("Initial file to testing")
		test_file = open("testAPI.py", mode="w")
		test_file.write("\nfrom random_functions import api")
		test_file.write("\nfrom dataStructure import dataStructure")
		test_file.write("\nclass testAPI():")
		test_file.write("\n\tdef __init__(self):")
		test_file.write("\n\t\tglobal random_tool")
		test_file.write("\n\t\trandom_tool = api()\n")

	def create_testcase(self, api_name, loop=100):

		test_api = open("testAPI.py", mode="a")
		test_api.write("\n\t### TEST: "+api_name+" ###")
		test_api.write("\n\tdef TEST_" + api_name + "(self):")
		test_api.write("\n\t\ttest_" + api_name + " = dataStructure()")
		test_api.write("\n\t\tkey = '" + api_name + "'")
		test_api.write('\n\t\ttest_'+api_name+'.createCommonData("TEST")')
		test_api.write('\n\t\ttest_'+api_name+'.updateCommonData("TEST", random_tool.random_randomlist([key]))')
		test_api.write("\n\t\ttest_" + api_name + ".createArrayData(key)")
		test_api.write("\n\t\tfor i in range("+str(loop)+"):")
		test_api.write("\n\t\t\ttest_"+api_name+".updateArrayData(key, random_tool."+api_name+"())")
		test_api.write("\n\t\ttest_"+api_name+".print_json()\n")
		print("Creating testcase for api: "+api_name)

	def call_testcase(self, api_list):
		test_api = open("testAPI.py", mode="a")
		print("\n--------- Prepare Testcase ---------")
		test_api.write("\n##==================== Call Testcase ====================##")
		test_api.write("\ntest_object = testAPI()")
		for api in api_list:
			test_api.write("\ntest_object.TEST_"+ api + "()")

	### auto Generate Testcase ###
	def auto_generate_testcase(self):
		api_file = open("random_functions.py", mode="r")
		self.create_file_test()
		lines = api_file.readlines()
		api_list = []
		for line in lines:
			if re.findall("^\tdef random_", line):
				api_name = str(re.findall("random_.+self", line))[2:-7]
				api_list.append(api_name)
				self.create_testcase(api_name)
		self.call_testcase(api_list)
		print("SUCCESS auto generate testcase")

test_obj = generateTestcase()
test_obj.auto_generate_testcase()
