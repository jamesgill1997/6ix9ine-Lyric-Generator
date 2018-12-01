import random

# This is a program to create bespoke songs using the style of Tekashi 6ix9ine
# In the form of:
#               -- intro
#               -- verse 1
#               -- chorus
#               -- verse 2 (feature)
#               -- chorus
#               -- outro


def create_finished_song():
    # Function to put together all the elements for your finished 6ix9ine Masterpiece
    create_song_name()


def create_song_name():
    # Function to make the song title
    # 4 letter words, all caps, consonants characters 1 and 3, vowels 2 and 4, vowels same on both
    # Populating lists of consonants and vowels
    consonants = ("B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z")
    vowels = ("A", "E", "I", "O", "U", "Y")

    # Create the song name
    repeated_vowel = random.choice(vowels)
    songname = random.choice(consonants) + repeated_vowel + random.choice(consonants) + repeated_vowel
    print("Your song title is \"" + songname + "\"")


create_finished_song()
