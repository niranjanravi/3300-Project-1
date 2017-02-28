song_list = []

def preprocess_corpus(save_as, artist):
	with open('songdata.csv') as f:
		contents = f.read()

	split = contents.split('"')

	for index, song in enumerate(split):
		if (index % 2 == 1 and artist in song) :
			song_list.append(split[index+1])

	with open(save_as,'w') as out:
		for song in song_list:
			out.write(song)


preprocess_corpus("data/drake.txt",drake)
