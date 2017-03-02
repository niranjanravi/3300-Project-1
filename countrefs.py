import re
import glob
import os
import json


datasource = "stripped-lyrics/*"
nicknames = {
"2_chainz" : [],
"50_cent": ["50 Cent", "Fifty","Fiddy","Interscope","Boo Boo"],
"chief_keef": [],
"desiigner" : [],
"drake" : ["Drake","Drizzy","Champagne Papi","October's Very Own", "6god", "six god"],
"fetty_wap": [], 
"future" : ["Future","Hendrix"], 
"gucci_mane" : ["Gucci", "Guwop","Mr. Zone 6", "East Atlanta Santa"], 
"kanye": ["Kanye","Yeezy", "Ye", "Louis Vuitton Don","Konman"], 
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

	#Need to get length, and then do subn

	for n in nicknames[name]:
		regex = r"" + n.lower()
		#Effectively remove the word so doesn get double counted by
		#a later nickname like in the example of 'kanye' and 'ye'
		referenceData[name]["count"] += re.subn(regex, "", lyrics)[1]
	f.close()

if os.path.exists("rappers.json"):
		os.remove("rappers.json")

with open ("rappers.json", "w") as file:
	json.dump(referenceData, file)













