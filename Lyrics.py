import requests
from numpy import average
import json

from app import fetch_lyrics_of_songs, artist_name

total_words =[]
def count_average_words_in_song():

    global artist_name
    lists_of_title = fetch_lyrics_of_songs()
    artist = artist_name
    url = 'https://api.lyrics.ovh/v1/{:}/{:}'
    for title in lists_of_title:
        if artist == artist_name:
            lyrics_dict = requests.get(url.format(artist, title)).json
            if lyrics_dict == None:
                print ("No lyrics found")
                pass

            lyrics = lyrics_dict.get('lyrics')
            songs = str(lyrics)
            words = len(songs.strip().split(" "))
        total_words.append(words)
        title += title

    print(average(total_words)) 

count_average_words_in_song()