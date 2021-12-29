def popis_država():
    import locale
    locale.setlocale(locale.LC_ALL, "hrv")
    
    popis = ["Afganistan", "Albanija", "Alžir", "Andora", "Angola", "Antigva i Barbuda", "Argentina", "Armenija","Australija", 
    "Austrija", "Azerbajdžan", "Bahami", "Bahrein", "Bangladeš", "Barbados", "Belarus", "Belgija", "Belize", "Benin", 
    "Bjelorusija", "Bocvana", "Bolivija", "Bosna i Hercegovina", "Brazil", "Brunej", "Bugarska", "Burkina Faso", 
    "Burundi", "Butan", "Cipar", "Crna Gora", "Čad", "Češka", "Čile", "Danska", "Kongo", "Dominikanska Republika", 
    "Džibuti", "Egipat", "Ekvador", "Ekvatorijalna Gvineja", "Eritreja", "Estonija", "Etiopija", "Fidži", "Filipini", 
    "Finska", "Francuska", "Gabon", "Gambija", "Gana", "Grčka", "Grenada", "Gruzija", "Gvajana", "Gvatemala", "Gvineja", 
    "Haiti", "Honduras", "Hrvatska", "Indija", "Indonezija", "Irak", "Iran", "Irska", "Island", "Istočni Timor", "Italija", 
    "Izrael", "Jamajka", "Japan", "Jemen", "Jordan", "Južna Koreja", "Južni Sudan", "Južnoafrička Republika", "Kambodža", 
    "Kamerun", "Kanada", "Katar", "Kazahstan", "Kenija", "Kina", "Kirgistan", "Kiribati", "Kolumbija", "Komori", "Kongo", 
    "Koreja", "Kosovo", "Kostarika", "Kuba", "Kuvajt", "Laos", "Latvija", "Lesoto", "Libanon", "Liberija", "Libija", 
    "Lihtenštajn", "Litva", "Luksemburg", "Madagaskar", "Mađarska", "Malavi", "Maldivi", "Malezija", "Mali", "Malta", 
    "Maroko", "Maršalovi Otoci", "Mauricijus", "Mauretanija", "Meksiko", "Mijanmar", "Mikronezija", "Moldavija", "Monako", 
    "Mongolija", "Mozambik", "Namibija", "Nauru", "Nepal", "Niger", "Nigerija", "Nikaragva", "Nizozemska", "Norveška", 
    "Novi Zeland", "Njemačka", "Oman", "Obala Bjelokosti", "Pakistan", "Palau", "Panama", "Papua Nova Gvineja", "Paragvaj", 
    "Peru", "Poljska", "Portugal", "Ruanda", "Rumunjska", "Rusija", "Ruska Federacija", "Salomonovi Otoci", "Salvador", 
    "Samoa", "San Marino", "Saudijska Arabija", "Sejšeli", "Senegal", "Sierra Leone", "Singapur", "Sirija", 
    "Sjedinjene Američke Države", "Sjeverna Koreja", "Sjeverna Makedonija", "Slovačka", "Slovenija", "Somalija", "Srbija", 
    "Srednjoafrička Republika", "Sudan", "Surinam", "Svazi", "Sveta Lucija", "Sveti Kristofor i Nevis", "Sveti Toma i Princip", 
    "Sveti Vincent i Grenadini", "Španjolska", "Šri Lanka", "Švedska", "Švicarska", "Tadžikistan", "Tajland", "Tanzanija", 
    "Ujedinjena Republika Tanzanija", "Togo", "Tonga", "Trinidad i Tobago", "Tunis", "Turkmenistan", "Turska", "Tuvalu", 
    "Uganda", "Ujedinjeni Arapski Emirati", "Ukrajina", "Urugvaj", "Uzbekistan", "Vanuatu", "Vatikan", "Velika Britanija", 
    "Venezuela", "Vijetnam", "Zambija", "Zelenortska Republika","Zimbabve"]
    for i in range (len(popis)):
        popis[i] = popis[i].upper()
    print(popis)

popis_država()




