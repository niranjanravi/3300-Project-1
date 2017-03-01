import re
import glob
import os
datasource = "data/*"

bracketRE = r"^\[.+\]" #Handles things like [Kanye], [Outro: x3], etc
colonRE = r"^.+:" #Handles expressions like 'Gucci Mane:' at the begging of new lines
parenthesesRE = r"^\(.+\)" #Handles expressions at beginnng of new line like '(Gucci)'
#Does catch some lyrics... but at least putting it at begging of new line minimizes some of that





newpath = 'stripped-lyrics/'

if not os.path.exists(newpath):
	os.mkdir(newpath)

for filename in glob.iglob(datasource):
	name = filename[len(datasource)-1:]
	lyrics = """ """
	with open(filename, 'r') as f:
		for line in f:
			lyrics += line

	f.close()
	lyrics = re.sub(bracketRE, "", lyrics, flags = re.MULTILINE)
	lyrics = re.sub(colonRE, "", lyrics, flags = re.MULTILINE)
	lyrics = re.sub(parenthesesRE, "", lyrics, flags = re.MULTILINE)

	newfilepath = newpath + "stripped-" + name

	if os.path.exists(newfilepath):
		os.remove(newfilepath)

	with open(newpath + "stripped-" + name, 'w') as new:
		new.write(lyrics)
	new.close()
	print("Stripped " + name + " as " + newfilepath)
