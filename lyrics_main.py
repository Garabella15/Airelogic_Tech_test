from pprint import pp
import requests
import json
from numpy import average


from app import fetch_lyrics_of_songs, artist_name              

# total_words =[]
total_lyrics = {}
def get_lyrics():
    artist ='Ariana Grande'
    lists_of_title = fetch_lyrics_of_songs()
    for title in lists_of_title:
​
        try:
            url = "https://api.lyrics.ovh/v1/" + artist + "/" + title
        
            response = requests.get(url).json()
            lyrics = response.get("lyrics")
            total_lyrics.update({title: lyrics})
        except json.decoder.JSONDecodeError:
            print('')   
            if response == None or response == '':
                print("No lyrics found")
                pass
        
get_lyrics()
count = 0
number = 1
for k,v in total_lyrics.items():
    if v == None or v == '':
        pass
    else:
        words = ''.join(v)   
        words = len(v.split())
        count += words        
    number += 1

    print(count)