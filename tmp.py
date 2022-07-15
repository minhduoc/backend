import calendar
import random
import string
import re
import json
# import requests

class database():
	def __init__(self):

		self.animalName = ['Mynah, indian', 'Monitor, white-throated', 'Heron, little', 'Crested barbet',
						   'Lemur, sportive', 'South American meadowlark (unidentified)', 'Monkey, rhesus',
						   'Bleu, blue-breasted cordon', 'Monitor lizard (unidentified)', 'Indian porcupine',
						   'Snow goose', 'Frilled dragon', 'Python, carpet', 'Stork, european', 'Fox, silver-backed',
						   'Hornbill, southern ground', 'Ring-tailed gecko', 'White-lipped peccary',
						   'Silver-backed fox', 'Godwit, hudsonian', 'Elephant, asian', 'Nighthawk, common',
						   'Loris, slender', 'Kafue flats lechwe', 'Red-breasted cockatoo', 'Common dolphin',
						   'Crimson-breasted shrike', 'Cat, toddy', 'Waxbill, blue', 'Jabiru stork', 'Llama',
						   'Weeper capuchin', 'Long-crested hawk eagle', 'American crow',
						   'Southern white-crowned shrike', 'Penguin, magellanic', 'Seal, common',
						   'Corella, long-billed', 'Cobra, cape', 'Gerenuk', 'Jacana, african',
						   'Yellow-headed caracara', 'Striated heron', 'Three-banded plover', 'Plains zebra',
						   'Wagtail, african pied', 'Porcupine, indian', 'Red brocket', 'Waxbill, black-cheeked',
						   'Cormorant, large', 'Mississippi alligator', 'Hawk, galapagos', 'Cormorant, flightless',
						   "Azara's zorro", 'Nile crocodile', 'Asian foreset tortoise', 'Blue and gold macaw',
						   'Japanese macaque', 'Bald eagle', 'Australian masked owl', 'Snake, carpet',
						   'Langur, hanuman', 'Malachite kingfisher', 'Owl, white-browed', 'Eurasian hoopoe',
						   'Curlew, black', 'Raven, cape', 'Worm snake (unidentified)', 'Whip-tailed wallaby',
						   'Starling, red-shouldered glossy', 'Woodrat (unidentified)', 'Eastern cottontail rabbit',
						   'Common raccoon', 'Oribi', 'Agouti', 'White-mantled colobus', 'Eastern dwarf mongoose',
						   'Common eland', 'Creeper, black-tailed tree', 'Sugar glider', 'Russian dragonfly',
						   'Tawny eagle', 'Crane, wattled', 'Springbuck', 'Red kangaroo', 'Little heron',
						   'Monkey, red howler', 'Southern elephant seal', 'Camel, dromedary', 'Flicker, campo',
						   'Possum, pygmy', 'Caracara (unidentified)', 'Bandicoot, southern brown', 'Purple grenadier',
						   'Madagascar hawk owl']

		self.appBundleID = ['com.gravatar.Y-Solowarm', 'com.answers.Alpha', 'jp.or.plala.Trippledex',
							'com.soundcloud.Pannier', 'com.slate.Biodex', 'cn.360.Konklux', 'com.wunderground.Alpha',
							'com.cnet.Prodder', 'com.blogs.Lotstring', 'gov.ed.Andalax', 'com.techcrunch.Gembucket',
							'com.issuu.Lotlux', 'org.unesco.Mat Lam Tam', 'com.livejournal.Rank',
							'com.nationalgeographic.Ventosanzap', 'gl.goo.Sonsing', 'edu.utexas.Fintone',
							'com.nydailynews.Zoolab', 'com.sun.Asoka', 'com.qq.Bigtax', 'cn.com.sina.Andalax',
							'it.tuttocitta.Sonair', 'com.youku.Konklux', 'com.bloglines.Sub-Ex', 'edu.si.Span',
							'com.microsoft.Stim', 'com.hubpages.Redhold', 'com.indiatimes.Tresom', 'com.mtv.Zathin',
							'com.pcworld.Duobam', 'net.cpanel.Wrapsafe', 'com.cafepress.Stringtough',
							'net.discuz.Y-Solowarm', 'org.w3.Konklab', 'com.chicagotribune.Veribet',
							'jp.co.yahoo.Cookley', 'gov.hhs.Overhold', 'com.sbwire.Veribet', 'com.foxnews.Namfix',
							'it.tuttocitta.Toughjoyfax', 'com.time.Fixflex', 'com.tinypic.Fintone',
							'uk.co.123-reg.Y-Solowarm', 'br.com.google.Treeflex', 'com.mashable.Vagram', 'com.wiley.It',
							'com.blogs.Sonair', 'com.nature.Solarbreeze', 'gov.senate.Kanlam', 'com.vinaora.Biodex',
							'gov.va.Subin', 'com.bloglovin.Solarbreeze', 'com.kickstarter.Ronstring',
							'org.unicef.Hatity', 'net.ovh.Aerified', 'com.cargocollective.It', 'ch.admin.Alpha',
							'io.soup.Hatity', 'com.ifeng.Pannier', 'com.seattletimes.Matsoft', 'uk.co.google.Lotlux',
							'com.chicagotribune.Alphazap', 'fr.free.Zoolab', 'com.hexun.Zamit', 'gov.va.Home Ing',
							'io.pen.Tres-Zap', 'com.bloomberg.Aerified', 'com.netlog.Namfix',
							'ru.odnoklassniki.Transcof', 'de.t-online.Latlux', 'com.blogtalkradio.Bitchip',
							'net.php.Prodder', 'gl.goo.Asoka', 'org.opensource.Holdlamis', 'com.topsy.Pannier',
							'com.geocities.Tempsoft', 'org.mozilla.Y-find', 'com.cisco.Gembucket', 'uk.gov.Treeflex',
							'org.unicef.Andalax', 'edu.ucsd.Otcom', 'com.deliciousdays.Ventosanzap', 'com.ted.Aerified',
							'org.redcross.Bitwolf', 'com.netscape.Cardify', 'com.washingtonpost.Konklab',
							'com.usnews.Voyatouch', 'info.aboutads.Y-find', 'com.nifty.Zamit', 'jp.ne.goo.Subin',
							'net.discuz.Asoka', 'com.wikia.Bamity', 'com.parallels.It', 'net.themeforest.Subin',
							'com.nbcnews.Holdlamis', 'uk.co.telegraph.Biodex', 'edu.si.Otcom', 'com.ycombinator.Duobam',
							'com.vinaora.Overhold', 'com.alibaba.Tempsoft']

		self.appName = ['Sonair', 'Sub-Ex', 'Domainer', 'Matsoft', 'Tres-Zap', 'Greenlam', 'Flowdesk', 'Stim', 'Y-find',
						'Lotstring', 'Y-Solowarm', 'Zoolab', 'Toughjoyfax', 'Quo Lux', 'Pannier', 'Viva', 'Konklab',
						'Otcom', 'Redhold', 'Zamit', 'Kanlam', 'Stronghold', 'Job', 'Daltfresh', 'Wrapsafe', 'Andalax',
						'Solarbreeze', 'Transcof', 'Fintone', 'Tin', 'Veribet', 'Lotlux', 'Fix San', 'Voltsillam',
						'Mat Lam Tam', 'Cookley', 'Hatity', 'Namfix', 'Zaam-Dox', 'Cardify', 'Ronstring', 'Asoka',
						'Bigtax',
						'Latlux', 'Span', 'Temp', 'Home Ing', 'Keylex', 'Zontrax', 'Bytecard', 'Alpha', 'Flexidy',
						'Opela',
						'Bitwolf', 'Biodex', 'Alphazap']

		self.avatar = ['ttps://robohash.org/nostrumearumdelectus.png?size=50x50&set=set1',
					   'https://robohash.org/velvitaesint.png?size=50x50&set=set1',
					   'https://robohash.org/autemquiex.png?size=50x50&set=set1',
					   'https://robohash.org/rationedoloremqueharum.png?size=50x50&set=set1',
					   'https://robohash.org/sequiquoiusto.png?size=50x50&set=set1',
					   'https://robohash.org/consequaturdictaprovident.png?size=50x50&set=set1',
					   'https://robohash.org/illumenimpossimus.png?size=50x50&set=set1',
					   'https://robohash.org/idmollitiaducimus.png?size=50x50&set=set1',
					   'https://robohash.org/atquepariatursoluta.png?size=50x50&set=set1',
					   'https://robohash.org/aliquammaioressit.png?size=50x50&set=set1',
					   'https://robohash.org/autetmagni.png?size=50x50&set=set1',
					   'https://robohash.org/laborumnoneos.png?size=50x50&set=set1',
					   'https://robohash.org/velitcommodiet.png?size=50x50&set=set1',
					   'https://robohash.org/architectoveroid.png?size=50x50&set=set1',
					   'https://robohash.org/providentapraesentium.png?size=50x50&set=set1',
					   'https://robohash.org/eosperspiciatissapiente.png?size=50x50&set=set1',
					   'https://robohash.org/explicabonemosunt.png?size=50x50&set=set1',
					   'https://robohash.org/laboriosamsequidolorum.png?size=50x50&set=set1',
					   'https://robohash.org/suscipitullamnesciunt.png?size=50x50&set=set1',
					   'https://robohash.org/quisveniamdolorem.png?size=50x50&set=set1',
					   'https://robohash.org/nemoadvel.png?size=50x50&set=set1',
					   'https://robohash.org/voluptatemdolorumrerum.png?size=50x50&set=set1',
					   'https://robohash.org/molestiaesaepeodio.png?size=50x50&set=set1',
					   'https://robohash.org/solutadoloribuscorrupti.png?size=50x50&set=set1',
					   'https://robohash.org/etsaepequia.png?size=50x50&set=set1',
					   'https://robohash.org/doloressedaut.png?size=50x50&set=set1',
					   'https://robohash.org/autamodi.png?size=50x50&set=set1',
					   'https://robohash.org/consequaturetreiciendis.png?size=50x50&set=set1',
					   'https://robohash.org/maximeipsaconsequatur.png?size=50x50&set=set1',
					   'https://robohash.org/etvelitet.png?size=50x50&set=set1',
					   'https://robohash.org/evenietliberoquos.png?size=50x50&set=set1',
					   'https://robohash.org/aspernaturpossimustempora.png?size=50x50&set=set1',
					   'https://robohash.org/nullaetet.png?size=50x50&set=set1',
					   'https://robohash.org/voluptatemuteveniet.png?size=50x50&set=set1',
					   'https://robohash.org/eumtotamplaceat.png?size=50x50&set=set1',
					   'https://robohash.org/culpavoluptaseum.png?size=50x50&set=set1',
					   'https://robohash.org/voluptatemsitdignissimos.png?size=50x50&set=set1',
					   'https://robohash.org/idexsuscipit.png?size=50x50&set=set1',
					   'https://robohash.org/magnamvoluptatumdebitis.png?size=50x50&set=set1',
					   'https://robohash.org/autinciduntveniam.png?size=50x50&set=set1',
					   'https://robohash.org/auteosdolores.png?size=50x50&set=set1',
					   'https://robohash.org/aspernaturanimicumque.png?size=50x50&set=set1',
					   'https://robohash.org/utmolestiasut.png?size=50x50&set=set1',
					   'https://robohash.org/remsintmaiores.png?size=50x50&set=set1',
					   'https://robohash.org/assumendasequiamet.png?size=50x50&set=set1',
					   'https://robohash.org/eumcorruptiet.png?size=50x50&set=set1',
					   'https://robohash.org/solutahicexercitationem.png?size=50x50&set=set1',
					   'https://robohash.org/aerrorsoluta.png?size=50x50&set=set1',
					   'https://robohash.org/sintnecessitatibusoccaecati.png?size=50x50&set=set1',
					   'https://robohash.org/deseruntquosdolorem.png?size=50x50&set=set1',
					   'https://robohash.org/suscipitametomnis.png?size=50x50&set=set1',
					   'https://robohash.org/porrocorporiscommodi.png?size=50x50&set=set1',
					   'https://robohash.org/atetest.png?size=50x50&set=set1',
					   'https://robohash.org/atfugaquia.png?size=50x50&set=set1',
					   'https://robohash.org/eumquosodio.png?size=50x50&set=set1',
					   'https://robohash.org/iustoetsimilique.png?size=50x50&set=set1',
					   'https://robohash.org/estetodit.png?size=50x50&set=set1',
					   'https://robohash.org/estautvoluptatibus.png?size=50x50&set=set1',
					   'https://robohash.org/quisquamquissuscipit.png?size=50x50&set=set1',
					   'https://robohash.org/utestaperiam.png?size=50x50&set=set1',
					   'https://robohash.org/ututalias.png?size=50x50&set=set1',
					   'https://robohash.org/doloretsed.png?size=50x50&set=set1',
					   'https://robohash.org/consequaturadipisciquo.png?size=50x50&set=set1',
					   'https://robohash.org/quodeseruntaccusantium.png?size=50x50&set=set1',
					   'https://robohash.org/ettemporibuset.png?size=50x50&set=set1',
					   'https://robohash.org/sitaspernaturet.png?size=50x50&set=set1',
					   'https://robohash.org/utconsequaturvel.png?size=50x50&set=set1',
					   'https://robohash.org/oditquasideserunt.png?size=50x50&set=set1',
					   'https://robohash.org/delenitivoluptatesint.png?size=50x50&set=set1',
					   'https://robohash.org/rationeeumpariatur.png?size=50x50&set=set1',
					   'https://robohash.org/accusamusaperiamconsequatur.png?size=50x50&set=set1',
					   'https://robohash.org/impeditidrepudiandae.png?size=50x50&set=set1',
					   'https://robohash.org/sedeaautem.png?size=50x50&set=set1',
					   'https://robohash.org/magniquaeaut.png?size=50x50&set=set1',
					   'https://robohash.org/aperiamhicoptio.png?size=50x50&set=set1',
					   'https://robohash.org/idexpeditaofficiis.png?size=50x50&set=set1',
					   'https://robohash.org/voluptatemomnissaepe.png?size=50x50&set=set1',
					   'https://robohash.org/perferendisexnatus.png?size=50x50&set=set1',
					   'https://robohash.org/magnamexpeditaiure.png?size=50x50&set=set1',
					   'https://robohash.org/doloribusvoluptasnon.png?size=50x50&set=set1',
					   'https://robohash.org/quibusdamverocommodi.png?size=50x50&set=set1',
					   'https://robohash.org/maioresiustoquam.png?size=50x50&set=set1',
					   'https://robohash.org/etliberoaut.png?size=50x50&set=set1',
					   'https://robohash.org/voluptatemaspernaturenim.png?size=50x50&set=set1',
					   'https://robohash.org/aspernaturetvoluptatum.png?size=50x50&set=set1',
					   'https://robohash.org/autvoluptaserror.png?size=50x50&set=set1',
					   'https://robohash.org/fugafacilisat.png?size=50x50&set=set1',
					   'https://robohash.org/eiusminimaquos.png?size=50x50&set=set1',
					   'https://robohash.org/autveritatisaccusantium.png?size=50x50&set=set1',
					   'https://robohash.org/utconsequatura.png?size=50x50&set=set1',
					   'https://robohash.org/consecteturdoloresquod.png?size=50x50&set=set1',
					   'https://robohash.org/nihilpariaturexercitationem.png?size=50x50&set=set1',
					   'https://robohash.org/eiusipsapossimus.png?size=50x50&set=set1',
					   'https://robohash.org/necessitatibuseosinventore.png?size=50x50&set=set1',
					   'https://robohash.org/eaqueomnisipsum.png?size=50x50&set=set1',
					   'https://robohash.org/etvelrerum.png?size=50x50&set=set1',
					   'https://robohash.org/asperioresvoluptatemeveniet.png?size=50x50&set=set1',
					   'https://robohash.org/nonexpeditaaliquam.png?size=50x50&set=set1',
					   'https://robohash.org/deseruntteneturvoluptatem.png?size=50x50&set=set1',
					   'https://robohash.org/voluptatedoloremquis.png?size=50x50&set=set1']

		self.boolean = ['false', 'true']

		self.carBrand = ['Hyundai', 'Mercedes-Benz', 'Audi', 'Kia', 'Buick', 'Dodge', 'Mitsubishi', 'BMW', 'Chevrolet',
						 'Oldsmobile', 'Bentley', 'Infiniti', 'Ford', 'GMC', 'Honda', 'Volkswagen', 'Pontiac',
						 'Plymouth', 'Mercury', 'Lincoln', 'Nissan', 'Lamborghini', 'Lexus', 'Toyota', 'Subaru',
						 'Jaguar', 'Cadillac', 'Chrysler', 'Land Rover', 'Suzuki', 'Jeep', 'Maybach', 'Bugatti']

		self.carModel = ['Navigator L', 'Integra', 'GTI', 'Brat', 'Roadmaster', '9-3', 'Ram 50', 'Regal', 'Avalon',
						 'Firebird', 'Impreza', 'Nubira', 'M-Class', 'CTS', 'Justy', 'Celica', '3 Series', '3500', 'X5',
						 'Accord', 'Bonneville', 'Grand Marquis', 'Mazdaspeed 3', 'LS', 'F250', 'TL', 'B-Series',
						 'Sportage', 'Tribute', '9000', 'A8', 'MKZ', 'Challenger', 'Breeze', '2500', 'Millenia',
						 'Veloster', 'Sonata', 'CTS-V', 'Th!nk', 'Supra', 'Continental Super', 'Yaris', 'Malibu',
						 'Yukon', 'Tempest', 'E250', 'Starion', 'E-Series', 'Ram', '612 Scaglietti', 'Outlander',
						 'F-Series', 'Bronco II', 'Elise', 'Altima', 'Riviera', 'Jetta', 'Leganza', 'Sierra 1500',
						 'Crossfire', 'Escort', 'G-Series G30', 'Q', 'Ram 1500 Club', 'Daewoo Magnus', 'G-Series 2500',
						 'Ram Van 1500', 'Yukon XL 2500', 'Century', 'Titan', 'Escalade', 'Wrangler', 'Tiburon',
						 'XK Series', 'Land Cruiser', 'STS', 'E150', 'C-Class', '80', 'Escalade EXT', 'SM', 'Tacoma',
						 'Avenger', 'D350', 'Canyon', 'CX-7', 'G-Class', 'Chariot', 'CC', '6000', 'Explorer', 'Volare',
						 'Samurai']

		self.city = ['Lobos', 'Yamparáez', 'Talawi', 'Khagrachhari', 'La Unión', 'Gaotian', 'Šabac', 'Lijiaping',
					 'Thị Trấn Bắc Yên', 'Anyu', 'Okiot', 'Xiaoyang', 'Mūsa Khel Bāzār', 'Calimete', 'Yongchang',
					 'Palaió Fáliro', 'Tempe', 'Carquefou', 'Bejuco', 'Almelo', 'Misau', 'Nyzhni Sirohozy', 'Oak Bay',
					 'Huoshaodian', 'Saint Louis', 'Diaoling', 'Arroyo Naranjo', 'Kunri', 'Lishan', 'Onueke', 'Đồi Ngô',
					 'Novyy Starodub', 'Água Retorta', 'Karangjaladri', 'Chita', 'Kubangkondang', 'Sandao',
					 'As Saffānīyah', 'Sindangkerta', 'Santa Rosa', 'Kajiki', 'Vingåker', 'Kericho', 'Barg-e Matāl',
					 'Languan', 'Ḩurayḑah', 'Cijangkar', 'Trzcinica', 'Cabrobó', 'Matinao', 'Mao’ershan', 'Rongkou',
					 'Dinalongan', 'Alfena', 'Biting', 'Zuru', 'Fenhe', 'Krupanj', 'Khashuri', 'Alkmaar', 'Semiluki',
					 'Vis', 'Teresópolis', 'Ngreco', 'Duoxiang', 'Campo Maior', 'Arapongas', 'Dulolong', 'Xintang',
					 'Castelões', 'Sindon', 'María la Baja', 'Kwatarkwashi', 'San Miguel', 'Stetseva', 'Maputo',
					 'Wangping', 'Göteborg', 'Poponcol', 'Bella Unión', 'Karátoulas', 'Yangkou', 'Oliveira', 'Merke',
					 'Sitrah', 'Juripiranga', 'Pokrovskoye-Streshnëvo', 'Palatine', 'Margahayukencana', 'Podstepki',
					 'Banjar Medura', 'San Lorenzo de Esmeraldas', 'Vítkov', 'Inya', 'Moyynkum', 'Itapetininga',
					 'Ciro Redondo', 'Cartagena', 'Arendal', 'Baijiang']

		self.color = ['Crimson', 'Khaki', 'Red', 'Blue', 'Aquamarine', 'Violet', 'Maroon', 'Orange', 'Green', 'Pink',
					  'Purple', 'Yellow', 'Puce', 'Teal', 'Goldenrod', 'Mauv', 'Turquoise', 'Fuscia', 'Indigo']

		self.companyName = ['Vitz', 'Leenti', 'Buzzster', 'Skibox', 'Jaxnation', 'Trudeo', 'Thoughtblab', 'Reallinks',
							'Flipstorm', 'Rhyzio', 'Skinte', 'Feedbug', 'Bluezoom', 'Snaptags', 'Divape', 'Eamia',
							'Innotype', 'Izio', 'Aimbu', 'Skimia', 'Skinix', 'Ozu', 'Kanoodle', 'Buzzshare', 'Meevee',
							'Oodoo', 'Devbug', 'Twimm', 'Meezzy', 'Kayveo', 'Twitterwire', 'Brightdog', 'Kare',
							'Gabvine', 'Twitterbeat', 'Mita', 'Blogpad', 'Twitternation', 'BlogXS', 'Linkbridge',
							'Twimbo', 'Thoughtbridge', 'Twitterworks', 'Livetube', 'Divanoodle', 'Mybuzz', 'Browsetype',
							'Katz', 'Skiptube', 'Trilia', 'Skyvu', 'Linkbuzz', 'Fivespan', 'Npath', 'LiveZ', 'Devshare',
							'Skippad', 'Meembee', 'Kwideo', 'Jayo', 'Blogtags', 'Einti', 'Jazzy', 'Tagfeed', 'Riffwire',
							'Realcube', 'Cogidoo', 'Feedfish', 'Devpoint', 'Oba', 'Quamba', 'Oyoloo', 'Bubbletube',
							'Zoonoodle', 'Kwimbee', 'Jaxspan', 'Devify', 'Wordware', 'Voolith', 'Divavu', 'Jabbertype',
							'Devcast', 'Meedoo', 'DabZ', 'Livepath', 'Brainbox', 'Youspan', 'Feedfire', 'Twinte',
							'Shufflester', 'Trunyx', 'Voomm']

		self.constructionHeavyEquipment = ['Dump Truck', 'Compactor', 'Grader', 'Crawler', 'Excavator', 'Scraper',
										 'Dragline', 'Trencher', 'Skid-Steer', 'Bulldozer', 'Backhoe']

		self.constructionMaterial = ['Rubber', 'Plastic', 'Vinyl', 'Granite', 'Wood', 'Plexiglass', 'Aluminum', 'Stone',
								   'Steel', 'Brass', 'Glass']

		self.constructionRole = ['Subcontractor', 'Engineer', 'Estimator', 'Construction Worker', 'Supervisor',
							   'Surveyor', 'Construction Manager', 'Project Manager', 'Architect',
							   'Construction Expeditor', 'Construction Foreman', 'Electrician']

		self.constructionTrade = ['Laborer', 'Pipefitter', 'Safety Officer', 'Waterproofer', 'Linemen', 'Glazier',
								'Millwright', 'Welder', 'Sheet Metal Worker', 'Refridgeration', 'Ironworker',
								'Brickmason', 'Equipment Operator', 'Carpenter', 'Pipelayer', 'Terrazzo',
								'Cement Mason', 'Concrete Finisher', 'Plasterers', 'Tile Setter', 'Plumber', 'Painter',
								'Landscaper', 'Electrician', 'Boilermaker', 'Stucco Mason']

		self.country = ['Brazil', 'Russia', 'China', 'Libya', 'Tajikistan', 'Moldova', 'Switzerland', 'Indonesia',
						'Albania', 'Peru', 'Czech Republic', 'Germany', 'Greece', 'Cuba', 'Sudan', 'Mongolia', 'Poland',
						'Ukraine', 'Sweden', 'Italy', 'Japan', 'Philippines', 'United Kingdom', 'United States',
						'Thailand', 'Macedonia', 'Finland', 'Portugal', 'Pakistan', 'France', 'Syria', 'Argentina',
						'Dominican Republic', 'Nigeria', 'Mexico', 'Estonia', 'Croatia', 'Colombia', 'Tanzania']

		self.countryCode = ['GB', 'IQ', 'BG', 'CO', 'TH', 'RU', 'UA', 'CN', 'IE', 'HN', 'RS', 'SE', 'NG', 'KG', 'TN',
							'PE', 'CZ', 'MX', 'ID', 'PH', 'IR', 'HK', 'AL', 'LU', 'BA', 'AR', 'EG', 'US', 'FR', 'CA',
							'VE', 'BO', 'TL', 'GR', 'PT', 'PL', 'KM', 'NE', 'JP', 'NL', 'CL']

		self.creditCardType = ['jcb', 'mastercard', 'visa-electron', 'bankcard', 'diners-club-carte-blanche', 'maestro',
							   'interpayment', 'laser', 'visa', 'diners-club-enroute', 'americanexpress',
							   'diners-club-international', 'diners-club-us-ca', 'china-unionpay', 'switch']

		self.currency = ['Ruble', 'Euro', 'Dinar', 'Rupiah', 'Peso', 'Franc', 'Dong', 'Dollar', 'Hryvnia', 'Tenge',
						 'Yuan Renminbi', 'Zloty', 'Taka', 'Sol', 'Forint', 'Lempira', 'Bolivar', 'Lek', 'Koruna',
						 'Krona', 'Baht', 'Ringgit', 'Colon', 'Litas', 'Yen', 'Krone', 'Real', 'Birr', 'Shekel']

		self.currencyCode = ['LKR', 'CVE', 'CNY', 'EUR', 'BAM', 'TWD', 'PLN', 'MAD', 'PHP', 'MKD', 'IDR', 'XOF', 'RUB',
							 'AFN', 'MYR', 'VEF', 'MMK', 'BRL', 'UAH', 'LRD', 'JPY', 'ZAR', 'USD', 'AMD', 'COP', 'ILS',
							 'SEK', 'VND', 'AOA', 'CZK', 'BTN', 'HNL', 'BGN', 'YER', 'CAD']

		self.dayWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

		self.department = ['Engineering', 'Marketing', 'Services', 'Sales', 'Training', 'Product Management', 'Legal',
						   'Research and Development', 'Accounting', 'Human Resources', 'Business Development',
						   'Support']

		self.domain = ['tmall.com', 'newyorker.com', 'wikipedia.org', 'i2i.jp', 'apple.com', 'phpbb.com',
					   'earthlink.net', 'hubpages.com', 'sciencedirect.com', 'ted.com', 'ca.gov', 'list-manage.com',
					   'wikimedia.org', 'example.com', 'harvard.edu', 'hao123.com', 'sitemeter.com', 'yolasite.com',
					   'cdc.gov', 'wordpress.org', 'arizona.edu', 'buzzfeed.com', 'marriott.com', 'mayoclinic.com',
					   'china.com.cn', 'ning.com', 'g.co', 'soundcloud.com', 'disqus.com', 'delicious.com', 'dot.gov',
					   'indiegogo.com', 'foxnews.com', 'wunderground.com', 'liveinternet.ru', 'goo.gl',
					   'wikispaces.com', 'sina.com.cn', 'ucla.edu', 'toplist.cz', 'deliciousdays.com', 'bloomberg.com',
					   'yale.edu', 'diigo.com', 'timesonline.co.uk', 'trellian.com', 'msu.edu', 'github.com', 'ovh.net',
					   'craigslist.org', 'businessinsider.com', 'nih.gov', 'kickstarter.com', 'quantcast.com',
					   'nsw.gov.au', 'yahoo.com', 'ehow.com', 'shop-pro.jp', 'about.me', 'storify.com', 'last.fm',
					   'scientificamerican.com', 'twitter.com', 'jiathis.com', 'wsj.com', 'flickr.com', '1688.com',
					   'google.it', 'microsoft.com', 'barnesandnoble.com', 'sfgate.com', 'wisc.edu', 'miibeian.gov.cn',
					   'webmd.com', 'shareasale.com', 'jalbum.net', 'boston.com', 'pen.io', 'google.es', 'de.vu',
					   'livejournal.com', 'google.com.br', 'nymag.com', 'independent.co.uk', 'is.gd', 'zimbio.com',
					   'fotki.com', 'economist.com', 'guardian.co.uk', 'techcrunch.com', 'oaic.gov.au']

		self.dummyImageURL = ['http://dummyimage.com/216x100.png/dddddd/000000',
							  'http://dummyimage.com/111x100.png/cc0000/ffffff',
							  'http://dummyimage.com/147x100.png/5fa2dd/ffffff',
							  'http://dummyimage.com/209x100.png/cc0000/ffffff',
							  'http://dummyimage.com/178x100.png/dddddd/000000',
							  'http://dummyimage.com/136x100.png/dddddd/000000',
							  'http://dummyimage.com/123x100.png/ff4444/ffffff',
							  'http://dummyimage.com/198x100.png/ff4444/ffffff',
							  'http://dummyimage.com/183x100.png/cc0000/ffffff',
							  'http://dummyimage.com/170x100.png/cc0000/ffffff',
							  'http://dummyimage.com/227x100.png/dddddd/000000',
							  'http://dummyimage.com/157x100.png/dddddd/000000',
							  'http://dummyimage.com/187x100.png/ff4444/ffffff',
							  'http://dummyimage.com/189x100.png/dddddd/000000',
							  'http://dummyimage.com/145x100.png/dddddd/000000',
							  'http://dummyimage.com/177x100.png/cc0000/ffffff',
							  'http://dummyimage.com/166x100.png/5fa2dd/ffffff',
							  'http://dummyimage.com/239x100.png/cc0000/ffffff',
							  'http://dummyimage.com/214x100.png/dddddd/000000',
							  'http://dummyimage.com/185x100.png/dddddd/000000',
							  'http://dummyimage.com/249x100.png/cc0000/ffffff',
							  'http://dummyimage.com/127x100.png/ff4444/ffffff',
							  'http://dummyimage.com/223x100.png/ff4444/ffffff',
							  'http://dummyimage.com/129x100.png/cc0000/ffffff',
							  'http://dummyimage.com/150x100.png/dddddd/000000',
							  'http://dummyimage.com/197x100.png/5fa2dd/ffffff',
							  'http://dummyimage.com/211x100.png/5fa2dd/ffffff',
							  'http://dummyimage.com/214x100.png/cc0000/ffffff',
							  'http://dummyimage.com/179x100.png/ff4444/ffffff',
							  'http://dummyimage.com/113x100.png/dddddd/000000',
							  'http://dummyimage.com/152x100.png/dddddd/000000',
							  'http://dummyimage.com/111x100.png/ff4444/ffffff',
							  'http://dummyimage.com/122x100.png/ff4444/ffffff',
							  'http://dummyimage.com/248x100.png/cc0000/ffffff',
							  'http://dummyimage.com/239x100.png/5fa2dd/ffffff',
							  'http://dummyimage.com/200x100.png/cc0000/ffffff',
							  'http://dummyimage.com/123x100.png/dddddd/000000',
							  'http://dummyimage.com/151x100.png/5fa2dd/ffffff',
							  'http://dummyimage.com/233x100.png/cc0000/ffffff',
							  'http://dummyimage.com/224x100.png/cc0000/ffffff',
							  'http://dummyimage.com/203x100.png/dddddd/000000',
							  'http://dummyimage.com/117x100.png/5fa2dd/ffffff',
							  'http://dummyimage.com/112x100.png/ff4444/ffffff',
							  'http://dummyimage.com/228x100.png/cc0000/ffffff',
							  'http://dummyimage.com/103x100.png/ff4444/ffffff',
							  'http://dummyimage.com/147x100.png/ff4444/ffffff',
							  'http://dummyimage.com/210x100.png/dddddd/000000',
							  'http://dummyimage.com/179x100.png/5fa2dd/ffffff',
							  'http://dummyimage.com/105x100.png/dddddd/000000',
							  'http://dummyimage.com/196x100.png/dddddd/000000',
							  'http://dummyimage.com/190x100.png/dddddd/000000',
							  'http://dummyimage.com/117x100.png/dddddd/000000',
							  'http://dummyimage.com/222x100.png/5fa2dd/ffffff',
							  'http://dummyimage.com/242x100.png/dddddd/000000',
							  'http://dummyimage.com/112x100.png/cc0000/ffffff',
							  'http://dummyimage.com/211x100.png/cc0000/ffffff',
							  'http://dummyimage.com/100x100.png/dddddd/000000',
							  'http://dummyimage.com/104x100.png/cc0000/ffffff',
							  'http://dummyimage.com/225x100.png/dddddd/000000',
							  'http://dummyimage.com/125x100.png/dddddd/000000',
							  'http://dummyimage.com/154x100.png/dddddd/000000',
							  'http://dummyimage.com/158x100.png/5fa2dd/ffffff',
							  'http://dummyimage.com/208x100.png/dddddd/000000',
							  'http://dummyimage.com/234x100.png/5fa2dd/ffffff',
							  'http://dummyimage.com/126x100.png/dddddd/000000',
							  'http://dummyimage.com/180x100.png/dddddd/000000',
							  'http://dummyimage.com/119x100.png/cc0000/ffffff',
							  'http://dummyimage.com/220x100.png/dddddd/000000',
							  'http://dummyimage.com/147x100.png/dddddd/000000',
							  'http://dummyimage.com/189x100.png/ff4444/ffffff',
							  'http://dummyimage.com/205x100.png/ff4444/ffffff',
							  'http://dummyimage.com/186x100.png/5fa2dd/ffffff',
							  'http://dummyimage.com/232x100.png/dddddd/000000',
							  'http://dummyimage.com/104x100.png/ff4444/ffffff',
							  'http://dummyimage.com/121x100.png/5fa2dd/ffffff',
							  'http://dummyimage.com/126x100.png/5fa2dd/ffffff',
							  'http://dummyimage.com/245x100.png/dddddd/000000',
							  'http://dummyimage.com/154x100.png/cc0000/ffffff',
							  'http://dummyimage.com/130x100.png/5fa2dd/ffffff',
							  'http://dummyimage.com/205x100.png/cc0000/ffffff',
							  'http://dummyimage.com/229x100.png/5fa2dd/ffffff',
							  'http://dummyimage.com/127x100.png/cc0000/ffffff',
							  'http://dummyimage.com/120x100.png/5fa2dd/ffffff',
							  'http://dummyimage.com/108x100.png/cc0000/ffffff',
							  'http://dummyimage.com/199x100.png/dddddd/000000',
							  'http://dummyimage.com/231x100.png/dddddd/000000',
							  'http://dummyimage.com/140x100.png/dddddd/000000',
							  'http://dummyimage.com/124x100.png/5fa2dd/ffffff',
							  'http://dummyimage.com/160x100.png/5fa2dd/ffffff',
							  'http://dummyimage.com/163x100.png/ff4444/ffffff',
							  'http://dummyimage.com/201x100.png/dddddd/000000',
							  'http://dummyimage.com/243x100.png/cc0000/ffffff']

		self.fileExtension = ['avi', 'bat', 'bin', 'csv', 'dll', 'doc', 'docx', 'exe', 'gif', 'html', 'js', 'iso',
							  'jar', 'jpg', 'jpeg', 'mp3', 'mp4', 'm4a', 'mov', 'pdf', 'png', 'pps', 'ppt', 'rar',
							  'zip', 'tmp', 'txt']

		self.fileName = ['Tresom', 'Lotstring', 'Alpha', 'Bigtax', 'Kanlam', 'Temp', 'Opela', 'Gembucket', 'Zathin',
						 'Rank', 'Keylex', 'Viva', 'Konklab', 'Overhold', 'Tin', 'Ronstring', 'Redhold', 'Hatity',
						 'Bytecard', 'Mat Lam Tam', 'Andalax', 'Toughjoyfax', 'It', 'Veribet', 'Zamit', 'Ventosanzap',
						 'Prodder', 'Trippledex', 'Pannier', 'Sub-Ex', 'Wrapsafe', 'Otcom', 'Job', 'Home Ing', 'Span',
						 'Asoka', 'Subin', 'Voyatouch', 'Zaam-Dox', 'Daltfresh', 'Tampflex', 'Fix San', 'Duobam',
						 'Alphazap', 'Flexidy', 'Sonair', 'Flowdesk', 'Voltsillam', 'Tempsoft', 'Konklux', 'Cardify',
						 'Y-Solowarm', 'Lotlux', 'Y-find', 'Biodex', 'Regrant']

		self.firstName = ['Greg', 'Benoit', 'Doe', 'Deloria', 'Aigneis', 'Dulcia', 'Orsola', 'Randell', 'Rosaline',
						  'Betty', 'Janeta', 'Harmon', 'Audra', 'Averyl', 'Hugues', 'Guinevere', 'Theodor', 'Thelma',
						  'Forster', 'Dagny', 'Spike', 'Vivienne', 'Ben', 'Lawrence', 'Garvin', 'Leyla', 'Mufinella',
						  'Dana', 'Yehudi', 'Nessa', 'Fairleigh', 'Florella', 'Chaddy', 'Janet', 'Kailey', 'Valry',
						  'Filmore', 'Jamill', 'Michele', 'Becca', 'Reggis', 'Arvie', 'Fin', 'Barbie', 'Glory', 'Naomi',
						  'Janean', 'Chancey', 'Claudelle', 'Gusty', 'Marius', 'George', 'Ade', 'Giacobo', 'Siegfried',
						  'Norry', 'Jaine', 'Windy', 'Iris', 'Bliss', 'Ninette', 'Nappy', 'Olimpia', 'Maryanna',
						  'Francisco', 'Emmaline', 'Peyter', 'Felizio', 'Kennan', 'Domingo', 'Angelia', 'Basia',
						  'Melany', 'Aldridge', 'Noni', 'Harriett', 'Jonis', 'Flory', 'Marlane', 'Chloette', 'Towney',
						  'Deloris', 'Kimberlee', 'Leigha', 'Yank', 'Kris', 'Carena', 'Rosabelle', 'Vonni', 'Inger',
						  'Rocky', 'Sophie', 'Borg', 'Celeste', 'Egor', 'Lotte', 'Casie', 'Helsa', 'Fritz', 'Marion']

		self.gender = ["Male", "Female"]

		self.jobTitle = ['Community Outreach Specialist', 'Design Engineer', 'Administrative Assistant II',
						 'Systems Administrator II', 'Programmer Analyst III', 'Financial Advisor', 'Nurse',
						 'Executive Secretary', 'Safety Technician IV', 'Assistant Manager', 'Nurse Practicioner',
						 'Desktop Support Technician', 'Analog Circuit Design manager', 'Automation Specialist I',
						 'Analyst Programmer', 'Software Engineer III', 'Quality Control Specialist', 'Sales Associate',
						 'Developer III', 'Technical Writer', 'Civil Engineer', 'Senior Quality Engineer',
						 'Chemical Engineer', 'GIS Technical Architect', 'Software Engineer I', 'Marketing Manager',
						 'Structural Analysis Engineer', 'VP Sales', 'Nuclear Power Engineer', 'Senior Editor',
						 'Associate Professor', 'Dental Hygienist', 'Graphic Designer', 'Web Developer IV',
						 'Developer IV', 'Marketing Assistant', 'Legal Assistant', 'Web Designer I',
						 'Director of Sales', 'Account Representative I', 'Speech Pathologist', 'Chief Design Engineer',
						 'Actuary', 'Research Nurse', 'Budget/Accounting Analyst III', 'Tax Accountant',
						 'Information Systems Manager', 'Software Test Engineer III', 'Programmer II', 'Social Worker',
						 'Administrative Officer', 'Senior Financial Analyst', 'Computer Systems Analyst IV',
						 'Engineer III', 'Recruiter', 'Safety Technician II', 'Mechanical Systems Engineer',
						 'Media Manager II', 'Biostatistician IV', 'Account Coordinator', 'Junior Executive',
						 'Geological Engineer', 'Human Resources Manager', 'Human Resources Assistant II',
						 'Accounting Assistant III', 'Electrical Engineer', 'Editor', 'Help Desk Technician',
						 'Structural Engineer', 'Research Assistant IV', 'Food Chemist',
						 'Payment Adjustment Coordinator', 'Accounting Assistant I', 'Assistant Professor',
						 'VP Marketing', 'Web Designer IV', 'Human Resources Assistant IV']

		self.language = ['Danish', 'Yiddish', 'Dhivehi', 'Mongolian', 'Māori', 'Kashmiri', 'Kazakh', 'English',
						 'Irish Gaelic', 'Persian', 'Swahili', 'Malayalam', 'Papiamento', 'Portuguese', 'Croatian',
						 'Marathi', 'Romanian', 'Korean', 'Hindi', 'Lao', 'Maltese', 'German', 'Chinese', 'Macedonian',
						 'Japanese', 'Aymara', 'Tetum', 'Estonian', 'Tswana', 'Spanish', 'Nepali',
						 'New Zealand Sign Language', 'Khmer', 'Somali', 'Georgian', 'Dutch', 'Luxembourgish', 'Sotho',
						 'Tsonga', 'Bengali', 'Montenegrin', 'Punjabi', 'Northern Sotho', 'Tamil', 'Burmese', 'Gagauz',
						 'Bosnian', 'Armenian', 'Kurdish', 'Kyrgyz', 'Amharic', 'Hebrew', 'Tok Pisin', 'Arabic',
						 'Indonesian', 'Swedish', 'Icelandic', 'Catalan', 'Guaraní', 'Moldovan', 'Oriya', 'Polish',
						 'Haitian Creole', 'Dari', 'Greek', 'Afrikaans']

		self.lastName = ['Opy', 'Rollinson', 'Rojas', 'Whibley', 'Fowden', 'Birtwhistle', 'Becken', 'Haugh', 'Ragge',
						 'Fodden', 'Giannini', 'Margerrison', 'Fulton', 'Dahlbom', 'Begwell', 'Bosdet', 'MacDwyer',
						 'Fettes', 'McEttigen', 'Camelli', 'Melledy', 'Ambrois', 'Fagge', 'Westberg', 'Petrello',
						 'Hartman', 'Kydd', 'Sukbhans', 'McComish', 'Barens', 'Deakan', 'Zanuciolii', 'Custard',
						 'Yakunin', 'Roglieri', 'Smale', 'Jolland', 'Toolan', 'Dorr', 'Ferrolli', 'Cartan', 'Yeulet',
						 'Keble', 'Tome', 'Redwing', 'Jorin', 'Brierly', 'Klaiser', 'Welton', 'Yule', 'Wickwar',
						 'Bampkin', 'Rontsch', 'Pearn', 'Kleinstern', 'Killingsworth', 'Hurl', 'Muzzullo', 'Aiskovitch',
						 'Nesbit', 'Thatcher', 'Skedge', 'Patek', 'Brunsdon', 'Van de Castele', 'Harden', 'Yellep',
						 'Dolan', 'Eversfield', 'Berthot', 'Spadelli', 'Butter', 'Plail', 'Shakle', 'Brame', 'Arter',
						 'Skully', 'McGeachie', 'Cargen', 'Madle', 'Fendt', 'Coppen', 'Nashe', 'Krikorian', 'Varden',
						 'Hoyes', 'Tunnacliffe', 'Peverell', 'Dabell', 'Brambill', 'Blackater', 'Ishak', 'Jurca', 'Han',
						 'Daniello', 'Trusse', 'Hanbidge', 'Willows', 'Thornber']

		self.productGrocery = ['Samosa - Veg', 'Mushroom - Porcini Frozen', 'Shrimp - 31/40', 'Sour Cream',
							   'Wine - Chateau Timberlay', 'Compound - Rum', 'Cake - Dulce De Leche', 'Lotus Leaves',
							   'Beef - Top Sirloin', 'Chicken - Base', 'Appetizer - Asian Shrimp Roll',
							   'Muffin Carrot - Individual', 'Cup - 8oz Coffee Perforated', 'Zucchini - Green',
							   'Salmon - Atlantic, No Skin', 'Flax Seed', 'Seaweed Green Sheets',
							   'Island Oasis - Peach Daiquiri', 'Relish', 'Tequila Rose Cream Liquor',
							   'Tart Shells - Sweet, 2', 'External Supplier', 'Chickensplit Half',
							   'Juice - Cranberry 284ml', 'Bread Bowl Plain', 'Corn - Cream, Canned',
							   'Pop Shoppe Cream Soda', 'Beef - Rouladin, Sliced', 'Sausage - Meat', 'Chives - Fresh',
							   'Nut - Pecan, Halves', 'Pasta - Cheese / Spinach Bauletti', 'Berry Brulee',
							   'Potatoes - Mini White 3 Oz', 'Higashimaru Usukuchi Soy', 'Nori Sea Weed - Gold Label',
							   'Tuna - Sushi Grade', 'Appetizer - Crab And Brie', 'Beef - Ox Tongue, Pickled',
							   'Ham - Cooked Bayonne Tinned', 'Wine - Niagara Peninsula Vqa', 'Aspic - Clear',
							   'Parsley - Fresh', 'Chickhen - Chicken Phyllo', 'V8 Splash Strawberry Banana',
							   'Mushroom - Oyster, Fresh', 'Dill Weed - Dry', 'Cheese - Asiago', 'White Baguette',
							   'Longos - Lasagna Veg', 'Juice - Grapefruit, 341 Ml', 'Shiratamako - Rice Flour',
							   'Bread - Italian Roll With Herbs', 'Seabream Whole Farmed', 'Silicone Parch. 16.3x24.3',
							   'The Pop Shoppe - Lime Rickey', 'Sugar - Monocystal / Rock',
							   'Soup - Campbells Mac N Cheese', 'Longos - Assorted Sandwich',
							   'Nut - Almond, Blanched, Whole', 'Pasta - Fusili, Dry', 'Frangelico',
							   'Flower - Commercial Spider', 'Wine - Red, Antinori Santa', 'Dikon',
							   'Gatorade - Lemon Lime', 'Mustard - Pommery', 'Wine - Red, Lurton Merlot De',
							   'Bar Energy Chocchip', 'Pepsi, 355 Ml', 'Scallops - 10/20', 'Mushroom - Morels, Dry',
							   'Filo Dough', 'Alize Red Passion', 'Wine - Pinot Grigio Collavini', 'Blackberries',
							   'Bols Melon Liqueur', 'Pork - Tenderloin, Fresh', 'Turnip - White, Organic',
							   'Vinegar - Cider', 'Beef - Diced', 'Crab Brie In Phyllo',
							   'Scrubbie - Scotchbrite Hand Pad', 'Edible Flower - Mixed',
							   'Cheese - Brie, Triple Creme', 'Fib N9 - Prague Powder',
							   'Bread - Italian Corn Meal Poly', 'Wine - Delicato Merlot', 'Lamb - Shanks',
							   'Ecolab - Medallion', 'Lettuce Romaine Chopped', 'Cup - Translucent 7 Oz Clear',
							   'Juice - Pineapple, 341 Ml', 'Wine - Winzer Krems Gruner', 'Toamtoes 6x7 Select',
							   'Poppy Seed', 'Bread - Calabrese Baguette']

		self.streetName = ['Bonner', 'Kings', 'Springs', 'Monica', 'Delaware', 'Mccormick', 'Heath', 'Pankratz',
						   'Namekagon', 'Johnson', 'Westerfield', 'Cordelia', 'Lakeland', 'Becker', 'Coleman', 'Loomis',
						   'Brown', 'Thierer', 'Raven', '8th', 'Waxwing', '1st', 'Banding', 'Schmedeman', 'Iowa',
						   'Sage', 'Pierstorff', 'Talisman', 'Glacier Hill', 'John Wall', 'Northfield', 'Monument',
						   'Logan', 'Harper', 'Dapin', 'Dunning', 'Sunfield', 'Dovetail', 'Warner', 'Charing Cross',
						   'Debs', 'Westport', 'Amoth', 'Dayton', 'Arrowood', 'Waywood', 'Rieder', 'Vahlen', 'Bowman',
						   'Forest', 'Southridge', 'Dryden', 'Oak Valley', 'Forest Dale', 'Heffernan', 'Quincy',
						   'Straubel', 'Jay', 'Larry', 'Rutledge', 'Claremont', 'Rigney', 'Esker', 'Summer Ridge',
						   'Saint Paul', 'Texas', 'Kennedy', 'Karstens', 'Autumn Leaf', 'Crescent Oaks', 'Bayside',
						   'Towne', 'Moland', 'Gateway', 'Center', 'Redwing', 'Crest Line', 'Lakewood', 'Dorton',
						   'Carioca', 'Menomonie', 'Fairview', 'Del Mar', 'Sheridan', 'Laurel', 'Vermont', 'Melby',
						   'Thackeray', 'Brentwood', 'Schlimgen', 'Stuart', 'Mariners Cove']

		self.timeZone = ['Asia/Manila', 'Asia/Urumqi', 'America/Santarem', 'Europe/Warsaw', 'Asia/Chongqing',
						 'Europe/Paris', 'America/Sao_Paulo', 'Asia/Shanghai', 'Asia/Makassar', 'America/Panama',
						 'America/Argentina/Mendoza', 'Asia/Yerevan', 'Asia/Jakarta', 'America/Argentina/Salta',
						 'Europe/Stockholm', 'Asia/Dhaka', 'Asia/Irkutsk', 'America/Denver', 'Asia/Bangkok',
						 'Europe/Moscow', 'Asia/Harbin', 'Europe/Bratislava', 'America/Monterrey',
						 'Africa/Johannesburg', 'Asia/Tokyo', 'Africa/Monrovia', 'America/Fortaleza',
						 'America/Los_Angeles', 'Asia/Ho_Chi_Minh', 'Europe/Vienna', 'Europe/Lisbon',
						 'America/Costa_Rica', 'Asia/Nicosia', 'America/Argentina/Cordoba', 'Africa/Banjul',
						 'America/Guayaquil', 'Asia/Tehran', 'Europe/Dublin', 'America/Argentina/Catamarca',
						 'America/La_Paz', 'Africa/Casablanca', 'Asia/Kabul', 'Africa/Djibouti', 'Europe/Zagreb',
						 'Pacific/Auckland', 'Africa/Ndjamena', 'Europe/Tirane']

		self.programmingLanguage = ["Python", "JavaScript", "Java", "C#", "C", "C++", "PHP"]

		self.month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
					  "November", "December"]

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

	def insertDB(self, table_name):
		file = open("tmp_insert.txt", mode = "w")
		obj_db = getattr(db, table_name)
		for i in range(len(obj_db)):
			file.write(f"INSERT INTO `{table_name}`(`value`) VALUES ('{obj_db[i]}')")
			file.write(";\n")

	###API for random animalName ###
	def random_animalName(self):
		return random.choice(db.animalName)

	###API for random appBundleID ###
	def random_appBundleID(self):
		return random.choice(db.appBundleID)

	###API for random appName ###
	def random_appName(self):
		return random.choice(db.appName)

	###API for random avatar ###
	def random_avatar(self):
		return random.choice(db.avatar)

	###API for random boolean ###
	def random_boolean(self):
		return random.choice(db.boolean)

	###API for random carBrand ###
	def random_carBrand(self):
		return random.choice(db.carBrand)

	###API for random carModel ###
	def random_carModel(self):
		return random.choice(db.carModel)

	###API for random city ###
	def random_city(self):
		return random.choice(db.city)

	###API for random color ###
	def random_color(self):
		return random.choice(db.color)

	###API for random companyName ###
	def random_companyName(self):
		return random.choice(db.companyName)

	###API for random constructionHeavyEquipment ###
	def random_constructionHeavyEquipment(self):
		return random.choice(db.constructionHeavyEquipment)

	###API for random constructionMaterial ###
	def random_constructionMaterial(self):
		return random.choice(db.constructionMaterial)

	###API for random constructionRole ###
	def random_constructionRole(self):
		return random.choice(db.constructionRole)

	###API for random constructionTrade ###
	def random_constructionTrade(self):
		return random.choice(db.constructionTrade)

	###API for random country ###
	def random_country(self):
		return random.choice(db.country)

	###API for random countryCode ###
	def random_countryCode(self):
		return random.choice(db.countryCode)

	###API for random creditCardType ###
	def random_creditCardType(self):
		return random.choice(db.creditCardType)

	###API for random currency ###
	def random_currency(self):
		return random.choice(db.currency)

	###API for random currencyCode ###
	def random_currencyCode(self):
		return random.choice(db.currencyCode)

	###API for random department ###
	def random_department(self):
		return random.choice(db.department)

	###API for random domain ###
	def random_domain(self):
		return random.choice(db.domain)

	###API for random dummyImageURL ###
	def random_dummyImageURL(self):
		return random.choice(db.dummyImageURL)

	###API for random fileExtension ###
	def random_fileExtension(self):
		return random.choice(db.fileExtension)

	###API for random fileName ###
	def random_fileName(self):
		return random.choice(db.fileName)

	###API for random firstName ###
	def random_firstName(self):
		return random.choice(db.firstName)

	###API for random jobTitle ###
	def random_jobTitle(self):
		return random.choice(db.jobTitle)

	###API for random language ###
	def random_language(self):
		return random.choice(db.language)

	###API for random lastName ###
	def random_lastName(self):
		return random.choice(db.lastName)

	###API for random productGrocery ###
	def random_productGrocery(self):
		return random.choice(db.productGrocery)

	###API for random streetName ###
	def random_streetName(self):
		return random.choice(db.streetName)

	###API for random timeZone ###
	def random_timeZone(self):
		return random.choice(db.timeZone)

	###API for random gender ###
	def random_gender(self):
		return random.choice(db.gender)

	###API for random programmingLanguage ###
	def random_programmingLanguage(self):
		return random.choice(db.programmingLanguage)

	###API for random dayWeek ###
	def random_dayWeek(self):
		return random.choice(db.dayWeek)

	###API for random month ###
	def random_month(self):
		return random.choice(db.month)

	###API for random customdata ###
	def random_customdata(self, dataset=[]):
		"""
		:param dataset:
		:return:
		"""
		if  not dataset:
			return []
		else:
			return random.choice(dataset)

	###API for random fullName ###
	def random_fullName(self):
		return self.random_firstName() + " " + self.random_lastName()

	###API for random userName ###
	def random_userName(self):
		return self.random_firstName()[0].lower() + self.random_lastName() + str(random.randint(1, 10))

	###API for random Age ###
	def randomAge(self, min=10, max=90):
		"""
		:param min:
		:param max:
		"""
		return random.randint(min, max)

	###API for random year ###
	def random_year(self, min=1800, max=2200):
		return random.randint(min, max)

	###API for random email ###
	def random_email(self, name="", domain=""):
		"""
		:param name:
		:param domain:
		"""
		if not name:
			name = self.random_fullName()
		name = re.sub(" ", "", name)
		if not domain:
			domain = self.random_domain()

		return name + "@" + domain

	###API for random ipv4 ###
	def random_IPv4(self):
		offset = [1, 0, 0, 1]
		ip = ""
		for i in offset:
			ip += str(random.randint(i, 255))
			ip += "."
		return ip[0:-1]

	###API for random ipv6 ###
	def random_IPv6(self):
		template = string.digits + "ABCDEF"
		ipv6 = ""
		for i in range(8):
			ipv6 += ''.join(random.choice(template) for _ in range(4))
			ipv6 += "."
		return ipv6[0:-1]

	###API for random macAddress ###
	def random_macAddress(self, seperator=":"):
		"""
		:param seperator: ":"  "-"
		"""

		template = string.digits + "ABCDEF"
		mac = ""
		for i in range(6):
			mac += ''.join(random.choice(template) for _ in range(2))
			mac += seperator
		return mac[0:-1]

	###API for random version ###
	def random_version(self, min=2, max=4):
		"""
		:param min:
		:param max:
		"""
		lenth = random.randint(min, max)
		version = ""
		for i in range(lenth):
			version += str(random.randint(1, 20))
			version += "."
		return version[0:-1]

	###API for random bitcoinAddress ###
	def random_bitcoinAddress(self):
		template = string.digits + string.ascii_lowercase
		bit = ""
		for i in range(42):
			bit += random.choice(template)
		return bit

	###API for random creditCard ###
	def random_creditCard(self, credit_type=None):
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
				credit_type.append(self.random_creditCardType())
		template = []
		if 'visa' in credit_type:
			template.append("4### #### #### ####")
		if 'visa-electron' in credit_type:
			template.append(
				str(self.random_customdata(dataset=[4026, 4405, 4508, 4844, 4913, 4917])) + " #### #### ####")
		if 'americanexpress' in credit_type:
			template.append(str(self.random_customdata(dataset=[34, 37])) + "## ###### #####")
		if 'china-unionpay' in credit_type:
			template.append("62## ###### #####")
		if 'mastercard' in credit_type:
			template.append(str(random.randint(51, 55)) + "## #### #### ####")
		if 'maestro' in credit_type:
			template.append(str(self.random_customdata(
				dataset=[5018, 5020, 5038, 5612, 5893, 6304, 6759, 6761, 6762, 6763, 6390])) + " #### #### ####")
		if 'diners-club-carte-blanche' in credit_type:
			template.append(str(random.randint(300, 305)) + "# ###### ####")
		if 'diners-club-international' in credit_type:
			template.append(str(self.random_customdata(dataset=[300, 301, 302, 303, 304, 305, 309])) + "# ###### ####")
		if 'diners-club-us-ca' in credit_type:
			template.append(str(self.random_customdata(dataset=[54, 55])) + "## #### #### ####")
		if 'jcb' in credit_type:
			template.append(str(random.randint(3528, 3589)) + " #### #### ####")
		if 'diners-club-enroute' in credit_type:
			template.append(str(self.random_customdata(dataset=[2014, 2149])) + " ####### ####")
		if 'interpayment' in credit_type:
			template.append("636# #### ####")
		if 'bankcard' in credit_type:
			template.append("5610 #### ####")
		if 'laser' in credit_type:
			template.append(str(self.random_customdata(dataset=[6304, 6706, 6771, 6709])) + "#### #### ####")
		if 'switch' in credit_type:
			template.append(str(self.random_customdata(dataset=[4903, 4905, 4911, 4936, 6333, 6759])) + "#### #### ####")
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
	def random_date(self, min="01/01/1800", max="31/12/2200", format="dd/mm/yyyy"):
		"""

		:param min: minimum date of random range
		:param max: maximum date of random range
		:param format:
			"dd/mm/yyyy"
			"mm/dd/yyyy"
			"Mth/dd/yyyy"

			"dd-mm-yyyy"
			"mm-dd-yyyy"
			"Mth-dd-yyyy"

			"dd.mm.yyyy"
			"mm.dd.yyyy"
			"Mth.dd.yyyy"
		"""

		minDay, minMonth, minYear = re.split('/', min)
		maxDay, maxMonth, maxYear = re.split('/', max)
		tmpY = str(random.randint(int(minYear), int(maxYear)))

		tmpM = random.randint(1, 12)
		dd = random.randint(1, calendar.mdays[tmpM])
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
	def random_fileNameWithExtension(self):
		return self.random_fileName() + "." + self.random_fileExtension()

	###API for random hexColorCode ###
	def random_hexColorCode(self):
		template = string.digits + "ABCDEF"
		return "#" + ''.join(random.choice(template) for _ in range(6))

	###API for random SHA256 ###
	def random_SHA256(self):
		template = string.digits + "abcdef"
		return ''.join(random.choice(template) for _ in range(64))

	###API for random phoneNumber ###
	def random_phoneNumber(self, format="0## ### ####"):
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
	def random_streetNameAndAddress(self):
		return str(random.randint(1, 999)) + " " + self.random_streetName()

	###API for random password ###
	def random_password(self, min=8, max=12):
		"""
		:param min:
		:param max:

		"""
		template = string.digits + string.ascii_lowercase + string.ascii_uppercase + '!@#$%^&*'
		len = random.randint(min, max)
		return ''.join(random.choice(template) for _ in range(len))

	###API for random number ###
	def random_number(self, min=0, max=9999):
		return random.randint(min, max)

	###API for random time ###
	def random_time(self, format="12 Hour"):
		"""
		:param format:
			"12 Hour"
			"24 Hour"
		"""
		h = str(random.randint(1, int(format[:2])))
		m = str(random.randint(0, 59))
		if len(m) == 1:
			m = '0' + m
		if format == "12 Hour":
			period = self.random_customdata(["AM", "PM"])
		else:
			period = ""
		return h + ":" + m + " " + period

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
		# print("---------------------------------------------")
		# print(json.dumps(parsed, indent=4, sort_keys=False))
		# print('\n\n')
		return json.dumps(parsed, indent=4, sort_keys=False)


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

def render_data(url = ""):
	data = generate_json_format(url).print_json()

	# data = re.sub("\n", "<br>", data)
	# data = re.sub(" ", "&nbsp;", data)
	# print(data)

	return data

for i in range(10):
	render_data()
