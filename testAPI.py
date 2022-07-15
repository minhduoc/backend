
from random_functions import api
from dataStructure import dataStructure
class testAPI():
	def __init__(self):
		global random_tool
		random_tool = api()

	### TEST: random_animalname ###
	def TEST_random_animalname(self):
		test_random_animalname = dataStructure()
		key = 'random_animalname'
		test_random_animalname.createCommonData("TEST")
		test_random_animalname.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_animalname.createArrayData(key)
		for i in range(100):
			test_random_animalname.updateArrayData(key, random_tool.random_animalname())
		test_random_animalname.print_json()

	### TEST: random_appbundleid ###
	def TEST_random_appbundleid(self):
		test_random_appbundleid = dataStructure()
		key = 'random_appbundleid'
		test_random_appbundleid.createCommonData("TEST")
		test_random_appbundleid.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_appbundleid.createArrayData(key)
		for i in range(100):
			test_random_appbundleid.updateArrayData(key, random_tool.random_appbundleid())
		test_random_appbundleid.print_json()

	### TEST: random_appname ###
	def TEST_random_appname(self):
		test_random_appname = dataStructure()
		key = 'random_appname'
		test_random_appname.createCommonData("TEST")
		test_random_appname.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_appname.createArrayData(key)
		for i in range(100):
			test_random_appname.updateArrayData(key, random_tool.random_appname())
		test_random_appname.print_json()

	### TEST: random_avatar ###
	def TEST_random_avatar(self):
		test_random_avatar = dataStructure()
		key = 'random_avatar'
		test_random_avatar.createCommonData("TEST")
		test_random_avatar.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_avatar.createArrayData(key)
		for i in range(100):
			test_random_avatar.updateArrayData(key, random_tool.random_avatar())
		test_random_avatar.print_json()

	### TEST: random_boolean ###
	def TEST_random_boolean(self):
		test_random_boolean = dataStructure()
		key = 'random_boolean'
		test_random_boolean.createCommonData("TEST")
		test_random_boolean.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_boolean.createArrayData(key)
		for i in range(100):
			test_random_boolean.updateArrayData(key, random_tool.random_boolean())
		test_random_boolean.print_json()

	### TEST: random_carbrand ###
	def TEST_random_carbrand(self):
		test_random_carbrand = dataStructure()
		key = 'random_carbrand'
		test_random_carbrand.createCommonData("TEST")
		test_random_carbrand.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_carbrand.createArrayData(key)
		for i in range(100):
			test_random_carbrand.updateArrayData(key, random_tool.random_carbrand())
		test_random_carbrand.print_json()

	### TEST: random_carmodel ###
	def TEST_random_carmodel(self):
		test_random_carmodel = dataStructure()
		key = 'random_carmodel'
		test_random_carmodel.createCommonData("TEST")
		test_random_carmodel.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_carmodel.createArrayData(key)
		for i in range(100):
			test_random_carmodel.updateArrayData(key, random_tool.random_carmodel())
		test_random_carmodel.print_json()

	### TEST: random_city ###
	def TEST_random_city(self):
		test_random_city = dataStructure()
		key = 'random_city'
		test_random_city.createCommonData("TEST")
		test_random_city.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_city.createArrayData(key)
		for i in range(100):
			test_random_city.updateArrayData(key, random_tool.random_city())
		test_random_city.print_json()

	### TEST: random_color ###
	def TEST_random_color(self):
		test_random_color = dataStructure()
		key = 'random_color'
		test_random_color.createCommonData("TEST")
		test_random_color.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_color.createArrayData(key)
		for i in range(100):
			test_random_color.updateArrayData(key, random_tool.random_color())
		test_random_color.print_json()

	### TEST: random_companyname ###
	def TEST_random_companyname(self):
		test_random_companyname = dataStructure()
		key = 'random_companyname'
		test_random_companyname.createCommonData("TEST")
		test_random_companyname.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_companyname.createArrayData(key)
		for i in range(100):
			test_random_companyname.updateArrayData(key, random_tool.random_companyname())
		test_random_companyname.print_json()

	### TEST: random_constructionheavyequipment ###
	def TEST_random_constructionheavyequipment(self):
		test_random_constructionheavyequipment = dataStructure()
		key = 'random_constructionheavyequipment'
		test_random_constructionheavyequipment.createCommonData("TEST")
		test_random_constructionheavyequipment.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_constructionheavyequipment.createArrayData(key)
		for i in range(100):
			test_random_constructionheavyequipment.updateArrayData(key, random_tool.random_constructionheavyequipment())
		test_random_constructionheavyequipment.print_json()

	### TEST: random_constructionmaterial ###
	def TEST_random_constructionmaterial(self):
		test_random_constructionmaterial = dataStructure()
		key = 'random_constructionmaterial'
		test_random_constructionmaterial.createCommonData("TEST")
		test_random_constructionmaterial.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_constructionmaterial.createArrayData(key)
		for i in range(100):
			test_random_constructionmaterial.updateArrayData(key, random_tool.random_constructionmaterial())
		test_random_constructionmaterial.print_json()

	### TEST: random_constructionrole ###
	def TEST_random_constructionrole(self):
		test_random_constructionrole = dataStructure()
		key = 'random_constructionrole'
		test_random_constructionrole.createCommonData("TEST")
		test_random_constructionrole.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_constructionrole.createArrayData(key)
		for i in range(100):
			test_random_constructionrole.updateArrayData(key, random_tool.random_constructionrole())
		test_random_constructionrole.print_json()

	### TEST: random_constructiontrade ###
	def TEST_random_constructiontrade(self):
		test_random_constructiontrade = dataStructure()
		key = 'random_constructiontrade'
		test_random_constructiontrade.createCommonData("TEST")
		test_random_constructiontrade.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_constructiontrade.createArrayData(key)
		for i in range(100):
			test_random_constructiontrade.updateArrayData(key, random_tool.random_constructiontrade())
		test_random_constructiontrade.print_json()

	### TEST: random_country ###
	def TEST_random_country(self):
		test_random_country = dataStructure()
		key = 'random_country'
		test_random_country.createCommonData("TEST")
		test_random_country.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_country.createArrayData(key)
		for i in range(100):
			test_random_country.updateArrayData(key, random_tool.random_country())
		test_random_country.print_json()

	### TEST: random_countrycode ###
	def TEST_random_countrycode(self):
		test_random_countrycode = dataStructure()
		key = 'random_countrycode'
		test_random_countrycode.createCommonData("TEST")
		test_random_countrycode.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_countrycode.createArrayData(key)
		for i in range(100):
			test_random_countrycode.updateArrayData(key, random_tool.random_countrycode())
		test_random_countrycode.print_json()

	### TEST: random_creditcardtype ###
	def TEST_random_creditcardtype(self):
		test_random_creditcardtype = dataStructure()
		key = 'random_creditcardtype'
		test_random_creditcardtype.createCommonData("TEST")
		test_random_creditcardtype.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_creditcardtype.createArrayData(key)
		for i in range(100):
			test_random_creditcardtype.updateArrayData(key, random_tool.random_creditcardtype())
		test_random_creditcardtype.print_json()

	### TEST: random_currency ###
	def TEST_random_currency(self):
		test_random_currency = dataStructure()
		key = 'random_currency'
		test_random_currency.createCommonData("TEST")
		test_random_currency.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_currency.createArrayData(key)
		for i in range(100):
			test_random_currency.updateArrayData(key, random_tool.random_currency())
		test_random_currency.print_json()

	### TEST: random_currencycode ###
	def TEST_random_currencycode(self):
		test_random_currencycode = dataStructure()
		key = 'random_currencycode'
		test_random_currencycode.createCommonData("TEST")
		test_random_currencycode.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_currencycode.createArrayData(key)
		for i in range(100):
			test_random_currencycode.updateArrayData(key, random_tool.random_currencycode())
		test_random_currencycode.print_json()

	### TEST: random_department ###
	def TEST_random_department(self):
		test_random_department = dataStructure()
		key = 'random_department'
		test_random_department.createCommonData("TEST")
		test_random_department.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_department.createArrayData(key)
		for i in range(100):
			test_random_department.updateArrayData(key, random_tool.random_department())
		test_random_department.print_json()

	### TEST: random_domain ###
	def TEST_random_domain(self):
		test_random_domain = dataStructure()
		key = 'random_domain'
		test_random_domain.createCommonData("TEST")
		test_random_domain.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_domain.createArrayData(key)
		for i in range(100):
			test_random_domain.updateArrayData(key, random_tool.random_domain())
		test_random_domain.print_json()

	### TEST: random_dummyimageurl ###
	def TEST_random_dummyimageurl(self):
		test_random_dummyimageurl = dataStructure()
		key = 'random_dummyimageurl'
		test_random_dummyimageurl.createCommonData("TEST")
		test_random_dummyimageurl.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_dummyimageurl.createArrayData(key)
		for i in range(100):
			test_random_dummyimageurl.updateArrayData(key, random_tool.random_dummyimageurl())
		test_random_dummyimageurl.print_json()

	### TEST: random_fileextension ###
	def TEST_random_fileextension(self):
		test_random_fileextension = dataStructure()
		key = 'random_fileextension'
		test_random_fileextension.createCommonData("TEST")
		test_random_fileextension.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_fileextension.createArrayData(key)
		for i in range(100):
			test_random_fileextension.updateArrayData(key, random_tool.random_fileextension())
		test_random_fileextension.print_json()

	### TEST: random_filename ###
	def TEST_random_filename(self):
		test_random_filename = dataStructure()
		key = 'random_filename'
		test_random_filename.createCommonData("TEST")
		test_random_filename.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_filename.createArrayData(key)
		for i in range(100):
			test_random_filename.updateArrayData(key, random_tool.random_filename())
		test_random_filename.print_json()

	### TEST: random_firstname ###
	def TEST_random_firstname(self):
		test_random_firstname = dataStructure()
		key = 'random_firstname'
		test_random_firstname.createCommonData("TEST")
		test_random_firstname.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_firstname.createArrayData(key)
		for i in range(100):
			test_random_firstname.updateArrayData(key, random_tool.random_firstname())
		test_random_firstname.print_json()

	### TEST: random_jobnitle ###
	def TEST_random_jobnitle(self):
		test_random_jobnitle = dataStructure()
		key = 'random_jobnitle'
		test_random_jobnitle.createCommonData("TEST")
		test_random_jobnitle.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_jobnitle.createArrayData(key)
		for i in range(100):
			test_random_jobnitle.updateArrayData(key, random_tool.random_jobnitle())
		test_random_jobnitle.print_json()

	### TEST: random_language ###
	def TEST_random_language(self):
		test_random_language = dataStructure()
		key = 'random_language'
		test_random_language.createCommonData("TEST")
		test_random_language.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_language.createArrayData(key)
		for i in range(100):
			test_random_language.updateArrayData(key, random_tool.random_language())
		test_random_language.print_json()

	### TEST: random_lastname ###
	def TEST_random_lastname(self):
		test_random_lastname = dataStructure()
		key = 'random_lastname'
		test_random_lastname.createCommonData("TEST")
		test_random_lastname.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_lastname.createArrayData(key)
		for i in range(100):
			test_random_lastname.updateArrayData(key, random_tool.random_lastname())
		test_random_lastname.print_json()

	### TEST: random_productgrocery ###
	def TEST_random_productgrocery(self):
		test_random_productgrocery = dataStructure()
		key = 'random_productgrocery'
		test_random_productgrocery.createCommonData("TEST")
		test_random_productgrocery.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_productgrocery.createArrayData(key)
		for i in range(100):
			test_random_productgrocery.updateArrayData(key, random_tool.random_productgrocery())
		test_random_productgrocery.print_json()

	### TEST: random_streetname ###
	def TEST_random_streetname(self):
		test_random_streetname = dataStructure()
		key = 'random_streetname'
		test_random_streetname.createCommonData("TEST")
		test_random_streetname.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_streetname.createArrayData(key)
		for i in range(100):
			test_random_streetname.updateArrayData(key, random_tool.random_streetname())
		test_random_streetname.print_json()

	### TEST: random_timezone ###
	def TEST_random_timezone(self):
		test_random_timezone = dataStructure()
		key = 'random_timezone'
		test_random_timezone.createCommonData("TEST")
		test_random_timezone.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_timezone.createArrayData(key)
		for i in range(100):
			test_random_timezone.updateArrayData(key, random_tool.random_timezone())
		test_random_timezone.print_json()

	### TEST: random_gender ###
	def TEST_random_gender(self):
		test_random_gender = dataStructure()
		key = 'random_gender'
		test_random_gender.createCommonData("TEST")
		test_random_gender.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_gender.createArrayData(key)
		for i in range(100):
			test_random_gender.updateArrayData(key, random_tool.random_gender())
		test_random_gender.print_json()

	### TEST: random_programminglanguage ###
	def TEST_random_programminglanguage(self):
		test_random_programminglanguage = dataStructure()
		key = 'random_programminglanguage'
		test_random_programminglanguage.createCommonData("TEST")
		test_random_programminglanguage.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_programminglanguage.createArrayData(key)
		for i in range(100):
			test_random_programminglanguage.updateArrayData(key, random_tool.random_programminglanguage())
		test_random_programminglanguage.print_json()

	### TEST: random_dayweek ###
	def TEST_random_dayweek(self):
		test_random_dayweek = dataStructure()
		key = 'random_dayweek'
		test_random_dayweek.createCommonData("TEST")
		test_random_dayweek.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_dayweek.createArrayData(key)
		for i in range(100):
			test_random_dayweek.updateArrayData(key, random_tool.random_dayweek())
		test_random_dayweek.print_json()

	### TEST: random_month ###
	def TEST_random_month(self):
		test_random_month = dataStructure()
		key = 'random_month'
		test_random_month.createCommonData("TEST")
		test_random_month.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_month.createArrayData(key)
		for i in range(100):
			test_random_month.updateArrayData(key, random_tool.random_month())
		test_random_month.print_json()

	### TEST: random_randomlist ###
	def TEST_random_randomlist(self):
		test_random_randomlist = dataStructure()
		key = 'random_randomlist'
		test_random_randomlist.createCommonData("TEST")
		test_random_randomlist.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_randomlist.createArrayData(key)
		for i in range(100):
			test_random_randomlist.updateArrayData(key, random_tool.random_randomlist())
		test_random_randomlist.print_json()

	### TEST: random_fullname ###
	def TEST_random_fullname(self):
		test_random_fullname = dataStructure()
		key = 'random_fullname'
		test_random_fullname.createCommonData("TEST")
		test_random_fullname.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_fullname.createArrayData(key)
		for i in range(100):
			test_random_fullname.updateArrayData(key, random_tool.random_fullname())
		test_random_fullname.print_json()

	### TEST: random_username ###
	def TEST_random_username(self):
		test_random_username = dataStructure()
		key = 'random_username'
		test_random_username.createCommonData("TEST")
		test_random_username.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_username.createArrayData(key)
		for i in range(100):
			test_random_username.updateArrayData(key, random_tool.random_username())
		test_random_username.print_json()

	### TEST: random_year ###
	def TEST_random_year(self):
		test_random_year = dataStructure()
		key = 'random_year'
		test_random_year.createCommonData("TEST")
		test_random_year.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_year.createArrayData(key)
		for i in range(100):
			test_random_year.updateArrayData(key, random_tool.random_year())
		test_random_year.print_json()

	### TEST: random_email ###
	def TEST_random_email(self):
		test_random_email = dataStructure()
		key = 'random_email'
		test_random_email.createCommonData("TEST")
		test_random_email.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_email.createArrayData(key)
		for i in range(100):
			test_random_email.updateArrayData(key, random_tool.random_email())
		test_random_email.print_json()

	### TEST: random_ipv4 ###
	def TEST_random_ipv4(self):
		test_random_ipv4 = dataStructure()
		key = 'random_ipv4'
		test_random_ipv4.createCommonData("TEST")
		test_random_ipv4.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_ipv4.createArrayData(key)
		for i in range(100):
			test_random_ipv4.updateArrayData(key, random_tool.random_ipv4())
		test_random_ipv4.print_json()

	### TEST: random_ipv6 ###
	def TEST_random_ipv6(self):
		test_random_ipv6 = dataStructure()
		key = 'random_ipv6'
		test_random_ipv6.createCommonData("TEST")
		test_random_ipv6.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_ipv6.createArrayData(key)
		for i in range(100):
			test_random_ipv6.updateArrayData(key, random_tool.random_ipv6())
		test_random_ipv6.print_json()

	### TEST: random_macaddress ###
	def TEST_random_macaddress(self):
		test_random_macaddress = dataStructure()
		key = 'random_macaddress'
		test_random_macaddress.createCommonData("TEST")
		test_random_macaddress.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_macaddress.createArrayData(key)
		for i in range(100):
			test_random_macaddress.updateArrayData(key, random_tool.random_macaddress())
		test_random_macaddress.print_json()

	### TEST: random_version ###
	def TEST_random_version(self):
		test_random_version = dataStructure()
		key = 'random_version'
		test_random_version.createCommonData("TEST")
		test_random_version.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_version.createArrayData(key)
		for i in range(100):
			test_random_version.updateArrayData(key, random_tool.random_version())
		test_random_version.print_json()

	### TEST: random_bitcoinaddress ###
	def TEST_random_bitcoinaddress(self):
		test_random_bitcoinaddress = dataStructure()
		key = 'random_bitcoinaddress'
		test_random_bitcoinaddress.createCommonData("TEST")
		test_random_bitcoinaddress.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_bitcoinaddress.createArrayData(key)
		for i in range(100):
			test_random_bitcoinaddress.updateArrayData(key, random_tool.random_bitcoinaddress())
		test_random_bitcoinaddress.print_json()

	### TEST: random_creditcard ###
	def TEST_random_creditcard(self):
		test_random_creditcard = dataStructure()
		key = 'random_creditcard'
		test_random_creditcard.createCommonData("TEST")
		test_random_creditcard.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_creditcard.createArrayData(key)
		for i in range(100):
			test_random_creditcard.updateArrayData(key, random_tool.random_creditcard())
		test_random_creditcard.print_json()

	### TEST: random_date ###
	def TEST_random_date(self):
		test_random_date = dataStructure()
		key = 'random_date'
		test_random_date.createCommonData("TEST")
		test_random_date.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_date.createArrayData(key)
		for i in range(100):
			test_random_date.updateArrayData(key, random_tool.random_date())
		test_random_date.print_json()

	### TEST: random_filenamewithextension ###
	def TEST_random_filenamewithextension(self):
		test_random_filenamewithextension = dataStructure()
		key = 'random_filenamewithextension'
		test_random_filenamewithextension.createCommonData("TEST")
		test_random_filenamewithextension.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_filenamewithextension.createArrayData(key)
		for i in range(100):
			test_random_filenamewithextension.updateArrayData(key, random_tool.random_filenamewithextension())
		test_random_filenamewithextension.print_json()

	### TEST: random_hexcolorcode ###
	def TEST_random_hexcolorcode(self):
		test_random_hexcolorcode = dataStructure()
		key = 'random_hexcolorcode'
		test_random_hexcolorcode.createCommonData("TEST")
		test_random_hexcolorcode.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_hexcolorcode.createArrayData(key)
		for i in range(100):
			test_random_hexcolorcode.updateArrayData(key, random_tool.random_hexcolorcode())
		test_random_hexcolorcode.print_json()

	### TEST: random_sha256 ###
	def TEST_random_sha256(self):
		test_random_sha256 = dataStructure()
		key = 'random_sha256'
		test_random_sha256.createCommonData("TEST")
		test_random_sha256.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_sha256.createArrayData(key)
		for i in range(100):
			test_random_sha256.updateArrayData(key, random_tool.random_sha256())
		test_random_sha256.print_json()

	### TEST: random_phonenumber ###
	def TEST_random_phonenumber(self):
		test_random_phonenumber = dataStructure()
		key = 'random_phonenumber'
		test_random_phonenumber.createCommonData("TEST")
		test_random_phonenumber.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_phonenumber.createArrayData(key)
		for i in range(100):
			test_random_phonenumber.updateArrayData(key, random_tool.random_phonenumber())
		test_random_phonenumber.print_json()

	### TEST: random_streetnameandaddress ###
	def TEST_random_streetnameandaddress(self):
		test_random_streetnameandaddress = dataStructure()
		key = 'random_streetnameandaddress'
		test_random_streetnameandaddress.createCommonData("TEST")
		test_random_streetnameandaddress.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_streetnameandaddress.createArrayData(key)
		for i in range(100):
			test_random_streetnameandaddress.updateArrayData(key, random_tool.random_streetnameandaddress())
		test_random_streetnameandaddress.print_json()

	### TEST: random_password ###
	def TEST_random_password(self):
		test_random_password = dataStructure()
		key = 'random_password'
		test_random_password.createCommonData("TEST")
		test_random_password.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_password.createArrayData(key)
		for i in range(100):
			test_random_password.updateArrayData(key, random_tool.random_password())
		test_random_password.print_json()

	### TEST: random_number ###
	def TEST_random_number(self):
		test_random_number = dataStructure()
		key = 'random_number'
		test_random_number.createCommonData("TEST")
		test_random_number.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_number.createArrayData(key)
		for i in range(100):
			test_random_number.updateArrayData(key, random_tool.random_number())
		test_random_number.print_json()

	### TEST: random_time ###
	def TEST_random_time(self):
		test_random_time = dataStructure()
		key = 'random_time'
		test_random_time.createCommonData("TEST")
		test_random_time.updateCommonData("TEST", random_tool.random_randomlist([key]))
		test_random_time.createArrayData(key)
		for i in range(100):
			test_random_time.updateArrayData(key, random_tool.random_time())
		test_random_time.print_json()

##==================== Call Testcase ====================##
test_object = testAPI()
test_object.TEST_random_animalname()
test_object.TEST_random_appbundleid()
test_object.TEST_random_appname()
test_object.TEST_random_avatar()
test_object.TEST_random_boolean()
test_object.TEST_random_carbrand()
test_object.TEST_random_carmodel()
test_object.TEST_random_city()
test_object.TEST_random_color()
test_object.TEST_random_companyname()
test_object.TEST_random_constructionheavyequipment()
test_object.TEST_random_constructionmaterial()
test_object.TEST_random_constructionrole()
test_object.TEST_random_constructiontrade()
test_object.TEST_random_country()
test_object.TEST_random_countrycode()
test_object.TEST_random_creditcardtype()
test_object.TEST_random_currency()
test_object.TEST_random_currencycode()
test_object.TEST_random_department()
test_object.TEST_random_domain()
test_object.TEST_random_dummyimageurl()
test_object.TEST_random_fileextension()
test_object.TEST_random_filename()
test_object.TEST_random_firstname()
test_object.TEST_random_jobnitle()
test_object.TEST_random_language()
test_object.TEST_random_lastname()
test_object.TEST_random_productgrocery()
test_object.TEST_random_streetname()
test_object.TEST_random_timezone()
test_object.TEST_random_gender()
test_object.TEST_random_programminglanguage()
test_object.TEST_random_dayweek()
test_object.TEST_random_month()
test_object.TEST_random_randomlist()
test_object.TEST_random_fullname()
test_object.TEST_random_username()
test_object.TEST_random_year()
test_object.TEST_random_email()
test_object.TEST_random_ipv4()
test_object.TEST_random_ipv6()
test_object.TEST_random_macaddress()
test_object.TEST_random_version()
test_object.TEST_random_bitcoinaddress()
test_object.TEST_random_creditcard()
test_object.TEST_random_date()
test_object.TEST_random_filenamewithextension()
test_object.TEST_random_hexcolorcode()
test_object.TEST_random_sha256()
test_object.TEST_random_phonenumber()
test_object.TEST_random_streetnameandaddress()
test_object.TEST_random_password()
test_object.TEST_random_number()
test_object.TEST_random_time()