import lyricsgenius as genius
import json
import markovify
import os
import shutil
import random

## LONG TERM
# TODO replace lyricsgenius with Genius' API + web scraper
# TODO implement flask wrapper to provide inputs
# TODO more front end development

## SHORT TERM
# TODO Look into how to make file paths cleaner
# TODO Make a nicer format for the printing of the song to the file

# Generate folder to store temporary files
if not os.path.exists('tmp_files'):
    os.makedirs('tmp_files')

# Give the user the option of combining artists together or having an artist with features
print("Song Creator - Version 1.0")
print("There are two options for how you want to use the program:")
print("1) Create new songs with one artist as the main and others as features")
print("2) Combine several artists lyrical style together to generate new mashups")
song_type = input("Do you want to choose option one or two? (Type 'one' or 'two' only)")

# Adding error handling for if the user enters an invalid string
while song_type != 'one' and song_type != 'two':
    print(song_type)
    print("Sorry, please type 'one' or 'two'")
    song_type = input("Do you want to choose option 1 or 2? (Type 'one' or 'two' only)")

# Initialising variables and lists
artists = []
num_songs_album = 0
feature_songs = []
number_of_features = 0

# Choosing the details if option 1 is chosen
if song_type == 'one':
    # Allowing the user to choose a single song or an album
    album_or_song = input("Do you want to make a single song or an album? (Type 'album' or 'song')")

    # Adding error handling for if the user enters an invalid string
    while album_or_song != 'album' and album_or_song != 'song':
        print("Sorry, please type 'album' or 'song'")
        album_or_song = input("Do you want to make a single song or an album? (Type 'album' or 'song')")

    # Allowing the user to choose the number of songs in the album
    if album_or_song == "album":
        num_songs_album = int(input("How many tracks in the album?"))
    else:
        num_songs_album = 1

    # Allowing the user to choose whether they would like features in the song(s)
    check_features = input("Would you like to add features? (Type 'yes' or 'no')")

    # Adding error handling for if the user enters an invalid string
    while check_features != 'yes' and check_features != 'no':
        print("Sorry, please type 'yes' or 'no'")
        check_features = input("Would you like to add features? (Type 'yes' or 'no')")

    # Adding a variable for the number of features
    number_of_features = random.randint(0, num_songs_album // 3)
    if number_of_features == 0:
        number_of_features += 1

    # Adding the main artist to the artists list
    artists.append(input("Who is the main artist?"))

    # Adding the feature artists
    print("You have " + str(number_of_features) + " features.")
    for i in range(number_of_features):
        artists.append(input("Who is featured artist " + str(i + 1) + "?"))

# Choosing the details if option 2 is chosen
if song_type == 'two':
    # Allowing user inputs to decide how many artists will be used when making the album
    num_artists = int(input("How many artists to combine?"))

    # Adding user inputted artists to a list of size num_artists
    for i in range(num_artists):
        artists.append(input("Who is artist " + str(i + 1) + "?"))

# Choosing the number of songs to use when creating the new songs
dash = '-'*60
print()
print(dash)
print()
print("Song creator uses an artists previous work to generate new songs.")
print("The more songs you choose to use, the more original the new songs will be!")
num_songs_used = int(input("How many songs should be used to create the new songs?"))

# Finding songs by the chosen artists using the genius api
api = genius.Genius('uDarA9_cUEi8NgSiEliFR8Lu-TRl-sanYEfw1_fDNLRyejlgXDul2-QfYJZ4SvQF')
artist_api = {}
for i in range(len(artists)):
    artist_api[artists[i]] = api.search_artist(artists[i], max_songs=num_songs_used)

# Saving the lyrics for the chosen artists and number of songs as a json file
for key, value in artist_api.items():
    tmp_path = os.path.dirname(os.path.realpath(__file__)) + '/tmp_files/Lyrics_{}'.format(str(key).replace(' ', ''))
    artist_api[key].save_lyrics(filename=tmp_path)

# Loading the json into memory as a variable
json_list = []
for i in artists:
    with open(os.path.dirname(os.path.realpath(__file__)) + '/tmp_files/Lyrics_{}.json'.format(i.replace(' ','')), 'r') as fp:
        obj = json.load(fp)
        json_list.append(obj)

# Saving artists lyrics to separate files
file_list = []
for count, i in enumerate(json_list):
    with open(os.path.dirname(os.path.realpath(__file__)) + '/tmp_files/all_lyrics_' + str(count) + '.txt', 'a') as the_file:
        for j in range(len(i['songs'])):
            the_file.write(i['songs'][j]['lyrics'])
    file_list.append('all_lyrics_' + str(i))

# Opening text files - opens with type: <class '_io.TextIOWrapper'>
open_files = []
for count, i in enumerate(file_list):
    open_files.append(open(os.path.dirname(os.path.realpath(__file__)) + '/tmp_files/all_lyrics_' + str(count) + '.txt'))

# Creates markov chain models for each of the open files
markov_models = {}
combined_model = {}
for count, i in enumerate(open_files):
    markov_models['model_{}'.format(count)] = markovify.NewlineText(i, state_size=2)

# Combining the markov chains if option 2 is chosen
if song_type == 'two':
    # Combines all markov chains for option two
    combined_model = markovify.combine(list(markov_models.values()))

# ALBUM SECTION

# Asks for album name
album_name = input('What is the album name: ')

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

# Choosing the number of tracks if option 2 is chosen
if song_type == 'two':
    num_songs_album = int(input('How many songs in the album: '))

# Choosing which songs get features for option one
num_features_used = 0
if song_type == 'one':
    while len(feature_songs) < number_of_features:
        feature_songs.append(random.randrange(num_songs_album))
        feature_songs = list(set(feature_songs))

# Generates the songs with a specific template and adds them into the album
for i in range(num_songs_album):

    if i in feature_songs:
        num_features_used += 1
        song_name = 'Song_{0}_ft_{1}'.format(i+1,artists[num_features_used]) + '.txt'
    else:
        song_name = 'Song_{}'.format(i+1) + '.txt'

    # with open(album_name + "/" + 'Song_{}'.format(i+1) + '.txt', 'a') as the_file:
    with open(album_name + '/' + song_name, 'a') as the_file:
        the_file.write('VERSE ONE')
        the_file.write('\n')
        the_file.write(dash)
        the_file.write('\n')
        # Choosing the verse one lyrics if option 1 is chosen
        if song_type == 'one':
            for j in range(4):
                the_file.write(markov_models.get('model_0').make_sentence(tries=150))
                the_file.write('\n')
        # Choosing the verse one lyrics if option 2 is chosen
        if song_type == 'two':
            for j in range(4):
                the_file.write(combined_model.make_sentence(tries=150))
                the_file.write('\n')

        the_file.write('\n')
        the_file.write('\n')

        # Choosing the verse two lyrics if option 1 is chosen
        if song_type == 'one':
            # Checks if the track will have a feature
            if i in feature_songs:
                the_file.write('VERSE TWO (' + artists[num_features_used] + ')')
                the_file.write('\n')
                the_file.write(dash)
                the_file.write('\n')
                for j in range(8):
                    # Feature therefore make lyrics using a featured artist
                    the_file.write(markov_models.get('model_' + str(num_features_used-1)).make_sentence(tries=150))
                    the_file.write('\n')
            else:
                the_file.write('VERSE TWO')
                the_file.write('\n')
                the_file.write(dash)
                the_file.write('\n')
                for j in range(8):
                    the_file.write(markov_models.get('model_0').make_sentence(tries=150))
                    the_file.write('\n')

        the_file.write('\n')

        # Choosing the verse two lyrics if option 2 is chosen
        if song_type == 'two':
            the_file.write('VERSE TWO')
            the_file.write('\n')
            the_file.write(dash)
            the_file.write('\n')
            for j in range(8):
                the_file.write(combined_model.make_sentence(tries=150))
                the_file.write('\n')
            the_file.write('\n')

        the_file.write('\n')

        the_file.write('VERSE THREE')
        the_file.write('\n')
        the_file.write(dash)
        the_file.write('\n')

        # Choosing the verse three lyrics if option 1 is chosen
        if song_type == 'one':
            for j in range(4):
                the_file.write(markov_models.get('model_0').make_sentence(tries=150))
                the_file.write('\n')
        # Choosing the verse three lyrics if option 2 is chosen
        if song_type == 'two':
            for j in range(4):
                the_file.write(combined_model.make_sentence(tries=150))
                the_file.write('\n')

# Remove unnecessary files generated
shutil.rmtree(os.path.dirname(os.path.realpath(__file__)) + '/tmp_files/')
