import random
import lyricsgenius as genius
import json
import markovify
import os

artist_one = 'Skepta'
artist_two = 'Stevie Wonder'
num_songs = 5

dash = '-'*60

## Finding Songs by Artist

api = genius.Genius('uDarA9_cUEi8NgSiEliFR8Lu-TRl-sanYEfw1_fDNLRyejlgXDul2-QfYJZ4SvQF')
artist_1 = api.search_artist(artist_one, max_songs=num_songs)
artist_2 = api.search_artist(artist_two, max_songs=num_songs)

## Saving Song Lyrics to JSON

artist_1.save_lyrics()
artist_2.save_lyrics()

with open('Lyrics_{}.json'.format(artist_one.replace(' ','')), 'r') as fp:
    obj_1 = json.load(fp)

with open('Lyrics_{}.json'.format(artist_two.replace(' ','')), 'r') as fp:
    obj_2 = json.load(fp)

## Saving JSON Data to Text File

with open('all_lyrics_1' + '.txt', 'a') as the_file:
    for i in range(len(obj_1['songs'])):
        the_file.write(obj_1['songs'][i]['lyrics'])

with open('all_lyrics_2' + '.txt', 'a') as the_file:
    for i in range(len(obj_2['songs'])):
        the_file.write(obj_2['songs'][i]['lyrics'])

## Opening Text Files

text_1 = open("all_lyrics_1.txt").read()
text_2 = open("all_lyrics_2.txt").read()

## Creating Markov Models

model_1 = markovify.NewlineText(text_1, state_size=2)
model_2 = markovify.NewlineText(text_2, state_size=2)

combined_model = markovify.combine([model_1, model_2])

## Printing Final Song

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



