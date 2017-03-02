import re
import glob
import os
import json


datasource = "stripped-lyrics/*"
nicknames = {
"2_chainz" : ["tity boi", "titty boi", "2chainz", "2 chainz"],
"50_cent": ["50 Cent", "50", "Fifty","Fiddy","Interscope","Boo Boo"],
"chief_keef": [],
"desiigner" : [],
"drake" : ["Drake","Drizzy", "jumpman", "jump man", "Champagne Papi","October's Very Own", "6god", "six god",       'VIETBRAH', 'Aubrey Graham', 'Drizzy', 'Heartbreak Drake', 'Young Angel', 'Wheelchair Jimmy', 'Francisco Mandarin', 'Young Frank', 'Young Papi', 'Champagne Papi', 'Drizzy Rodgers', 'Drizzy Drake Rodgers', 'Drizzy Hendrix', 'Homicide Drizzy', 'Voodoo Child', 'Aubz', 'Shopping Bag Drizzy', 'Mr OVOXO', 'Griffin', 'Young Frankie Geechi Liberachi', 'Young Sweet Jones', "Mr. Damn He Aint' Coppin That Is He?", 'The Same Yellow Boy That Used To Play Up On Degrassi', 'The Chris Paul Of This Fall', 'The Lebron James Of This Rap Game', 'Prada G (Not a Gucci Groupie)', 'The Reason Why You Always Getting Faded', 'The Young Money White Knight', 'Young Money Superstar', 'Cash Money Running Back', 'Champagne Charlie', 'Little Nicky', 'Captain Hook', 'Hookah Papi', 'Young King', 'Mr CTV', 'Bottega Don.', 'Drakkardnoir', 'One Take Drake', "October's Very Own", 'Mr. October', "October's Truly", 'OVO Don Dada', 'The Only 23 Year Old Wine Connoisseur', 'The King Of 1st Quarter', 'Frostbite Drizzy', 'Light Skin Keith Sweat', "'91 Dan Marino", 'The Kid With The Motor Mouth ', 'The Boy', '6God', "The Youngest Nigga Reppin'", '6Man', 'Young Papito'],
"fetty_wap": [], 
"future" : ["Future","Hendrix"], 
"gucci_mane" : ["Gucci", "Guwop","Mr. Zone 6", "East Atlanta Santa"], 
"kanye": ["Kanye","Yeezy", "Ye ", "Louis Vuitton Don","Konman", 'Pablo','Yeezus','West', 'Don', 'Martin Louis the King', 'KanYeezy', 'The LeBron of Rhyme', 'K-Rock', 'Omari', 'The Black Zac Efron', 'Evel Kanyevel', 'Swag King Cole'   ], 
"lil_wayne": ["Birdman","Tuneche","Weezyana","Weezy","Carter","Tunechi"]
}
referenceData = {
"2_chainz" : {"count": 0, "totalwords" : 0},
"50_cent": {"count": 0, "totalwords" : 0},
"chief_keef": {"count": 0, "totalwords" : 0},
"desiigner" : {"count": 0, "totalwords" : 0},
"drake" : {"count": 0, "totalwords" : 0},
"fetty_wap": {"count": 0, "totalwords" : 0}, 
"future" : {"count": 0, "totalwords" : 0}, 
"gucci_mane" : {"count": 0, "totalwords" : 0}, 
"kanye": {"count": 0, "totalwords" : 0}, 
"lil_wayne": {"count": 0, "totalwords" : 0}
}

nameRE = r"(/stripped-)(.*)(.txt)"

for filename in glob.iglob(datasource):
	name = re.search(nameRE, filename).group(2)
	f = open(filename)

	lyrics = """ """

	for line in f:
		lyrics += line

	lyrics = lyrics.lower()
	lyrics = re.sub(r"\n", " ", lyrics)
	counterlyrics = lyrics
	referenceData[name]["totalwords"] = len(counterlyrics.split(" "))

	print("==================================")
	print(name)
	print("==================================")

	for n in nicknames[name]:
		regex = r"" + n.lower()
		#Effectively remove the word so doesn get double counted by
		#a later nickname like in the example of 'kanye' and 'ye'
		lyrics, count = re.subn(regex, "", lyrics)
		referenceData[name]["count"] += count
		print("'{}' has count of {}".format(n, count))
	f.close()

if os.path.exists("rappers.json"):
		os.remove("rappers.json")

with open ("rappers.json", "w") as file:
	json.dump(referenceData, file)













