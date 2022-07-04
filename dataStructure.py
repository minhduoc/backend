
import json

class dataStructure ():

	def __init__(self):
		self.data = None
		self.parent = None
		self.value_type = None

	def createCommonData(self, FieldName):
		if self.data is None:
			self.data = {}
			self.data[FieldName] = ""
		else:
			self.data[FieldName] = None

	def updateCommonData(self, FieldName, data):
		self.data[FieldName] = data

	def createObjectData(self,FieldName):
		if self.data is None:
			self.data = {}
		else:
			self.data[FieldName] = {}

	def updateObjectData(self, FieldName, data):
		self.data.update({FieldName : data})

	def createArrayData(self, FieldName) :
		if self.data is None:
			self.data = []
		else:
			self.data[FieldName] = []

	def updateArrayData(self, FieldName, data):
		try:
			self.data[FieldName].append(data)
		except:
			self.data.append(data)

	def format_data(self):
		self.data = str(self.data).replace("'", '"')

	def print_json(self):
		self.format_data()
		your_json =str(self.data)
		parsed = json.loads(your_json)
		print("---------------------------------------------")
		print(json.dumps(parsed, indent=4, sort_keys=False))
		print('\n\n')
		return json.dumps(parsed, indent=4, sort_keys=False)
