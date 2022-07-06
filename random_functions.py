import calendar
import random
import string
import re
from db import database

class api():
	global db
	db = database()

	def formatData(self, rawdata):
		item_list = re.split("\n", rawdata)
		data = []
		for item in item_list:
			if item != "":
				if item not in data:
					data.append(item)
		return data

	def updateDatabase(self, name, data):
		data_list = self.formatData(data)
		file_database = open("db.py", mode="a")
		file_API = open("random_functions.py", mode="a")

		file_database.write("\n\t\tself." + name + " = " + str(data_list) + "\n")
		file_API.write("\n\t\t###API for random " + name + " ###")
		file_API.write("\n\tdef random_" + name + "(self):")
		file_API.write("\n\t\treturn random.choice(db." + name + ")\n")

	def wrap(self, args):
		min = int(args[0])
		max = int(args[1])
		if min > max:
			tmp = min
			min = max
			max = tmp
		return min, max

	###API for random animalName ###
	def random_animalname(self):
		return random.choice(db.animalName)

	###API for random appBundleID ###
	def random_appbundleid(self):
		return random.choice(db.appBundleID)

	###API for random appName ###
	def random_appname(self):
		return random.choice(db.appName)

	###API for random avatar ###
	def random_avatar(self):
		return random.choice(db.avatar)

	###API for random boolean ###
	def random_boolean(self):
		return random.choice(db.boolean)

	###API for random carBrand ###
	def random_carbrand(self):
		return random.choice(db.carBrand)

	###API for random carModel ###
	def random_carmodel(self):
		return random.choice(db.carModel)

	###API for random city ###
	def random_city(self):
		return random.choice(db.city)

	###API for random color ###
	def random_color(self):
		return random.choice(db.color)

	###API for random companyName ###
	def random_companyname(self):
		return random.choice(db.companyName)

	###API for random contrucionHeavyEquipment ###
	def random_contrucionheavyequipment(self):
		return random.choice(db.contrucionHeavyEquipment)

	###API for random contrucionMaterial ###
	def random_contrucionmaterial(self):
		return random.choice(db.contrucionMaterial)

	###API for random contrucionRole ###
	def random_contrucionrole(self):
		return random.choice(db.contrucionRole)

	###API for random contrucionTrade ###
	def random_contruciontrade(self):
		return random.choice(db.contrucionTrade)

	###API for random country ###
	def random_country(self):
		return random.choice(db.country)

	###API for random countryCode ###
	def random_countrycode(self):
		return random.choice(db.countryCode)

	###API for random creditCardType ###
	def random_creditcardtype(self):
		return random.choice(db.creditCardType)

	###API for random currency ###
	def random_currency(self):
		return random.choice(db.currency)

	###API for random currencyCode ###
	def random_currencycode(self):
		return random.choice(db.currencyCode)

	###API for random department ###
	def random_department(self):
		return random.choice(db.department)

	###API for random domain ###
	def random_domain(self):
		return random.choice(db.domain)

	###API for random dummyImageURL ###
	def random_dummyimageurl(self):
		return random.choice(db.dummyImageURL)

	###API for random fileExtension ###
	def random_fileextension(self):
		return random.choice(db.fileExtension)

	###API for random fileName ###
	def random_filename(self):
		return random.choice(db.fileName)

	###API for random firstName ###
	def random_firstname(self):
		return random.choice(db.firstName)

	###API for random jobTitle ###
	def random_jobnitle(self):
		return random.choice(db.jobTitle)

	###API for random language ###
	def random_language(self):
		return random.choice(db.language)

	###API for random lastName ###
	def random_lastname(self):
		return random.choice(db.lastName)

	###API for random productGrocery ###
	def random_productgrocery(self):
		return random.choice(db.productGrocery)

	###API for random streetName ###
	def random_streetname(self):
		return random.choice(db.streetName)

	###API for random timeZone ###
	def random_timezone(self):
		return random.choice(db.timeZone)

	###API for random gender ###
	def random_gender(self):
		return random.choice(db.gender)

	###API for random programmingLanguage ###
	def random_programminglanguage(self):
		return random.choice(db.programmingLanguage)

	###API for random dayWeek ###
	def random_dayweek(self):
		return random.choice(db.dayWeek)

	###API for random month ###
	def random_month(self):
		return random.choice(db.month)

	###API for random customdata ###
	def random_randomlist(self, dataset=[]):
		if  not dataset:
			return []
		else:
			try:
				dataset = re.sub(" ", "", dataset[0])
				dataset = re.split(",", dataset)
			except:
				pass
			return random.choice(dataset)

	###API for random fullName ###
	def random_fullname(self):
		return self.random_firstname() + " " + self.random_lastname()

	###API for random userName ###
	def random_username(self):
		return self.random_firstname()[0].lower() + self.random_lastname().lower() + str(random.randint(1, 99))

	###API for random Age ###
	def random_age(self, args=None):

		min = 10
		max = 90
		if args:
			min, max = self.wrap(args)

		return random.randint(min, max)

	###API for random year ###
	def random_year(self, args = None):
		min = 1800
		max = 2200
		if args:
			min, max = self.wrap(args)

		return random.randint(min, max)

	###API for random email ###
	def random_email(self, args = None):

		name = self.random_username()
		if args:
			domain = random.choice(args)
		else:
			domain = self.random_domain()
			return name.lower() + "@" + domain

		extends = ["com", "net", "org", "edu", "vn", "com.vn", "net.vn", "edu.vn", "ac.uk", "co.uk", "gov.uk", "me.uk", "org.uk"]

		return name.lower() + "@" + domain + "." + self.random_randomlist(extends)

	###API for random ipv4 ###
	def random_ipv4(self):
		offset = [1, 0, 0, 1]
		ip = ""
		for i in offset:
			ip += str(random.randint(i, 255))
			ip += "."
		return ip[0:-1]

	###API for random ipv6 ###
	def random_ipv6(self):
		template = string.digits + "ABCDEF"
		ipv6 = ""
		for i in range(8):
			ipv6 += ''.join(random.choice(template) for _ in range(4))
			ipv6 += "."
		return ipv6[0:-1]

	###API for random macAddress ###
	def random_macaddress(self, args=None):
		"""
		:param seperator: ":"  "-"
		"""
		if args:
			seperator = args[0]
		else:
			seperator = ":"

		template = string.digits + "ABCDEF"
		mac = ""
		for i in range(6):
			mac += ''.join(random.choice(template) for _ in range(2))
			mac += seperator
		return mac[0:-1]

	###API for random version ###
	def random_version(self, args = None):
		min = 2
		max = 4
		if args:
			min, max = self.wrap(args)

		lenth = random.randint(min, max)
		version = ""
		for i in range(lenth):
			version += str(random.randint(1, 20))
			version += "."
		return version[0:-1]

	###API for random bitcoinAddress ###
	def random_bitcoinaddress(self):
		template = string.digits + string.ascii_lowercase
		bit = ""
		for i in range(42):
			bit += random.choice(template)
		return bit

	###API for random creditCard ###
	def random_creditcard(self, credit_type=None):
		"""
		:param credit_type:
			'visa'
			'visa-electron'
			'americanexpress'
			'china-unionpay'
			'mastercard'
			'maestro'
			'diners-club-carte-blanche'
			'diners-club-international'
			'diners-club-us-ca'
			'jcb'
			'diners-club-enroute'
			'interpayment'
			'bankcard'
			'laser'
			'switch'
			'other'
		"""

		if credit_type is None:
			credit_type = []
			for i in range(random.randint(2, 8)):
				credit_type.append(self.random_creditcardtype())
		template = []
		if 'visa' in credit_type:
			template.append("4### #### #### ####")
		if 'visa-electron' in credit_type:
			template.append(
				str(self.random_randomlist(dataset=[4026, 4405, 4508, 4844, 4913, 4917])) + " #### #### ####")
		if 'americanexpress' in credit_type:
			template.append(str(self.random_randomlist(dataset=[34, 37])) + "## ###### #####")
		if 'china-unionpay' in credit_type:
			template.append("62## ###### #####")
		if 'mastercard' in credit_type:
			template.append(str(random.randint(51, 55)) + "## #### #### ####")
		if 'maestro' in credit_type:
			template.append(str(self.random_randomlist(
				dataset=[5018, 5020, 5038, 5612, 5893, 6304, 6759, 6761, 6762, 6763, 6390])) + " #### #### ####")
		if 'diners-club-carte-blanche' in credit_type:
			template.append(str(random.randint(300, 305)) + "# ###### ####")
		if 'diners-club-international' in credit_type:
			template.append(str(self.random_randomlist(dataset=[300, 301, 302, 303, 304, 305, 309])) + "# ###### ####")
		if 'diners-club-us-ca' in credit_type:
			template.append(str(self.random_randomlist(dataset=[54, 55])) + "## #### #### ####")
		if 'jcb' in credit_type:
			template.append(str(random.randint(3528, 3589)) + " #### #### ####")
		if 'diners-club-enroute' in credit_type:
			template.append(str(self.random_randomlist(dataset=[2014, 2149])) + " ####### ####")
		if 'interpayment' in credit_type:
			template.append("636# #### ####")
		if 'bankcard' in credit_type:
			template.append("5610 #### ####")
		if 'laser' in credit_type:
			template.append(str(self.random_randomlist(dataset=[6304, 6706, 6771, 6709])) + "#### #### ####")
		if 'switch' in credit_type:
			template.append(str(self.random_randomlist(dataset=[4903, 4905, 4911, 4936, 6333, 6759])) + "#### #### ####")
		if template == []:
			template = "#### #### #### ####"

		credit_number = ""
		random_template = random.choice(template)
		for n in random_template:
			if n == "#":
				credit_number += str(random.randint(0, 9))
			else:
				credit_number += str(n)
		return credit_number

	###API for random date ###
	def random_date(self, args= None):
		min = "01/01/1800"
		max = "31/12/2200"
		try:
			format = args[2]
		except:
			format = "dd/mm/yyyy"
		if args:
			minDay, minMonth, minYear = re.split('/', args[0])
			maxDay, maxMonth, maxYear = re.split('/', args[1])
		else:
			minDay, minMonth, minYear = re.split('/', min)
			maxDay, maxMonth, maxYear = re.split('/', max)
		tmpY = str(random.randint(int(minYear), int(maxYear)))

		if minYear == maxYear:
			tmpM = int(random.randint(int(minMonth), int(maxMonth)))
		else:
			tmpM = random.randint(1, 12)

		while True:
			dd = random.randint(1, calendar.mdays[tmpM])
			if dd > int(minDay) and dd < int(maxDay):
				break
		if len(str(dd)) == 1:
			dd = '0' + str(dd)

		date = ""
		tmpM = str(tmpM)
		if "mm" in format:
			if len(str(tmpM)) == 1:
				tmpM = '0' + str(tmpM)
			date = re.sub("mm", tmpM, format)
		else:
			tmpM = calendar.month_name[int(tmpM)][:3]
			date = re.sub("Mth", tmpM, format)

		date = re.sub("dd", str(dd), date)

		date = re.sub("yyyy", tmpY, date)
		return date

	###API for random fileNameWithExtension ###
	def random_filenamewithextension(self):
		return self.random_filename() + "." + self.random_fileextension()

	###API for random hexColorCode ###
	def random_hexcolorcode(self):
		template = string.digits + "ABCDEF"
		return "#" + ''.join(random.choice(template) for _ in range(6))

	###API for random SHA256 ###
	def random_sha256(self):
		template = string.digits + "abcdef"
		return ''.join(random.choice(template) for _ in range(64))

	###API for random phoneNumber ###
	def random_phonenumber(self, format="0## ### ####"):
		"""
		:param format:
			"0## ### ####"
			"0##-###-####"
			"(0##)###-####"
			"+84 ### ### ###"
			"0#########"
		"""
		phone = ''
		for n in format:
			if n == "#":
				phone += str(random.randint(0, 9))
			else:
				phone += str(n)
		return phone

	###API for random streetNameAndAddress ###
	def random_streetnameandaddress(self):
		return str(random.randint(1, 999)) + " " + self.random_streetname()

	###API for random password ###
	def random_password(self, args= None):
		"""
		:param min:
		:param max:

		"""
		min = 8
		max = 12
		if args:
			min, max = self.wrap(args)

		template = string.digits + string.ascii_lowercase + string.ascii_uppercase + '!@#$%^&*'
		len = random.randint(min, max)
		return ''.join(random.choice(template) for _ in range(len))

	###API for random number ###
	def random_number(self, args=None):

		min = 8
		max = 12
		if args:
			min, max = self.wrap(args)

		return random.randint(min, max)

	###API for random time ###
	def random_time(self, args = None):
		"""
		:param format:
			"12 Hour"
			"24 Hour"
		"""
		if args:
			format = args[0]
		else:
			format = "12 Hour"

		h = str(random.randint(1, int(format[:2]) - 1))
		m = str(random.randint(0, 59))
		if len(m) == 1:
			m = '0' + m
		if format == "12 Hour":
			period = self.random_randomlist(["AM", "PM"])
		else:
			period = ""
		return h + ":" + m + " " + period