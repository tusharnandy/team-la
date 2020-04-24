def knn(dataframe, k, history):

    avg_coordinates = []
    for dim in space:
        avg = 0
        for p in history:
            avg += dataframe.loc[dataframe["Song Name"] == p, dim].values[0]
        avg /= len(history)
        avg_coordinates.append(avg)

    list = dataframe["Song Name"].values.tolist()
    list.remove(current_song)
    upcoming = []

    for j in range(k):

        nextsong = ''
        min = 10**8

        for next in list:
            dist = 0

            for dim in range(len(space)):
                dist += (dataframe.loc[dataframe["Song Name"] == next, space[dim]].values[0] - avg_coordinates[dim]) ** 2

            dist = np.sqrt(dist)
            if dist < min:
                min = dist
                nextsong = next

        list.remove(nextsong)
        upcoming.append(nextsong)

    return upcoming

import pandas as pd
import numpy as np

path = "Songs_LA - Sheet1.csv"
database = pd.read_csv(path)


space = database.columns.tolist()[2:]
space.pop(3)

df = database

print('''WElCOME...!!!''')

current_song = input("\nPlease type your first song: ")


rejection_score = [0]*60
recent_history = [current_song]


song1, song2 = knn(df, 2, recent_history)

while True:

    print(f'''\nCurrently playing: {current_song}
            Upcoming song:{song1}\n''')

    command = input("Type command here: ").lower()

    if command == "next":
        current_song = song1
        song1 = song2

        if len(recent_history) < 4:
            recent_history.append(current_song)
        else:
            recent_history.remove(recent_history[0])
            recent_history.append(current_song)


        song2 = knn(df, 1, recent_history)

    elif command == "skip-next":

        current_song = song2

        if len(recent_history) < 4:
            recent_history.append(current_song)
        else:
            recent_history.remove(recent_history[0])
            recent_history.append(current_song)

        for song1_num in range (60):
            if song1 == df['Song Name'][song1_num]:
                break

        moods = df.columns.tolist()[2:5]
        mood = moods[0]
        for i in range(1, 3):
            if df[mood][song1_num] < df[moods[i]][song1_num]:
                mood = moods[i]

        if rejection_score[song1_num] == 0 and df[mood][song1_num] != 0:
            df[mood][song1_num] -= 0.5
        elif df[mood][song1_num] != 0:
            df[mood][song1_num] -= (0.5)**(1/3)

        song1, song2 = knn(df, 2, recent_history)

    elif command == "search":
        current_song = input("What would you like to hear? ").lower()

        # code for negative marking

    elif command == "exit":
        break
