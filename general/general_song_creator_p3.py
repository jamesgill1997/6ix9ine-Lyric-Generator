import lyricsgenius as genius
import json
import markovify
import os

# TODO replace lyricsgenius with Genius' API + web scraper
# TODO implement flask wrapper to provide inputs
# TODO more front end development

# Allowing user inputs to decide how many artists will be used when making the album
num_artists = int(input("How many artists to combine?"))

# Initialising variables and lists
artists = []
i = 0

# Adding user inputted artists to a list of size num_artists
while num_artists > 0:
    current_artist = i + 1
    artists.append(input("Who is artist " + str(current_artist) + "?"))
    num_artists = num_artists - 1
    i = i + 1

# Choosing the number of songs to use when creating the new songs
num_songs_used = int(input("How many songs should be used to create the new songs?"))

dash = '-'*60

# Finding songs by the chosen artists using the genius api
api = genius.Genius('uDarA9_cUEi8NgSiEliFR8Lu-TRl-sanYEfw1_fDNLRyejlgXDul2-QfYJZ4SvQF')
artist_api = {}
for i in range(len(artists)):
    artist_api[artists[i]] = api.search_artist(artists[i], max_songs=num_songs_used)

# Saving the lyrics for the chosen artists and number of songs as a json file
for key, value in artist_api.items():
    artist_api[key].save_lyrics()

# Loading the json into memory as a variable
json_list = []
for i in artists:
    with open('Lyrics_{}.json'.format(i.replace(' ','')), 'r') as fp:
        obj = json.load(fp)
        json_list.append(obj)

# Saving all the lyrics into one file
for i in json_list:
    with open('all_lyrics_1' + '.txt', 'a') as the_file:
        for j in range(len(i['songs'])):
            the_file.write(i['songs'][j]['lyrics'])


with open('all_lyrics_1' + '.txt', 'a') as the_file:
    for i in range(len(obj_1['songs'])):
        the_file.write(obj_1['songs'][i]['lyrics'])

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################


artist_one = '21 Savage'
artist_two = 'Drake'
num_songs = 10


# Finding Songs by Artist

api = genius.Genius('uDarA9_cUEi8NgSiEliFR8Lu-TRl-sanYEfw1_fDNLRyejlgXDul2-QfYJZ4SvQF')
artist_1 = api.search_artist(artist_one, max_songs=num_songs)
artist_2 = api.search_artist(artist_two, max_songs=num_songs)

# Saving Song Lyrics to JSON

artist_1.save_lyrics()
artist_2.save_lyrics()

with open('Lyrics_{}.json'.format(artist_one.replace(' ','')), 'r') as fp:
    obj_1 = json.load(fp)

with open('Lyrics_{}.json'.format(artist_two.replace(' ','')), 'r') as fp:
    obj_2 = json.load(fp)

# Saving JSON Data to Text File

with open('all_lyrics_1' + '.txt', 'a') as the_file:
    for i in range(len(obj_1['songs'])):
        the_file.write(obj_1['songs'][i]['lyrics'])

with open('all_lyrics_2' + '.txt', 'a') as the_file:
    for i in range(len(obj_2['songs'])):
        the_file.write(obj_2['songs'][i]['lyrics'])

# Opening Text Files

text_1 = open("all_lyrics_1.txt").read()
text_2 = open("all_lyrics_2.txt").read()

# Creating Markov Models

model_1 = markovify.NewlineText(text_1, state_size=2)
model_2 = markovify.NewlineText(text_2, state_size=2)

combined_model = markovify.combine([model_1, model_2])

# Printing Final Song

album_name = 'album_one'

dir_path = os.path.dirname(os.path.realpath(__file__))
if not os.path.exists(album_name):
    os.makedirs(album_name)


for i in range(8):
    with open(album_name + "/" + 'song_{}'.format(i) + '.txt', 'a') as the_file:
        the_file.write('VERSE ONE')
        the_file.write('\n')
        the_file.write(dash)
        the_file.write('\n')
        for i in range(4):
            the_file.write(combined_model.make_sentence(tries=150))
            the_file.write('\n')

        the_file.write('\n')

        the_file.write('VERSE TWO')
        the_file.write('\n')
        the_file.write(dash)
        the_file.write('\n')

        for i in range(8):
            the_file.write(combined_model.make_sentence(tries=150))
            the_file.write('\n')

        the_file.write('\n')

        the_file.write('VERSE THREE')
        the_file.write('\n')
        the_file.write(dash)
        the_file.write('\n')

        for i in range(4):
            the_file.write(combined_model.make_sentence(tries=150))
            the_file.write('\n')



