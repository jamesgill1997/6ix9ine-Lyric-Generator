import random
import os

#  /$$$$$$$$ /$$$$$$$   /$$$$$$  /$$     /$$ /$$      /$$  /$$$$$$  /$$     /$$
# |__  $$__/| $$__  $$ /$$__  $$|  $$   /$$/| $$  /$ | $$ /$$__  $$|  $$   /$$/
#    | $$   | $$  \ $$|__/  \ $$ \  $$ /$$/ | $$ /$$$| $$| $$  \ $$ \  $$ /$$/
#    | $$   | $$$$$$$/   /$$$$$/  \  $$$$/  | $$/$$ $$ $$| $$$$$$$$  \  $$$$/
#    | $$   | $$__  $$  |___  $$   \  $$/   | $$$$_  $$$$| $$__  $$   \  $$/
#    | $$   | $$  \ $$ /$$  \ $$    | $$    | $$$/ \  $$$| $$  | $$    | $$
#    | $$   | $$  | $$|  $$$$$$/    | $$    | $$/   \  $$| $$  | $$    | $$
#    |__/   |__/  |__/ \______/     |__/    |__/     \__/|__/  |__/    |__/
#
# This is a program to create bespoke songs using the style of Tekashi 6ix9ine
# In the form of:
#               -- intro
#               -- verse 1
#               -- chorus
#               -- verse 2 (feature)
#               -- chorus
#               -- outro
#
#   /$$$$$$   /$$$$$$  /$$   /$$ /$$      /$$      /$$$$$$   /$$$$$$  /$$   /$$  /$$$$$$
# /$$__  $$ /$$__  $$| $$  | $$| $$$    /$$$     /$$__  $$ /$$__  $$| $$$ | $$ /$$__  $$
# | $$  \__/| $$  \__/| $$  | $$| $$$$  /$$$$    | $$  \__/| $$  \ $$| $$$$| $$| $$  \__/
# |  $$$$$$ | $$      | $$  | $$| $$ $$/$$ $$    | $$ /$$$$| $$$$$$$$| $$ $$ $$| $$ /$$$$
#  \____  $$| $$      | $$  | $$| $$  $$$| $$    | $$|_  $$| $$__  $$| $$  $$$$| $$|_  $$
#  /$$  \ $$| $$    $$| $$  | $$| $$\  $ | $$    | $$  \ $$| $$  | $$| $$\  $$$| $$  \ $$
# |  $$$$$$/|  $$$$$$/|  $$$$$$/| $$ \/  | $$    |  $$$$$$/| $$  | $$| $$ \  $$|  $$$$$$/
#  \______/  \______/  \______/ |__/     |__/     \______/ |__/  |__/|__/  \__/ \______/


def print_ascii_art():
    # Function to add sick ascii art in the console
    treyway = ("""\
     /$$$$$$$$ /$$$$$$$   /$$$$$$  /$$     /$$ /$$      /$$  /$$$$$$  /$$     /$$
    |__  $$__/| $$__  $$ /$$__  $$|  $$   /$$/| $$  /$ | $$ /$$__  $$|  $$   /$$/
       | $$   | $$  \ $$|__/  \ $$ \  $$ /$$/ | $$ /$$$| $$| $$  \ $$ \  $$ /$$/
       | $$   | $$$$$$$/   /$$$$$/  \  $$$$/  | $$/$$ $$ $$| $$$$$$$$  \  $$$$/
       | $$   | $$__  $$  |___  $$   \  $$/   | $$$$_  $$$$| $$__  $$   \  $$/
       | $$   | $$  \ $$ /$$  \ $$    | $$    | $$$/ \  $$$| $$  | $$    | $$
       | $$   | $$  | $$|  $$$$$$/    | $$    | $$/   \  $$| $$  | $$    | $$
       |__/   |__/  |__/ \______/     |__/    |__/     \__/|__/  |__/    |__/
                        """)
    scumgang = ("""\
      /$$$$$$   /$$$$$$  /$$   /$$ /$$      /$$      /$$$$$$   /$$$$$$  /$$   /$$  /$$$$$$
     /$$__  $$ /$$__  $$| $$  | $$| $$$    /$$$     /$$__  $$ /$$__  $$| $$$ | $$ /$$__  $$
     | $$  \__/| $$  \__/| $$  | $$| $$$$  /$$$$    | $$  \__/| $$  \ $$| $$$$| $$| $$  \__/
     |  $$$$$$ | $$      | $$  | $$| $$ $$/$$ $$    | $$ /$$$$| $$$$$$$$| $$ $$ $$| $$ /$$$$
      \____  $$| $$      | $$  | $$| $$  $$$| $$    | $$|_  $$| $$__  $$| $$  $$$$| $$|_  $$
      /$$  \ $$| $$    $$| $$  | $$| $$\  $ | $$    | $$  \ $$| $$  | $$| $$\  $$$| $$  \ $$
     |  $$$$$$/|  $$$$$$/|  $$$$$$/| $$ \/  | $$    |  $$$$$$/| $$  | $$| $$ \  $$|  $$$$$$/
      \______/  \______/  \______/ |__/     |__/     \______/ |__/  |__/|__/  \__/ \______/
                        """)
    gangshit = ("""\
      /$$$$$$   /$$$$$$  /$$   /$$  /$$$$$$       /$$$$$$  /$$   /$$ /$$$$$$ /$$$$$$$$
     /$$__  $$ /$$__  $$| $$$ | $$ /$$__  $$     /$$__  $$| $$  | $$|_  $$_/|__  $$__/
    | $$  \__/| $$  \ $$| $$$$| $$| $$  \__/    | $$  \__/| $$  | $$  | $$     | $$   
    | $$ /$$$$| $$$$$$$$| $$ $$ $$| $$ /$$$$    |  $$$$$$ | $$$$$$$$  | $$     | $$   
    | $$|_  $$| $$__  $$| $$  $$$$| $$|_  $$     \____  $$| $$__  $$  | $$     | $$   
    | $$  \ $$| $$  | $$| $$\  $$$| $$  \ $$     /$$  \ $$| $$  | $$  | $$     | $$   
    |  $$$$$$/| $$  | $$| $$ \  $$|  $$$$$$/    |  $$$$$$/| $$  | $$ /$$$$$$   | $$   
     \______/ |__/  |__/|__/  \__/ \______/      \______/ |__/  |__/|______/   |__/   
                """)
    splishsplash = ("""\
      /$$$$$$  /$$$$$$$  /$$       /$$$$$$  /$$$$$$  /$$   /$$      /$$$$$$  /$$$$$$$  /$$        /$$$$$$   /$$$$$$  /$$   /$$
     /$$__  $$| $$__  $$| $$      |_  $$_/ /$$__  $$| $$  | $$     /$$__  $$| $$__  $$| $$       /$$__  $$ /$$__  $$| $$  | $$
    | $$  \__/| $$  \ $$| $$        | $$  | $$  \__/| $$  | $$    | $$  \__/| $$  \ $$| $$      | $$  \ $$| $$  \__/| $$  | $$
    |  $$$$$$ | $$$$$$$/| $$        | $$  |  $$$$$$ | $$$$$$$$    |  $$$$$$ | $$$$$$$/| $$      | $$$$$$$$|  $$$$$$ | $$$$$$$$
     \____  $$| $$____/ | $$        | $$   \____  $$| $$__  $$     \____  $$| $$____/ | $$      | $$__  $$ \____  $$| $$__  $$
     /$$  \ $$| $$      | $$        | $$   /$$  \ $$| $$  | $$     /$$  \ $$| $$      | $$      | $$  | $$ /$$  \ $$| $$  | $$
    |  $$$$$$/| $$      | $$$$$$$$ /$$$$$$|  $$$$$$/| $$  | $$    |  $$$$$$/| $$      | $$$$$$$$| $$  | $$|  $$$$$$/| $$  | $$
     \______/ |__/      |________/|______/ \______/ |__/  |__/     \______/ |__/      |________/|__/  |__/ \______/ |__/  |__/
                """)
    schmurder = ("""\
      /$$$$$$   /$$$$$$  /$$   /$$ /$$      /$$ /$$   /$$ /$$$$$$$  /$$$$$$$  /$$$$$$$$ /$$$$$$$ 
     /$$__  $$ /$$__  $$| $$  | $$| $$$    /$$$| $$  | $$| $$__  $$| $$__  $$| $$_____/| $$__  $$
    | $$  \__/| $$  \__/| $$  | $$| $$$$  /$$$$| $$  | $$| $$  \ $$| $$  \ $$| $$      | $$  \ $$
    |  $$$$$$ | $$      | $$$$$$$$| $$ $$/$$ $$| $$  | $$| $$$$$$$/| $$  | $$| $$$$$   | $$$$$$$/
     \____  $$| $$      | $$__  $$| $$  $$$| $$| $$  | $$| $$__  $$| $$  | $$| $$__/   | $$__  $$
     /$$  \ $$| $$    $$| $$  | $$| $$\  $ | $$| $$  | $$| $$  \ $$| $$  | $$| $$      | $$  \ $$
    |  $$$$$$/|  $$$$$$/| $$  | $$| $$ \/  | $$|  $$$$$$/| $$  | $$| $$$$$$$/| $$$$$$$$| $$  | $$
     \______/  \______/ |__/  |__/|__/     |__/ \______/ |__/  |__/|_______/ |________/|__/  |__/
                """)
    ascii_options = (treyway, scumgang, gangshit, splishsplash, schmurder)
    print(random.choice(ascii_options))


def create_intro():
    # Function to create the introduction to our song

    # List of intro lines
    intro = [
        "You rockin' with Take Money Promotions",
        "Take Money Promotions",
        "Y'all already know it be the boy Yung Gordon",
        "It's fuckin' TR3YWAY!",
        "Bitch, we in the city on that hot shit",
        "Uh",
        "Bebe, no te pasa nada, vuelvete loca",
        "M-M-M-Murda",
        "I prayed to the lord that he'd watch my family",
        "B.B. with the Robin's, lookin' all retarded",
        "Scum Gang!",
        "Bitches suck my dick, 'cause I'm fly like Aladdin"
    ]

    # Replaces all instances of the n word with a more family friendly alternative
    intro = [v.replace('niggas', 'n****s') for v in intro]
    intro = [v.replace('nigga', 'n****') for v in intro]
    intro = [v.replace('Niggas', 'n****s') for v in intro]
    intro = [v.replace('Nigga', 'n****s') for v in intro]

    # List of producer taglines
    producer_tagline = [
        "Yung Lan on the track",
        "Scott Storch",
        "Custodian, will you pack my fudge?",
        "We got London on da track",
        "I'm in London, got my beat from London"
    ]

    # Replaces all instances of the n word with a more family friendly alternative
    producer_tagline = [v.replace('niggas', 'n****s') for v in producer_tagline]
    producer_tagline = [v.replace('nigga', 'n****') for v in producer_tagline]
    producer_tagline = [v.replace('Niggas', 'n****s') for v in producer_tagline]
    producer_tagline = [v.replace('Nigga', 'n****s') for v in producer_tagline]

    # List of intro-to-verse transitions
    transition = [
        "Tay Keith, fuck these niggas up",
        "Murda on the beat so it's not nice!",
        "I do my own stunts, Jackie Chan with it",
        "Real nigga, quick to pull a fucking trigger",
        "I blow that shit, now you where Bobby Shmurda's hat went!"
    ]

    # Replaces all instances of the n word with a more family friendly alternative
    transition = [v.replace('niggas', 'n****s') for v in transition]
    transition = [v.replace('nigga', 'n****') for v in transition]
    transition = [v.replace('Niggas', 'n****s') for v in transition]
    transition = [v.replace('Nigga', 'n****s') for v in transition]

    # Create a empty list
    intro_list = []

    # While loop to add intro lines up until a certain limit
    while len(intro_list) < 3:

        lyric_app = random.choice(intro)

        if lyric_app not in intro_list:
            intro_list.append(lyric_app)

    # Adds a producer tagline to the end of the intro
    intro_list.append(random.choice(producer_tagline))

    return intro_list


def create_finished_song():
    # Function to put together all the elements for your finished 6ix9ine Masterpiece
    create_song_name()
    create_intro()


def create_song_name():
    # Function to make the song title
    # 4 letter words, all caps, consonants characters 1 and 3, vowels 2 and 4, vowels same on both
    # Populating lists of consonants and vowels
    consonants = ("B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z")
    vowels = ("A", "E", "I", "O", "U")

    # Create the song name
    repeated_vowel = random.choice(vowels)
    songname = random.choice(consonants) + repeated_vowel + random.choice(consonants) + repeated_vowel
    print("Your song title is: \"" + songname + "\"")


print_ascii_art()
create_finished_song()
