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

# Adding user inputted artists to a list of size num_artists
for i in range(num_artists):
    artists.append(input("Who is artist " + str(i+1) + "?"))


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

# Saving artists lyrics to separate files
file_list = []
for count, i in enumerate(json_list):
    with open('all_lyrics_' + str(count) + '.txt', 'a') as the_file:
        for j in range(len(i['songs'])):
            the_file.write(i['songs'][j]['lyrics'])
    file_list.append('all_lyrics_' + str(i))

# Opening text files - opens with type: <class '_io.TextIOWrapper'>
open_files = []
for count, i in enumerate(file_list):
    open_files.append(open('all_lyrics_' + str(count) + '.txt'))

# Creates markov chain models for each of the open files
markov_models = {}
for count, i in enumerate(open_files):
    markov_models['model_{}'.format(count)] = markovify.NewlineText(i, state_size=2)

# Combines all markov chains
# TODO Need to make user input for whether they want a mixture of artists in one go, or just as features
combined_model = markovify.combine(list(markov_models.values()))


# ALBUM SECTION

# Asks for inputs regarding the album
album_name = input('What is the album name: ')
num_songs_album = int(input('How many songs in the album: '))
# Checks if the album already exists or not
album_bool = True
while album_bool:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    if not os.path.exists(album_name):
        os.makedirs(album_name)
        album_bool = False
    else:
        print('This album already exists.')
        album_name = input('What is the album name: ')

# Generates the songs with a specific template and adds them into the album
# TODO Make a nicer format for the printing of the song to the file
for i in range(num_songs_album):
    with open(album_name + "/" + 'Song_{}'.format(i+1) + '.txt', 'a') as the_file:
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