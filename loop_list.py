import requests
import json
from numpy import average


lists_of_title =['Santa Baby', 'One Last Time (Gazzo remix)', 'Only 1', 'Tribute and Cover Songs', 'Die in Your Arms', 
                'Tribute Songs', 'Clarity', 'imagine', 'Love Me Harder (Gregor Salto Amsterdam remix)', 
                "Break Up With Your Girlfriend, I'm Bored", 'Cadillac Song', 'Side to Side (DJ DSpin Ben remix)',
                'Breathin (Drew G dirty pop mix)', 'How I Look on You', 'Pink Champagne', 'side to side', 'Moonlight', 'Best Mistake'] 
                


total_words =[]
def get_lyrics():

    artist = 'Ariana Grande'
    url = 'https://api.lyrics.ovh/v1/{:}/{:}'
    for title in lists_of_title:
        if artist == 'Ariana Grande':
            lyrics_dict = requests.get(url.format(artist, title)).json()
            if lyrics_dict == None:
                print ("No lyrics found")
                pass
            
            lyrics=lyrics_dict.get('lyrics')
            songs= str(lyrics)
            words=len(songs.strip().split(" "))
        total_words.append(words)
        title += title

    print(average(total_words))

get_lyrics()