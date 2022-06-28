import requests
from numpy import average
import json

from app import fetch_lyrics_of_songs, artist_name

total_words =[]
artist = artist_name
def fetch_lyrics():
    artist = artist_name
    lists_of_title = fetch_lyrics_of_songs()
    for title in lists_of_title:

        try:
            url = "https://api.lyrics.ovh/v1/" + artist + "/" + title
        
            response = requests.get(url).json()
        except json.decoder.JSONDecodeError:
            print('')   
            if response == None or response == '':
                print("No lyrics found")
                pass
            else:
    
                lyrics = response.get("lyrics")
                total_words.append(lyrics)
        
        

fetch_lyrics()
total_words = " ".join(total_words)
print(average(len(total_words.split()))) 

fetch_lyrics()
# count_average_words_in_song()