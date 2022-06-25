from urllib import response
import requests
import json

def get_lyrics():
# specify Vairables
    artist = 'Ariana Grande'
    Song_title = '34+35'
    url = 'https://api.lyrics.ovh/v1/'+ artist + '/' + Song_title

    # fetching lyrics
    #def fetch_lyrics_of_song(response):
    response = requests.get(url)
    json_data=json.loads(response.content)
    lyrics = json_data['lyrics']

    print(len(lyrics.strip().split(" ")))

get_lyrics()