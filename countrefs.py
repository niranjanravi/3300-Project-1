import re
import glob
import os
import json

"""
COUNTING METRIC: Find all references to any of rapper's nicknames.
Rapper's reference count is the top 10 highest counts per nickname.
"""


datasource = "stripped-lyrics/*"
nicknames = {
"2_chainz" : ["tity boi", "titty boi", "2chainz", "2 chainz", "duffle bag boi"],
"50_cent": ["50 Cent", "50", "Fifty","Fiddy","Interscope","Boo Boo"],
"chief_keef": ["chief keef", "keef", "almighty sosa",  "sosa", " king ", "almighty", "otto", "turbo", "batman"],
"desiigner" : ["desiigner"],
"drake" : ["Drake","Drizzy", "jumpman", "jump man", "Champagne Papi","October's Very Own", "6god", "six god", 'VIETBRAH', 'Aubrey Graham', 'Drizzy', 'Heartbreak Drake', 'Young Angel', 'Wheelchair Jimmy', 'Francisco Mandarin', 'Young Frank', 'Young Papi', 'Champagne Papi', 'Drizzy Rodgers', 'Drizzy Drake Rodgers', 'Drizzy Hendrix', 'Homicide Drizzy', 'Voodoo Child', 'Aubz', 'Shopping Bag Drizzy', 'Mr OVOXO', 'Griffin', 'Young Frankie Geechi Liberachi', 'Young Sweet Jones', "Mr. Damn He Aint' Coppin That Is He?", 'The Same Yellow Boy That Used To Play Up On Degrassi', 'The Chris Paul Of This Fall', 'The Lebron James Of This Rap Game', 'Prada G (Not a Gucci Groupie)', 'The Reason Why You Always Getting Faded', 'The Young Money White Knight', 'Young Money Superstar', 'Cash Money Running Back', 'Champagne Charlie', 'Little Nicky', 'Captain Hook', 'Hookah Papi', 'Young King', 'Mr CTV', 'Bottega Don.', 'Drakkardnoir', 'One Take Drake', "October's Very Own", 'Mr. October', "October's Truly", 'OVO Don Dada', 'The Only 23 Year Old Wine Connoisseur', 'The King Of 1st Quarter', 'Frostbite Drizzy', 'Light Skin Keith Sweat', "'91 Dan Marino", 'The Kid With The Motor Mouth ', 'The Boy', '6God', "The Youngest Nigga Reppin'", '6Man', 'Young Papito'],
"fetty_wap": ["fetty wap", "fetty"], 
"future" : ["Future","Hendrix", "Xanman", "astronaut kid"], 
"gucci_mane" : ["Gucci", "Guwop","Mr. Zone 6", "East Atlanta Santa"], 
"kanye": ["Kanye","Yeezy", "Ye ", "Louis Vuitton Don","Konman", 'Pablo','Yeezus','West', 'Don', 'Martin Louis the King', 'KanYeezy', 'The LeBron of Rhyme', 'K-Rock', 'Omari', 'The Black Zac Efron', 'Evel Kanyevel', 'Swag King Cole'], 
"lil_wayne": ["Birdman","Tuneche","Weezyana","Weezy","Carter","Tunechi", "Tune",  'Ammo', 'Ammo Mammal', 'Apple Eagle Weezle', 'Automatic Weezy', 'The BB King', 'The Beast', 'Big Daddy Kane', 'Big Baller', 'Big Body', 'Big Dog', 'Big Money Weezy', 'Big Pockets', 'Big Stick', 'Big Stunna', 'Big Tymer', 'Birdman Jr', 'Bossman Weezy', 'Brick Cannon', 'Bring The Money Home', 'Candy Carter', 'The Carter', 'Cartey', 'Cash Money Hot Boy', 'Cash Money Makaveli', 'Daddy', 'Deepwater Carter', 'Deion Sanders', 'Dr. Carter', 'Dr. Carter M.D', 'Eagle Carter', 'Eddie', 'Eduardo', 'Fireman', 'First Place', "Fo' Sheezy", 'Gangsta Gangsta', 'Groundhog', 'Heatman', 'Hi-C', 'Hoodie Man', "I Can't Feel My Face", 'I Got Enough Money On Me', 'Iceberg Shorty', 'J.R', 'Junior', 'Knievel', 'Killa', 'Lil Cardiac', 'Lil Carter', 'Lil Birdman Junior', 'Lil Full Clip Me', 'Lil Rabbit', 'Lil Tunechi', 'Lil Weezle', 'Lil Weezy', 'Lil Weezy-ana', 'Lil Whodi', 'Little Big Kahuna', 'Little Russell Crowe', 'Little Weezy', 'Little Wizzle', 'Lord', 'Money Making Weezy', 'Mr. Carter', 'Mr. Coach Carter', 'Mr. Crazy Flow', "Mr. Director's Chair", 'Mr. Doctor Carter', 'Mr. Go-Harder', "Mr. I-Can't-Make-An-Appointment", 'Mr. Lawn Mower', 'Mr. Make-It-Rain-On-Them-Hoes', 'Mr. Ointment', 'Mr. President', 'Mr. Rainman', 'Mr. Sandman', "Mr. Shoot-'Em-Down", 'Mr. Swag-more', 'Mr. Water Coolers', 'Mr. Weezy Baby', 'Mr. Withdraws', 'The New Orleans Nightmare', 'No Lungs', 'The Number One Hot Boy On Fire', 'Ocean Drive Slim', 'Off The Heezy', 'Pac-Man', 'Payday', 'Pistol Pete', 'President Carter', 'Porta-Potty Tunechi', 'The Pussy Monster', 'Quick Draw McGraw', 'The Rapper Eater', 'Raw Tune', 'Red Alert', 'The Rhyming Oasis', 'Settling', 'Seventeen Creeper', 'A Shark', 'Stunna Jr', 'Survivor', 'Teardrop Tune', 'That Lil Nigga With The Rope Full Of Diamonds', 'Tommy Gun Tunechi', 'Trigga Man', 'Triple A', 'Tune', 'Tunechi', 'Tunechi Bitch', 'Tunechi Li', 'Tunechi The Boss', 'Usain Wayne', 'Uncle Sam', 'The Ventriloquist', 'The Warden', 'Weez', 'Weezy Baby', 'Weezy Da Crack', 'Weezy Da King', 'Weezy F', "Weezy Fuckin' Baby", 'Weezy F Crazy', 'Weezy The Dime', 'Weezy The Don', 'Weezy Wayne', 'Weezy Wee', 'Weezy West', 'Wife Beater', 'Wizzle', 'Wizzle F Baby', 'Wizzle Fizzle', 'Wizzy Fizzy', 'Young Ass Weezy', 'Young Baby', 'Young Boy', 'Young Carter', 'Young Dictionary', 'Young Fly Wizzy', 'Young God', 'Young Heart Attack', 'Young Money Democrat', 'Young Nino', 'Young Ozzy Osbourne', "Young Pimpin'", 'Young Popeye', 'Young Roy Jones, Jr', 'Young Stunna', 'Young Tuna Fish', 'Young Tune', 'Young Tunechi', 'Young Wayne', 'Young Wayne Carruth', 'Young Weezle', 'Young Weezy', 'Young Weezy Baby', 'Young Wizzle']
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

	topCounts = []
	for n in nicknames[name]:
		regex = r"" + n.lower()
		#Effectively remove the word so doesn get double counted by
		#a later nickname like in the example of 'kanye' and 'ye'
		lyrics, count = re.subn(regex, "", lyrics)
		topCounts += [count]
		print("'{}' has count of {}".format(n, count))
	f.close()

	topCounts = sorted(topCounts, reverse = True)

	if len(topCounts) > 10:
		topCounts = topCounts[:10]

	for c in topCounts:
		referenceData[name]["count"] += c

if os.path.exists("rappers.json"):
		os.remove("rappers.json")

with open ("rappers.json", "w") as file:
	json.dump(referenceData, file)













