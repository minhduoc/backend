
from random_functions import api
from dataStructure import dataStructure
class testAPI():
	def __init__(self):
		global random_tool
		random_tool = api()

	### TEST: random_animalName ###
	def TEST_random_animalName(self):
		test_random_animalName = dataStructure()
		key = 'random_animalName'
		test_random_animalName.createCommonData("TEST")
		test_random_animalName.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_animalName.createArrayData(key)
		for i in range(10):
			test_random_animalName.updateArrayData(key, random_tool.random_animalName())
		test_random_animalName.print_json()

	### TEST: random_appBundleID ###
	def TEST_random_appBundleID(self):
		test_random_appBundleID = dataStructure()
		key = 'random_appBundleID'
		test_random_appBundleID.createCommonData("TEST")
		test_random_appBundleID.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_appBundleID.createArrayData(key)
		for i in range(10):
			test_random_appBundleID.updateArrayData(key, random_tool.random_appBundleID())
		test_random_appBundleID.print_json()

	### TEST: random_appName ###
	def TEST_random_appName(self):
		test_random_appName = dataStructure()
		key = 'random_appName'
		test_random_appName.createCommonData("TEST")
		test_random_appName.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_appName.createArrayData(key)
		for i in range(10):
			test_random_appName.updateArrayData(key, random_tool.random_appName())
		test_random_appName.print_json()

	### TEST: random_avatar ###
	def TEST_random_avatar(self):
		test_random_avatar = dataStructure()
		key = 'random_avatar'
		test_random_avatar.createCommonData("TEST")
		test_random_avatar.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_avatar.createArrayData(key)
		for i in range(10):
			test_random_avatar.updateArrayData(key, random_tool.random_avatar())
		test_random_avatar.print_json()

	### TEST: random_boolean ###
	def TEST_random_boolean(self):
		test_random_boolean = dataStructure()
		key = 'random_boolean'
		test_random_boolean.createCommonData("TEST")
		test_random_boolean.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_boolean.createArrayData(key)
		for i in range(10):
			test_random_boolean.updateArrayData(key, random_tool.random_boolean())
		test_random_boolean.print_json()

	### TEST: random_carBrand ###
	def TEST_random_carBrand(self):
		test_random_carBrand = dataStructure()
		key = 'random_carBrand'
		test_random_carBrand.createCommonData("TEST")
		test_random_carBrand.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_carBrand.createArrayData(key)
		for i in range(10):
			test_random_carBrand.updateArrayData(key, random_tool.random_carBrand())
		test_random_carBrand.print_json()

	### TEST: random_carModel ###
	def TEST_random_carModel(self):
		test_random_carModel = dataStructure()
		key = 'random_carModel'
		test_random_carModel.createCommonData("TEST")
		test_random_carModel.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_carModel.createArrayData(key)
		for i in range(10):
			test_random_carModel.updateArrayData(key, random_tool.random_carModel())
		test_random_carModel.print_json()

	### TEST: random_city ###
	def TEST_random_city(self):
		test_random_city = dataStructure()
		key = 'random_city'
		test_random_city.createCommonData("TEST")
		test_random_city.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_city.createArrayData(key)
		for i in range(10):
			test_random_city.updateArrayData(key, random_tool.random_city())
		test_random_city.print_json()

	### TEST: random_color ###
	def TEST_random_color(self):
		test_random_color = dataStructure()
		key = 'random_color'
		test_random_color.createCommonData("TEST")
		test_random_color.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_color.createArrayData(key)
		for i in range(10):
			test_random_color.updateArrayData(key, random_tool.random_color())
		test_random_color.print_json()

	### TEST: random_companyName ###
	def TEST_random_companyName(self):
		test_random_companyName = dataStructure()
		key = 'random_companyName'
		test_random_companyName.createCommonData("TEST")
		test_random_companyName.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_companyName.createArrayData(key)
		for i in range(10):
			test_random_companyName.updateArrayData(key, random_tool.random_companyName())
		test_random_companyName.print_json()

	### TEST: random_contrucionHeavyEquipment ###
	def TEST_random_contrucionHeavyEquipment(self):
		test_random_contrucionHeavyEquipment = dataStructure()
		key = 'random_contrucionHeavyEquipment'
		test_random_contrucionHeavyEquipment.createCommonData("TEST")
		test_random_contrucionHeavyEquipment.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_contrucionHeavyEquipment.createArrayData(key)
		for i in range(10):
			test_random_contrucionHeavyEquipment.updateArrayData(key, random_tool.random_contrucionHeavyEquipment())
		test_random_contrucionHeavyEquipment.print_json()

	### TEST: random_contrucionMaterial ###
	def TEST_random_contrucionMaterial(self):
		test_random_contrucionMaterial = dataStructure()
		key = 'random_contrucionMaterial'
		test_random_contrucionMaterial.createCommonData("TEST")
		test_random_contrucionMaterial.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_contrucionMaterial.createArrayData(key)
		for i in range(10):
			test_random_contrucionMaterial.updateArrayData(key, random_tool.random_contrucionMaterial())
		test_random_contrucionMaterial.print_json()

	### TEST: random_contrucionRole ###
	def TEST_random_contrucionRole(self):
		test_random_contrucionRole = dataStructure()
		key = 'random_contrucionRole'
		test_random_contrucionRole.createCommonData("TEST")
		test_random_contrucionRole.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_contrucionRole.createArrayData(key)
		for i in range(10):
			test_random_contrucionRole.updateArrayData(key, random_tool.random_contrucionRole())
		test_random_contrucionRole.print_json()

	### TEST: random_contrucionTrade ###
	def TEST_random_contrucionTrade(self):
		test_random_contrucionTrade = dataStructure()
		key = 'random_contrucionTrade'
		test_random_contrucionTrade.createCommonData("TEST")
		test_random_contrucionTrade.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_contrucionTrade.createArrayData(key)
		for i in range(10):
			test_random_contrucionTrade.updateArrayData(key, random_tool.random_contrucionTrade())
		test_random_contrucionTrade.print_json()

	### TEST: random_country ###
	def TEST_random_country(self):
		test_random_country = dataStructure()
		key = 'random_country'
		test_random_country.createCommonData("TEST")
		test_random_country.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_country.createArrayData(key)
		for i in range(10):
			test_random_country.updateArrayData(key, random_tool.random_country())
		test_random_country.print_json()

	### TEST: random_countryCode ###
	def TEST_random_countryCode(self):
		test_random_countryCode = dataStructure()
		key = 'random_countryCode'
		test_random_countryCode.createCommonData("TEST")
		test_random_countryCode.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_countryCode.createArrayData(key)
		for i in range(10):
			test_random_countryCode.updateArrayData(key, random_tool.random_countryCode())
		test_random_countryCode.print_json()

	### TEST: random_creditCardType ###
	def TEST_random_creditCardType(self):
		test_random_creditCardType = dataStructure()
		key = 'random_creditCardType'
		test_random_creditCardType.createCommonData("TEST")
		test_random_creditCardType.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_creditCardType.createArrayData(key)
		for i in range(10):
			test_random_creditCardType.updateArrayData(key, random_tool.random_creditCardType())
		test_random_creditCardType.print_json()

	### TEST: random_currency ###
	def TEST_random_currency(self):
		test_random_currency = dataStructure()
		key = 'random_currency'
		test_random_currency.createCommonData("TEST")
		test_random_currency.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_currency.createArrayData(key)
		for i in range(10):
			test_random_currency.updateArrayData(key, random_tool.random_currency())
		test_random_currency.print_json()

	### TEST: random_currencyCode ###
	def TEST_random_currencyCode(self):
		test_random_currencyCode = dataStructure()
		key = 'random_currencyCode'
		test_random_currencyCode.createCommonData("TEST")
		test_random_currencyCode.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_currencyCode.createArrayData(key)
		for i in range(10):
			test_random_currencyCode.updateArrayData(key, random_tool.random_currencyCode())
		test_random_currencyCode.print_json()

	### TEST: random_department ###
	def TEST_random_department(self):
		test_random_department = dataStructure()
		key = 'random_department'
		test_random_department.createCommonData("TEST")
		test_random_department.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_department.createArrayData(key)
		for i in range(10):
			test_random_department.updateArrayData(key, random_tool.random_department())
		test_random_department.print_json()

	### TEST: random_domain ###
	def TEST_random_domain(self):
		test_random_domain = dataStructure()
		key = 'random_domain'
		test_random_domain.createCommonData("TEST")
		test_random_domain.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_domain.createArrayData(key)
		for i in range(10):
			test_random_domain.updateArrayData(key, random_tool.random_domain())
		test_random_domain.print_json()

	### TEST: random_dummyImageURL ###
	def TEST_random_dummyImageURL(self):
		test_random_dummyImageURL = dataStructure()
		key = 'random_dummyImageURL'
		test_random_dummyImageURL.createCommonData("TEST")
		test_random_dummyImageURL.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_dummyImageURL.createArrayData(key)
		for i in range(10):
			test_random_dummyImageURL.updateArrayData(key, random_tool.random_dummyImageURL())
		test_random_dummyImageURL.print_json()

	### TEST: random_fileExtension ###
	def TEST_random_fileExtension(self):
		test_random_fileExtension = dataStructure()
		key = 'random_fileExtension'
		test_random_fileExtension.createCommonData("TEST")
		test_random_fileExtension.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_fileExtension.createArrayData(key)
		for i in range(10):
			test_random_fileExtension.updateArrayData(key, random_tool.random_fileExtension())
		test_random_fileExtension.print_json()

	### TEST: random_fileName ###
	def TEST_random_fileName(self):
		test_random_fileName = dataStructure()
		key = 'random_fileName'
		test_random_fileName.createCommonData("TEST")
		test_random_fileName.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_fileName.createArrayData(key)
		for i in range(10):
			test_random_fileName.updateArrayData(key, random_tool.random_fileName())
		test_random_fileName.print_json()

	### TEST: random_firstName ###
	def TEST_random_firstName(self):
		test_random_firstName = dataStructure()
		key = 'random_firstName'
		test_random_firstName.createCommonData("TEST")
		test_random_firstName.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_firstName.createArrayData(key)
		for i in range(10):
			test_random_firstName.updateArrayData(key, random_tool.random_firstName())
		test_random_firstName.print_json()

	### TEST: random_jobTitle ###
	def TEST_random_jobTitle(self):
		test_random_jobTitle = dataStructure()
		key = 'random_jobTitle'
		test_random_jobTitle.createCommonData("TEST")
		test_random_jobTitle.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_jobTitle.createArrayData(key)
		for i in range(10):
			test_random_jobTitle.updateArrayData(key, random_tool.random_jobTitle())
		test_random_jobTitle.print_json()

	### TEST: random_language ###
	def TEST_random_language(self):
		test_random_language = dataStructure()
		key = 'random_language'
		test_random_language.createCommonData("TEST")
		test_random_language.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_language.createArrayData(key)
		for i in range(10):
			test_random_language.updateArrayData(key, random_tool.random_language())
		test_random_language.print_json()

	### TEST: random_lastName ###
	def TEST_random_lastName(self):
		test_random_lastName = dataStructure()
		key = 'random_lastName'
		test_random_lastName.createCommonData("TEST")
		test_random_lastName.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_lastName.createArrayData(key)
		for i in range(10):
			test_random_lastName.updateArrayData(key, random_tool.random_lastName())
		test_random_lastName.print_json()

	### TEST: random_productGrocery ###
	def TEST_random_productGrocery(self):
		test_random_productGrocery = dataStructure()
		key = 'random_productGrocery'
		test_random_productGrocery.createCommonData("TEST")
		test_random_productGrocery.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_productGrocery.createArrayData(key)
		for i in range(10):
			test_random_productGrocery.updateArrayData(key, random_tool.random_productGrocery())
		test_random_productGrocery.print_json()

	### TEST: random_streetName ###
	def TEST_random_streetName(self):
		test_random_streetName = dataStructure()
		key = 'random_streetName'
		test_random_streetName.createCommonData("TEST")
		test_random_streetName.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_streetName.createArrayData(key)
		for i in range(10):
			test_random_streetName.updateArrayData(key, random_tool.random_streetName())
		test_random_streetName.print_json()

	### TEST: random_timeZone ###
	def TEST_random_timeZone(self):
		test_random_timeZone = dataStructure()
		key = 'random_timeZone'
		test_random_timeZone.createCommonData("TEST")
		test_random_timeZone.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_timeZone.createArrayData(key)
		for i in range(10):
			test_random_timeZone.updateArrayData(key, random_tool.random_timeZone())
		test_random_timeZone.print_json()

	### TEST: random_gender ###
	def TEST_random_gender(self):
		test_random_gender = dataStructure()
		key = 'random_gender'
		test_random_gender.createCommonData("TEST")
		test_random_gender.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_gender.createArrayData(key)
		for i in range(10):
			test_random_gender.updateArrayData(key, random_tool.random_gender())
		test_random_gender.print_json()

	### TEST: random_programmingLanguage ###
	def TEST_random_programmingLanguage(self):
		test_random_programmingLanguage = dataStructure()
		key = 'random_programmingLanguage'
		test_random_programmingLanguage.createCommonData("TEST")
		test_random_programmingLanguage.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_programmingLanguage.createArrayData(key)
		for i in range(10):
			test_random_programmingLanguage.updateArrayData(key, random_tool.random_programmingLanguage())
		test_random_programmingLanguage.print_json()

	### TEST: random_dayWeek ###
	def TEST_random_dayWeek(self):
		test_random_dayWeek = dataStructure()
		key = 'random_dayWeek'
		test_random_dayWeek.createCommonData("TEST")
		test_random_dayWeek.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_dayWeek.createArrayData(key)
		for i in range(10):
			test_random_dayWeek.updateArrayData(key, random_tool.random_dayWeek())
		test_random_dayWeek.print_json()

	### TEST: random_month ###
	def TEST_random_month(self):
		test_random_month = dataStructure()
		key = 'random_month'
		test_random_month.createCommonData("TEST")
		test_random_month.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_month.createArrayData(key)
		for i in range(10):
			test_random_month.updateArrayData(key, random_tool.random_month())
		test_random_month.print_json()

	### TEST: random_customdata ###
	def TEST_random_customdata(self):
		test_random_customdata = dataStructure()
		key = 'random_customdata'
		test_random_customdata.createCommonData("TEST")
		test_random_customdata.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_customdata.createArrayData(key)
		for i in range(10):
			test_random_customdata.updateArrayData(key, random_tool.random_customdata())
		test_random_customdata.print_json()

	### TEST: random_fullName ###
	def TEST_random_fullName(self):
		test_random_fullName = dataStructure()
		key = 'random_fullName'
		test_random_fullName.createCommonData("TEST")
		test_random_fullName.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_fullName.createArrayData(key)
		for i in range(10):
			test_random_fullName.updateArrayData(key, random_tool.random_fullName())
		test_random_fullName.print_json()

	### TEST: random_userName ###
	def TEST_random_userName(self):
		test_random_userName = dataStructure()
		key = 'random_userName'
		test_random_userName.createCommonData("TEST")
		test_random_userName.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_userName.createArrayData(key)
		for i in range(10):
			test_random_userName.updateArrayData(key, random_tool.random_userName())
		test_random_userName.print_json()

	### TEST: random_year ###
	def TEST_random_year(self):
		test_random_year = dataStructure()
		key = 'random_year'
		test_random_year.createCommonData("TEST")
		test_random_year.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_year.createArrayData(key)
		for i in range(10):
			test_random_year.updateArrayData(key, random_tool.random_year())
		test_random_year.print_json()

	### TEST: random_email ###
	def TEST_random_email(self):
		test_random_email = dataStructure()
		key = 'random_email'
		test_random_email.createCommonData("TEST")
		test_random_email.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_email.createArrayData(key)
		for i in range(10):
			test_random_email.updateArrayData(key, random_tool.random_email())
		test_random_email.print_json()

	### TEST: random_IPv4 ###
	def TEST_random_IPv4(self):
		test_random_IPv4 = dataStructure()
		key = 'random_IPv4'
		test_random_IPv4.createCommonData("TEST")
		test_random_IPv4.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_IPv4.createArrayData(key)
		for i in range(10):
			test_random_IPv4.updateArrayData(key, random_tool.random_IPv4())
		test_random_IPv4.print_json()

	### TEST: random_IPv6 ###
	def TEST_random_IPv6(self):
		test_random_IPv6 = dataStructure()
		key = 'random_IPv6'
		test_random_IPv6.createCommonData("TEST")
		test_random_IPv6.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_IPv6.createArrayData(key)
		for i in range(10):
			test_random_IPv6.updateArrayData(key, random_tool.random_IPv6())
		test_random_IPv6.print_json()

	### TEST: random_macAddress ###
	def TEST_random_macAddress(self):
		test_random_macAddress = dataStructure()
		key = 'random_macAddress'
		test_random_macAddress.createCommonData("TEST")
		test_random_macAddress.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_macAddress.createArrayData(key)
		for i in range(10):
			test_random_macAddress.updateArrayData(key, random_tool.random_macAddress())
		test_random_macAddress.print_json()

	### TEST: random_version ###
	def TEST_random_version(self):
		test_random_version = dataStructure()
		key = 'random_version'
		test_random_version.createCommonData("TEST")
		test_random_version.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_version.createArrayData(key)
		for i in range(10):
			test_random_version.updateArrayData(key, random_tool.random_version())
		test_random_version.print_json()

	### TEST: random_bitcoinAddress ###
	def TEST_random_bitcoinAddress(self):
		test_random_bitcoinAddress = dataStructure()
		key = 'random_bitcoinAddress'
		test_random_bitcoinAddress.createCommonData("TEST")
		test_random_bitcoinAddress.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_bitcoinAddress.createArrayData(key)
		for i in range(10):
			test_random_bitcoinAddress.updateArrayData(key, random_tool.random_bitcoinAddress())
		test_random_bitcoinAddress.print_json()

	### TEST: random_creditCard ###
	def TEST_random_creditCard(self):
		test_random_creditCard = dataStructure()
		key = 'random_creditCard'
		test_random_creditCard.createCommonData("TEST")
		test_random_creditCard.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_creditCard.createArrayData(key)
		for i in range(10):
			test_random_creditCard.updateArrayData(key, random_tool.random_creditCard())
		test_random_creditCard.print_json()

	### TEST: random_date ###
	def TEST_random_date(self):
		test_random_date = dataStructure()
		key = 'random_date'
		test_random_date.createCommonData("TEST")
		test_random_date.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_date.createArrayData(key)
		for i in range(10):
			test_random_date.updateArrayData(key, random_tool.random_date())
		test_random_date.print_json()

	### TEST: random_fileNameWithExtension ###
	def TEST_random_fileNameWithExtension(self):
		test_random_fileNameWithExtension = dataStructure()
		key = 'random_fileNameWithExtension'
		test_random_fileNameWithExtension.createCommonData("TEST")
		test_random_fileNameWithExtension.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_fileNameWithExtension.createArrayData(key)
		for i in range(10):
			test_random_fileNameWithExtension.updateArrayData(key, random_tool.random_fileNameWithExtension())
		test_random_fileNameWithExtension.print_json()

	### TEST: random_hexColorCode ###
	def TEST_random_hexColorCode(self):
		test_random_hexColorCode = dataStructure()
		key = 'random_hexColorCode'
		test_random_hexColorCode.createCommonData("TEST")
		test_random_hexColorCode.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_hexColorCode.createArrayData(key)
		for i in range(10):
			test_random_hexColorCode.updateArrayData(key, random_tool.random_hexColorCode())
		test_random_hexColorCode.print_json()

	### TEST: random_SHA256 ###
	def TEST_random_SHA256(self):
		test_random_SHA256 = dataStructure()
		key = 'random_SHA256'
		test_random_SHA256.createCommonData("TEST")
		test_random_SHA256.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_SHA256.createArrayData(key)
		for i in range(10):
			test_random_SHA256.updateArrayData(key, random_tool.random_SHA256())
		test_random_SHA256.print_json()

	### TEST: random_phoneNumber ###
	def TEST_random_phoneNumber(self):
		test_random_phoneNumber = dataStructure()
		key = 'random_phoneNumber'
		test_random_phoneNumber.createCommonData("TEST")
		test_random_phoneNumber.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_phoneNumber.createArrayData(key)
		for i in range(10):
			test_random_phoneNumber.updateArrayData(key, random_tool.random_phoneNumber())
		test_random_phoneNumber.print_json()

	### TEST: random_streetNameAndAddress ###
	def TEST_random_streetNameAndAddress(self):
		test_random_streetNameAndAddress = dataStructure()
		key = 'random_streetNameAndAddress'
		test_random_streetNameAndAddress.createCommonData("TEST")
		test_random_streetNameAndAddress.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_streetNameAndAddress.createArrayData(key)
		for i in range(10):
			test_random_streetNameAndAddress.updateArrayData(key, random_tool.random_streetNameAndAddress())
		test_random_streetNameAndAddress.print_json()

	### TEST: random_password ###
	def TEST_random_password(self):
		test_random_password = dataStructure()
		key = 'random_password'
		test_random_password.createCommonData("TEST")
		test_random_password.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_password.createArrayData(key)
		for i in range(10):
			test_random_password.updateArrayData(key, random_tool.random_password())
		test_random_password.print_json()

	### TEST: random_number ###
	def TEST_random_number(self):
		test_random_number = dataStructure()
		key = 'random_number'
		test_random_number.createCommonData("TEST")
		test_random_number.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_number.createArrayData(key)
		for i in range(10):
			test_random_number.updateArrayData(key, random_tool.random_number())
		test_random_number.print_json()

	### TEST: random_time ###
	def TEST_random_time(self):
		test_random_time = dataStructure()
		key = 'random_time'
		test_random_time.createCommonData("TEST")
		test_random_time.updateCommonData("TEST", random_tool.random_customdata([key]))
		test_random_time.createArrayData(key)
		for i in range(10):
			test_random_time.updateArrayData(key, random_tool.random_time())
		test_random_time.print_json()

##==================== Call Testcase ====================##
test_object = testAPI()
test_object.TEST_random_animalName()
test_object.TEST_random_appBundleID()
test_object.TEST_random_appName()
test_object.TEST_random_avatar()
test_object.TEST_random_boolean()
test_object.TEST_random_carBrand()
test_object.TEST_random_carModel()
test_object.TEST_random_city()
test_object.TEST_random_color()
test_object.TEST_random_companyName()
test_object.TEST_random_contrucionHeavyEquipment()
test_object.TEST_random_contrucionMaterial()
test_object.TEST_random_contrucionRole()
test_object.TEST_random_contrucionTrade()
test_object.TEST_random_country()
test_object.TEST_random_countryCode()
test_object.TEST_random_creditCardType()
test_object.TEST_random_currency()
test_object.TEST_random_currencyCode()
test_object.TEST_random_department()
test_object.TEST_random_domain()
test_object.TEST_random_dummyImageURL()
test_object.TEST_random_fileExtension()
test_object.TEST_random_fileName()
test_object.TEST_random_firstName()
test_object.TEST_random_jobTitle()
test_object.TEST_random_language()
test_object.TEST_random_lastName()
test_object.TEST_random_productGrocery()
test_object.TEST_random_streetName()
test_object.TEST_random_timeZone()
test_object.TEST_random_gender()
test_object.TEST_random_programmingLanguage()
test_object.TEST_random_dayWeek()
test_object.TEST_random_month()
test_object.TEST_random_customdata()
test_object.TEST_random_fullName()
test_object.TEST_random_userName()
test_object.TEST_random_year()
test_object.TEST_random_email()
test_object.TEST_random_IPv4()
test_object.TEST_random_IPv6()
test_object.TEST_random_macAddress()
test_object.TEST_random_version()
test_object.TEST_random_bitcoinAddress()
test_object.TEST_random_creditCard()
test_object.TEST_random_date()
test_object.TEST_random_fileNameWithExtension()
test_object.TEST_random_hexColorCode()
test_object.TEST_random_SHA256()
test_object.TEST_random_phoneNumber()
test_object.TEST_random_streetNameAndAddress()
test_object.TEST_random_password()
test_object.TEST_random_number()
test_object.TEST_random_time()