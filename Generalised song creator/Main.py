import random
import os

# test commit

#  /$$$$$$$$ /$$$$$$$   /$$$$$$  /$$     /$$ /$$      /$$  /$$$$$$  /$$     /$$
# |__  $$__/| $$__  $$ /$$__  $$|  $$   /$$/| $$  /$ | $$ /$$__  $$|  $$   /$$/
#    | $$   | $$  \ $$|__/  \ $$ \  $$ /$$/ | $$ /$$$| $$| $$  \ $$ \  $$ /$$/
#    | $$   | $$$$$$$/   /$$$$$/  \  $$$$/  | $$/$$ $$ $$| $$$$$$$$  \  $$$$/
#    | $$   | $$__  $$  |___  $$   \  $$/   | $$$$_  $$$$| $$__  $$   \  $$/
#    | $$   | $$  \ $$ /$$  \ $$    | $$    | $$$/ \  $$$| $$  | $$    | $$
#    | $$   | $$  | $$|  $$$$$$/    | $$    | $$/   \  $$| $$  | $$    | $$
#    |__/   |__/  |__/ \______/     |__/    |__/     \__/|__/  |__/    |__/
#
# This is a program to create a bespoke 7-track album using the style of Tekashi 6ix9ine
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


def create_ascii_art():
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
    tekashi = ("""\
     /$$$$$$$$ /$$$$$$$$ /$$   /$$  /$$$$$$   /$$$$$$  /$$   /$$ /$$$$$$
    |__  $$__/| $$_____/| $$  /$$/ /$$__  $$ /$$__  $$| $$  | $$|_  $$_/
       | $$   | $$      | $$ /$$/ | $$  \ $$| $$  \__/| $$  | $$  | $$  
       | $$   | $$$$$   | $$$$$/  | $$$$$$$$|  $$$$$$ | $$$$$$$$  | $$  
       | $$   | $$__/   | $$  $$  | $$__  $$ \____  $$| $$__  $$  | $$  
       | $$   | $$      | $$\  $$ | $$  | $$ /$$  \ $$| $$  | $$  | $$  
       | $$   | $$$$$$$$| $$ \  $$| $$  | $$|  $$$$$$/| $$  | $$ /$$$$$$
       |__/   |________/|__/  \__/|__/  |__/ \______/ |__/  |__/|______/
                """)
    brooklyn = ("""\
     /$$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$  /$$   /$$ /$$   /$$     /$$ /$$   /$$
    | $$__  $$| $$__  $$ /$$__  $$ /$$__  $$| $$  /$$/| $$  |  $$   /$$/| $$$ | $$
    | $$  \ $$| $$  \ $$| $$  \ $$| $$  \ $$| $$ /$$/ | $$   \  $$ /$$/ | $$$$| $$
    | $$$$$$$ | $$$$$$$/| $$  | $$| $$  | $$| $$$$$/  | $$    \  $$$$/  | $$ $$ $$
    | $$__  $$| $$__  $$| $$  | $$| $$  | $$| $$  $$  | $$     \  $$/   | $$  $$$$
    | $$  \ $$| $$  \ $$| $$  | $$| $$  | $$| $$\  $$ | $$      | $$    | $$\  $$$
    | $$$$$$$/| $$  | $$|  $$$$$$/|  $$$$$$/| $$ \  $$| $$$$$$$$| $$    | $$ \  $$
    |_______/ |__/  |__/ \______/  \______/ |__/  \__/|________/|__/    |__/  \__/
                """)

    ascii_options = (treyway, scumgang, gangshit, splishsplash, schmurder, tekashi, brooklyn)
    choice = random.choice(ascii_options)
    return choice


def create_song_name():
    # Function to make the song title
    # 4 letter words, all caps, consonants characters 1 and 3, vowels 2 and 4, vowels same on both
    # Populating lists of consonants and vowels
    consonants = (
    "B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z")
    vowels = ("A", "E", "I", "O", "U")

    # Create the song name
    repeated_vowel = random.choice(vowels)
    songname = random.choice(consonants) + repeated_vowel + random.choice(consonants) + repeated_vowel

    return songname


def create_album_name():
    # Function to create the album name
    # Will be a random noun from the 50 most common nouns in the English language with 69 appended
    nouns = ('Area', 'Book', 'Business', 'Case', 'Child', 'Company', 'Country', 'Day', 'Eye', 'Fact', 'Family',
             'Government', 'Group', 'Hand', 'Home', 'Job', 'Life', 'Lot', 'Man', 'Money', 'Month', 'Mother',
             'Mr', 'Night', 'Number', 'Part', 'People', 'Place', 'Point', 'Problem', 'Program', 'Question', 'Right',
             'Room', 'School', 'State', 'Story', 'Student', 'Study', 'System', 'Thing', 'Time', 'Water', 'Way',
             'Week', 'Woman', 'Word', 'Work', 'World', 'Year')
    album_name = random.choice(nouns) + " 69"

    return album_name


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


def create_song_verses_chorus():
    # Function to create the verses and the chorus

    # List of adlibs
    adlibs = [
        "(Stupid)",
        "(Stoopid)",
        "(You don't wanna die)",
        "(Ooh)",
        "(Mmm)",
        "(Mi baby; uah, uah)",
        "(Lo-loca-loca)",
        "(Hot)",
        "(Hey Michael)",
        "(Pop)",
        "(Hey!)",
        "(On the dick, hey!)",
        "(YEET)"
    ]

    # Replaces all instances of the n word with a more family friendly alternative
    adlibs = [v.replace('niggas', 'n****s') for v in adlibs]
    adlibs = [v.replace('nigga', 'n****') for v in adlibs]
    adlibs = [v.replace('Niggas', 'n****s') for v in adlibs]
    adlibs = [v.replace('Nigga', 'n****s') for v in adlibs]

    # List of verse lines
    verses = [
        "Bitch, I'm silly",
        "Spin a hoop, who the fuck is you?",
        "Niggas killed your cousin, you want smoke, nigga? Glo nigga, rollin' up your cousin in a blunt, nigga",
        "Bozo, bitch, are you dumb-d-dumb-dumb-dumb-d-dumb-dumb-dumb?",
        "I be stealin', I be robbin', I be lootin'",
        "Tell him shut up, suck a dick",
        "Your baby daddy mixtape wasn't shit, he a bitch",
        "Free Bobby, free Rowdy, free Cueno, free the 9",
        "Pussy got that wet, wet, got that drip, drip",
        "She eat my dick like it's free, free",
        "Bend her down then I make it clap, clap, clap",
        "Draco got that kick-back when I blow that, they all do track",
        "You get hit, I do not miss shots",
        "I got them big rocks in my ear, nuggets",
        "Saks Off Fifth, I'm with your bitch",
        "Hit it in the back of the Jeep-Jeep",
        "I do my own shit, I dont need 50 niggas to roll with",
        "Kick her out, I'm gettin' money now, actin' funny now"
        "I send her in the pool even though I'm rich as shit",
        "Tiki Taki, Spanish mami, she a hot tamale",
        "Drug dealer, professional pot-whipper",
        "She want me, I ain't want her, ooh",
        "Broke niggas, go stand over there",
        "Fake ass hoes, go meet 'em over there",
        "Back at it like a mothafuckin' crack addict",
        "Drop down and pick your weave up, girl",
        "You know them chicken-heads eat it up, girl",
        "Sex addict, I'm a mothafuckin' sex addict",
        "That pussy get wetter than yours",
        "Just bought a piece of Fashion Nova. Your girlfriend look like a ogre",
        "Real fly, yellow Prada socks, Bumblebee, huh",
        "The streets so cold, gotta ride wit' a pole",
        "Loaded Glock, lettin' that thing pop , they can't freeze us",
        "Glock .30, hollow tips",
        "These bitches think I'm stupid, I ain't stupid",
        "Like a Smackdown, rock bottom I'ma pin her down",
        "Licky-licky, licky on my blicky, uh",
        "Bitch, you used to fuckin' leave me on seen and shit",
        "Stupid lil' dumb nigga, now you on YouTube",
        "Police pull up on you, you gon' get to yappin'",
        "Scope with a zoom, fuck around and boom, homie",
        "Yeah that's a blackout, get dragged out and packed out",
        "Shorty dont clap back on the dick",
        "Dont clap back on the dick",
        "Bust it down, the Rollie, now she tryna fuck",
        "Sending shots to his body, make him sing like Ozuna",
        "Blocked blocks, sent shots"
    ]

    # Replaces all instances of the n word with a more family friendly alternative
    verses = [v.replace('niggas', 'n****s') for v in verses]
    verses = [v.replace('nigga', 'n****') for v in verses]
    verses = [v.replace('Niggas', 'n****s') for v in verses]
    verses = [v.replace('Nigga', 'n****s') for v in verses]

    # Creates empty list the verses, and chorus
    v1_list = []
    v2_list = []
    chorus_list = []

    # Generate basic list:
    while len(v1_list) < 6:
        lyric_v1 = random.choice(verses)

        if lyric_v1 not in v1_list:
            v1_list.append(lyric_v1)

    while len(v2_list) < 6:
        lyric_v2 = random.choice(verses)

        if lyric_v2 not in v1_list and lyric_v2 not in v2_list:
            v2_list.append(lyric_v2)

    while len(chorus_list) < 6:
        lyric_chorus = random.choice(verses)

        if lyric_chorus not in v1_list and lyric_chorus not in v2_list and lyric_chorus not in chorus_list:
            chorus_list.append(lyric_chorus)

    # Add adlibs:
    numadlibs_v1 = random.randint(0, len(v1_list))
    numadlibs_v2 = random.randint(0, len(v2_list))
    numadlibs_chorus = random.randint(0, len(chorus_list))

    # Creates verse and chorus appended lists
    v1_lines_appended = []
    v2_lines_appended = []
    chorus_lines_appended = []

    for i in range(numadlibs_v1):

        lineappend_v1 = random.randint(0, len(v1_list) - 1)

        if lineappend_v1 not in v1_lines_appended:
            v1_lines_appended.append(lineappend_v1)

            adlib_app = random.choice(adlibs)
            v1_list[lineappend_v1] += ' ' + adlib_app

    for j in range(numadlibs_v2):

        lineappend_v2 = random.randint(0, len(v2_list) - 1)

        if lineappend_v2 not in v2_lines_appended:
            v2_lines_appended.append(lineappend_v2)

            adlib_app = random.choice(adlibs)
            v2_list[lineappend_v2] += ' ' + adlib_app

    for k in range(numadlibs_chorus):

        lineappend_chorus = random.randint(0, len(chorus_list) - 1)

        if lineappend_chorus not in chorus_lines_appended:
            chorus_lines_appended.append(lineappend_chorus)

            adlib_app = random.choice(adlibs)
            chorus_list[lineappend_chorus] += ' ' + adlib_app

    return v1_list, v2_list, chorus_list


def create_outro():
    # Function to create the song outros

    # List of outro lines
    outro = [
        "Hold up, hold up, hold up, gang",
        "Run that shit back",
        "You ain't my bitch, nah",
        "It's fuckin' Target",
        "It's fuckin' Trojan",
        "Little thottie, got her rowdy, choosing everybody",
        "Yo, chill, chill, chill, chill, chill, woah, woah, woah",
        "Now stop",
        "You cannot say that, bro, c'mon",
        "Lately, I been on some 'suck my dick' shit",
        "I can't sleep, I can't sleep",
        "Bitch, I'm stressin', oh, bitch, I'm stressin'",
        "Why you tweet my shit?",
        "DVDs, porno tapes",
        "Do you beat your meat to a porno tape?",
        "Watch his body Milly Rock, yeah"
    ]

    # Replaces all instances of the n word with a more family friendly alternative
    outro = [v.replace('niggas', 'n****s') for v in outro]
    outro = [v.replace('nigga', 'n****') for v in outro]
    outro = [v.replace('Niggas', 'n****s') for v in outro]
    outro = [v.replace('Nigga', 'n****s') for v in outro]

    # Creates an empty outro list
    outro_list = []

    while len(outro_list) < 3:

        lyric_app = random.choice(outro)

        if lyric_app not in outro_list:
            outro_list.append(lyric_app)

    return outro_list


def create_whole_song(album_name):
    # Function to put together all the elements for your finished 6ix9ine Masterpiece

    # Verse 2 will feature a rapper as ever hit needs someone else to spit bars
    feat_list = ('Kanye West', 'Nicki Minaj', 'Bobby Shmurder', 'A Boogie Wit Da Hoodie', 'Gunna', 'Trife Drew',
                 'DJ Spinking', 'Torey Lanez', 'Murda Beats', 'Fetty Wap', 'Young Thug')
    number = random.randint(0, 100)

    feat_artist = False
    if number < 30:
        feat_artist = True

    if feat_artist:
        feat = random.choice(feat_list)

    ascii = create_ascii_art()
    if feat_artist:
        song_name = create_song_name() + ' (feat ' + feat + ')'
    else:
        song_name = create_song_name()

    song_intro = create_intro()
    v1, v2, chorus = create_song_verses_chorus()
    outro = create_outro()

    # Add dividing line
    dash = '-' * 20

    dir_path = os.path.dirname(os.path.realpath(__file__))
    if not os.path.exists(album_name):
        os.makedirs(album_name)

    song_path = os.path.dirname(os.path.realpath(__file__)) + "/" + album_name + "/" + song_name + ".txt"
    if os.path.exists(song_path):
        song_name = song_name + " (Part 2)"

    # Write the song out to a file
    with open(album_name + "/" + song_name + '.txt', 'a') as the_file:
        the_file.write(ascii)
        the_file.write('\n')
        the_file.write(dash)
        the_file.write('\n')
        the_file.write('SONG NAME: ' + song_name)
        the_file.write('\n')
        the_file.write(dash)
        the_file.write('\n')
        the_file.write('INTRO:')
        the_file.write('\n')
        the_file.write(dash)
        the_file.write('\n')
        the_file.write('\n'.join(song_intro))
        the_file.write('\n')
        the_file.write(dash)
        the_file.write('\n')
        the_file.write('VERSE ONE:')
        the_file.write('\n')
        the_file.write(dash)
        the_file.write('\n')
        the_file.write('\n'.join(v1))
        the_file.write('\n')
        the_file.write(dash)
        the_file.write('\n')
        the_file.write('CHORUS:')
        the_file.write('\n')
        the_file.write(dash)
        the_file.write('\n')
        the_file.write('\n'.join(chorus))
        the_file.write('\n')
        the_file.write(dash)
        the_file.write('\n')
        if feat_artist:
            the_file.write('VERSE TWO' + ' (' + feat + '):')
        else:
            the_file.write('VERSE TWO:')
        the_file.write('\n')
        the_file.write(dash)
        the_file.write('\n')
        the_file.write('\n'.join(v2))
        the_file.write('\n')
        the_file.write(dash)
        the_file.write('\n')
        the_file.write('OUTRO:')
        the_file.write('\n')
        the_file.write(dash)
        the_file.write('\n')
        the_file.write('\n'.join(outro))


album_name = create_album_name()
for i in range(7):
    create_whole_song(album_name)
