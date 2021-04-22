
def state_capital():
    stato_capitale = {'Afghanistan':'Kabul','Albania':'Tirana','Algeria':'Algeri','Andorra':'Andorra La Vella',
                      'Angola':'Luanda','Antigua e Barbuda':'Saint Johns','Arabia Saudita':'Riyad',
                      'Argentina':'Buenos Aires','Armenia':'Yerevan','Australia':'Camberra','Austria':'Vienna',
                      'Azerbeigian':'Baku','Bahamas':'Nassau','Bahrain':'Manama','Bangladesh':'Dhaka',
                      'Barbados':'Bridgetown','Belgio':'Bruxelles','Belize':'Belmopan','Benin':'Porto-Novo',
                      'Bhutan':'Thimphu','Bielorussia':'Minsk','Birmania':'Naypyidaw','Bolivia':'Sucre-La Paz',
                      'Bosnia-Erzegovina':'Sarajevo','Botswana':'Gaborone','Brasile':'Brasilia',
                      'Brunei':'Bandar Seri Bagawan','Bulgaria':'Sofia','Burkina Faso':'Ouagadougou',
                      'Burundi':'Gitega','Cambogia':'Phnom Penh','Camerun':'Yaoundé','Canada':'Ottawa','Capo Verde':'Praia',
                      'Ciad':'NDjamena','Cile':'Santiago Del Cile','Cina':'Pechino','Cipro':'Nicosia','Colombia':'Bogotà','Comore':'Moroni',
                      'Rep. Del Congo':'Brazzaville','Rep. Dem. Del Congo':'Kinshasa','Corea Del Nord':'Pyongyang','Corea Del Sud':'Seul',
                      "Costa d'Avorio":'Yamoussoukro','Costa Rica':'San José','Croazia':'Zagabria','Cuba':"L'Havana",'Danimarca':'Copenhagen',
                      'Dominica':'Roseau','Ecuador':'Quito','Egitto':'Il Cairo','El Salvador':'San Salvador','Emirati Arabi Uniti':'Abu Dhabi',
                      'Eritrea':'Asmara','Estonia':'Tallinn','Etiopia':'Addis Abeba','Fiji':'Suva','Filippine':'Manila','Finlandia':'Helsinki',
                      'Francia':'Parigi','Gabon':'Libreville','Gambia':'Banjul','Georgia':'Tbilisi','Germania':'Berlino','Ghana':'Accra',
                      'Giamaica':'Kingston','Giappone':'Tokyo','Gibuti':'Gibuti','Giordania':'Amman','Grecia':'Atene','Grenada':'St. George',
                      'Guatemala':'Città Del Guatemala','Guinea':'Conakry','Guinea-Bissau':'Bissau','Guinea Equatoriale':'Malabo','Guyana':'George Town',
                      'Haiti':'Port-Au-Prince','Honduras':'Tegucigalpa','India':'Nuova Dehli','Indonesia':'Giacarta','Iran':'Teheran','Iraq':'Baghdad',
                      'Irlanda':'Dublino','Islanda':'Reykjavik','Isole Marshall':'Majuro','Isole Salomone':'Honiara','Israele':'Gerusalemme','Italia':'Roma',
                      'Kazakistan':'Nur-Sultan','Kenya':'Nairobi','Kirghizistan':'Biskek','Kiribati':'Tarawa Sud','Kuwait':'Medinat-Al-Kuwait','Laos':'Vientiane',
                      'Lesotho':'Maseru','Lettonia':'Riga','Libano':'Beirut','Liberia':'Monrovia','Libia':'Tripoli','Liechtenstein':'Vaduz','Lituania':'Vilnius',
                      'Lussemburgo':'Lussemburgo','Macedonia':'Skopje','Madagascar':'Antananarivo','Malawi':'Lilongwe','Malaysia':'Kuala Lampur','Maldive':'Malé',
                      'Mali':'Bamako','Malta':'La Valletta','Marocco':'Rabat','Mauritania':'Nouakchott','Mauritius':'Port-Louis','Messico':'Città Del Messico',
                      'Micronesia':'Palikir','Moldavia':'Chisinau','Monaco':'Monaco','Mongolia':'Ulan Bator','Montenegro':'Podgorica','Mozambico':'Maputo',
                      'Namibia':'Windhoek','Nauru':'Yeren','Nepal':'Kathmandu','Nicaragua':'Managua','Niger':'Niamey','Nigeria':'Abuja','Norvegia':'Oslo',
                      'Nuova Zelanda':'Wellington','Oman':'Mascate','Paesi Bassi':'Amsterdam','Pakistan':'Islamabad','Palau':'Ngerulmud','Palestina':'Gerusalemme Est',
                      'Panama':'Città Di Panama','Papua Nuova Guinea':'Port Moresby','Paraguay':'Assunciòn','Perù':'Lima','Polonia':'Varsavia','Portogallo':'Lisbona',
                      'Qatar':'Doha','Regno Unito':'Londra','Repubblica Ceca':'Praga','Repubblica Centroafricana':'Bangui','Repubblica Dominicana':'Santo Domingo',
                      'Repubblica Sudafricana':'Pretoria-Bloemfontein-Città Del Capo','Romania':'Bucarest','Ruanda':'Kigali','Russia':'Mosca','Saint Kitts E Nevis':'Basseterre',
                      'Saint Lucia':'Castries','Saint Vincent E Grenadine':'Kingstown','Samoa':'Apia','San Marino':'Città Di San Marino','Sao Tomé E Principe':'Sao Tomé',
                      'Senegal':'Dakar','Serbia':'Belgrado','Seychelles':'Victoria','Sierra Leone':'Free Town','Singapore':'Singapore','Siria':'Damasco',
                      'Slovacchia':'Bratislava','Slovenia':'Lubiana','Somalia':'Mogadiscio','Spagna':'Madrid','Sri Lanka':'Sri Jayawandenapura Kotte','Stati Uniti':'Washington',
                      'Sudan':'Khartum','Sudan Del Sud':'Giuba','Suriname':'Paramaribo','Svezia':'Stoccolma','Svizzera':'Berna','Swaziland':'Mbabane-Lobamba','Tagikistan':'Dusambe',
                      'Taiwan':'Taipei','Tanzania':'Dodoma-Dar Es Salaam','Thailandia':'Bangkok','Timor Est':'Dili','Togo':'Lomé','Tonga':'Nuku Alofa','Trinidad E Tobago':'Port Of Spain',
                      'Tunisia':'Tunisi','Turchia':'Ankara','Turkmenistan':'Asgabat','Tuvalu':'Funafuti','Ucraina':'Kiev','Uganda':'Kampala','Ungheria':'Budapest',
                      'Uruguay':'Montevideo','Uzbekistan':'Tashkent','Vanuatu':'Port Vila','Vaticano':'Città Del Vaticano','Venezuela':'Caracas','Vietnam':'Hanoi','Yemen':'Sanaa-Aden',
                      'Zambia':'Lusaka','Zimbabwe':'Harare','Abcasia':'Sukhumi','Cipro del Nord':'Nicosia Nord','Kosovo':'Pristina',
                      'Artsakh':"Step' anakert",'Ossezia del Sud':'Tskhinvali','Sahara Occidentale':'El Aaiun','Somaliland':'Hergheisa',
                      'Transnistria':'Tiraspol','Repubblica Popolare di Doneck':"Donec'k",'Repubblica Popolare di Lugansk':"Luhans'k",
                      "Isole Cook":"Avarua","Niue":"Alofi"}
    return stato_capitale

def states():
    stati = ['Afghanistan','Albania','Algeria','Andorra','Angola','Antigua e Barbuda','Arabia Saudita',
         'Argentina','Armenia','Australia','Austria','Azerbeigian','Bahamas','Bahrain','Bangladesh',
         'Barbados','Belgio','Belize','Benin','Bhutan','Bielorussia','Birmania','Bolivia','Bosnia-Erzegovina',
         'Botswana','Brasile','Brunei','Bulgaria','Burkina Faso','Burundi','Cambogia','Camerun','Canada','Capo Verde',
         'Ciad','Cile','Cina','Cipro','Colombia','Comore','Rep. Del Congo','Rep. Dem. Del Congo','Corea Del Nord','Corea Del Sud',
         "Costa d'Avorio",'Costa Rica','Croazia','Cuba','Danimarca','Dominica','Ecuador','Egitto','El Salvador','Emirati Arabi Uniti',
         'Eritrea','Estonia','Etiopia','Fiji','Filippine','Finlandia','Francia','Gabon','Gambia','Georgia','Germania','Ghana','Giamaica',
         'Giappone','Gibuti','Giordania','Grecia','Grenada','Guatemala','Guinea','Guinea-Bissau','Guinea Equatoriale','Guyana','Haiti','Honduras',
         'India','Indonesia','Iran','Iraq','Irlanda','Islanda','Isole Marshall','Isole Salomone','Israele','Italia','Kazakistan','Kenya',
         'Kirghizistan','Kiribati','Kuwait','Laos','Lesotho','Lettonia','Libano','Liberia','Libia','Liechtenstein','Lituania','Lussemburgo',
         'Macedonia','Madagascar','Malawi','Malaysia','Maldive','Mali','Malta','Marocco','Mauritania','Mauritius','Messico','Micronesia','Moldavia',
         'Monaco','Mongolia','Montenegro','Mozambico','Namibia','Nauru','Nepal','Nicaragua','Niger','Nigeria','Norvegia','Nuova Zelanda','Oman',
         'Paesi Bassi','Pakistan','Palau','Palestina','Panama','Papua Nuova Guinea','Paraguay','Perù','Polonia','Portogallo','Qatar','Regno Unito',
         'Repubblica Ceca','Repubblica Centroafricana','Repubblica Dominicana','Repubblica Sudafricana','Romania','Ruanda','Russia','Saint Kitts E Nevis',
         'Saint Lucia','Saint Vincent E Grenadine','Samoa','San Marino','Sao Tomé E Principe','Senegal','Serbia','Seychelles','Sierra Leone','Singapore',
         'Siria','Slovacchia','Slovenia','Somalia','Spagna','Sri Lanka','Stati Uniti','Sudan','Sudan Del Sud','Suriname','Svezia','Svizzera','Swaziland',
         'Tagikistan','Taiwan','Tanzania','Thailandia','Timor Est','Togo','Tonga','Trinidad E Tobago','Tunisia','Turchia','Turkmenistan',
         'Tuvalu','Ucraina','Uganda','Ungheria','Uruguay','Uzbekistan','Vanuatu','Vaticano','Venezuela','Vietnam','Yemen','Zambia','Zimbabwe',
         'Abcasia','Cipro del Nord','Kosovo','Artsakh','Ossezia del Sud','Sahara Occidentale','Somaliland','Transnistria','Repubblica Popolare di Doneck',
         'Repubblica Popolare di Lugansk','Isole Cook','Niue']
    return stati

