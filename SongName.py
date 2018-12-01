import random

# Function to make the song title
# 4 letter words, all caps, consonants characters 1 and 3, vowels 2 and 4, vowels same on both


def create_song_name():
    # Populating lists of consonants and vowels
    consonants = ("B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z")
    vowels = ("A", "E", "I", "O", "U", "Y")

    # Create the song name
    repeated_vowel = random.choice(vowels)
    songname = random.choice(consonants) + repeated_vowel + random.choice(consonants) + repeated_vowel