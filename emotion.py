import numpy as np
import streamlit as st
import pandas as pd
import cv2
from collections import Counter
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D

# Read csv file containing data.
df = pd.read_csv('muse_v3.csv')

# Renaming column of dataframe.
df['link'] = df['lastfm_url']
df['name'] = df['track']
df['emotional'] = df['number_of_emotion_tags']
df['pleasant'] = df['valence_tags']

# Taking out useful column.
df = df[['name','emotional','pleasant','link','artist']]

# Sort column based on emotional & pleasant column value.
# Pleasant = degree of pleasant in that particular song.
# Emotional = emotional word used in that song.
df = df.sort_values(by=["emotional", "pleasant"])
df.reset_index()

# Diving dataframe based on emotional & pleasant value in sorted order.
df_sad = df[:18000]
df_fear = df[18000:36000]
df_angry = df[36000:54000]
df_neutral = df[54000:72000]
df_happy = df[72000:]

# Task of function 'fun' is to take list of unique emotions & return dataframe of 30 rows.
def fun(list):

    # Creating Empty Dataframe
    data = pd.DataFrame()

    # If list of emotion's contain only 1 emotion
    if len(list) == 1:
        # Emotion name
        v = list[0]

        # Number of rows for this emotion
        t = 30

        if v == 'Neutral':
            # Adding rows to data
            data = data.append(df_neutral.sample(n=t))

        elif v == 'Angry':
            # Adding rows to data
            data = data.append(df_angry.sample(n=t))

        elif v == 'fear':
            # Adding rows to data
            data = data.append(df_fear.sample(n=t))

        elif v == 'happy':
            # Adding rows to data
            data = data.append(df_happy.sample(n=t))

        else:
            # Adding rows to data
            data = data.append(df_sad.sample(n=t))

    elif len(list) == 2:
        # Row's count per emotion
        times = [20,10]

        for i in range(len(list)):
            # Emotion name
            v = list[i]

            # Number of rows for this emotion
            t = times[i]

            if v == 'Neutral':
                # Adding rows to data
                data = data.append(df_neutral.sample(n=t))

            elif v == 'Angry':
                # Adding rows to data
                data = data.append(df_angry.sample(n=t))

            elif v == 'fear':
                # Adding rows to data
                data = data.append(df_fear.sample(n=t))

            elif v == 'happy':
                # Adding rows to data
                data = data.append(df_happy.sample(n=t))

            else:
                # Adding rows to data
                data = data.append(df_sad.sample(n=t))

    elif len(list) == 3:
        # Row's count per emotion
        times = [15,10,5]

        for i in range(len(list)):
            # Emotion name
            v = list[i]

            # Number of rows for this emotion
            t = times[i]

            if v == 'Neutral':
                # Adding rows to data
                data = data.append(df_neutral.sample(n=t))

            elif v == 'Angry':
                # Adding rows to data
                data = data.append(df_angry.sample(n=t))

            elif v == 'fear':
                # Adding rows to data
                data = data.append(df_fear.sample(n=t))

            elif v == 'happy':
                # Adding rows to data
                data = data.append(df_happy.sample(n=t))

            else:
                # Adding rows to data
                data = data.append(df_sad.sample(n=t))

    elif len(list) == 4:
        # Row's count per emotion
        times = [10,9,8,3]

        for i in range(len(list)):
            # Emotion name
            v = list[i]

            # Number of rows for this emotion
            t = times[i]

            if v == 'Neutral':
                # Adding rows to data
                data = data.append(df_neutral.sample(n=t))

            elif v == 'Angry':
                # Adding rows to data
                data = data.append(df_angry.sample(n=t))

            elif v == 'fear':
                # Adding rows to data
                data = data.append(df_fear.sample(n=t))

            elif v == 'happy':
                # Adding rows to data
                data = data.append(df_happy.sample(n=t))

            else:
                # Adding rows to data
                data = data.append(df_sad.sample(n=t))
    else:
        # Row's count per emotion
        times = [10,7,6,5,2]

        for i in range(len(list)):
            # Emotion name
            v = list[i]

            # Number of rows for this emotion
            t = times[i]

            if v == 'Neutral':
                # Adding rows to data
                data = data.append(df_neutral.sample(n=t))

            elif v == 'Angry':
                # Adding rows to data
                data = data.append(df_angry.sample(n=t))

            elif v == 'fear':
                # Adding rows to data
                data = data.append(df_fear.sample(n=t))

            elif v == 'happy':
                # Adding rows to data
                data = data.append(df_happy.sample(n=t))

            else:
                # Adding rows to data
                data = data.append(df_sad.sample(n=t))
    return data
