# I am assuming that all the relevant information is in lists or numpy arrays

import numpy as np

print('''WElCOME...!!!''')

song_current = input("\nPlease type your first song: ")

while True:

    # Code for knn selection

    song1, song2, song3 = ['A', 'B', 'C']
    print(f'''\nCurrently playing: {song_current}
            Upcoming songs: 1. {song1}  2. {song2}  3. {song3}\n''')

    command = input("Type command here: ").lower()

    if command == "next":
        song_current = song1

        # some code for scoring the recommendation

    elif command == "skip-next":
        song_current = song2

        # some code for scoring, different as compared to the previous one

    elif command = "search":
        song_current = input("What would you like to hear? ").lower()

        # code for negative marking

    elif command = "exit":
        break
