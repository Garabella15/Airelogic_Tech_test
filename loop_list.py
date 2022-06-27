from pprint import pp
import requests
import json
from numpy import average


lists_of_title =['Santa Baby', 'One Last Time (Gazzo remix)', 'Only 1', 'Tribute and Cover Songs', 'Die in Your Arms', 
                'Tribute Songs', 'Clarity', 'imagine', 'Love Me Harder (Gregor Salto Amsterdam remix)', 
                "Break Up With Your Girlfriend, I'm Bored", 'Cadillac Song', 'Side to Side (DJ DSpin Ben remix)',
                'Breathin (Drew G dirty pop mix)', 'How I Look on You', 'Pink Champagne', 'side to side', 'Moonlight', 'Best Mistake'] 
                


total_words =[]
total_lyrics = {}
def get_lyrics():
    artist ='Ariana Grande'
    # lists_of_title = fetch_lyrics_of_songs()
    for title in lists_of_title:

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
for lyrics in total_lyrics.values():
    words = len(lyrics.split(" "))

    count += words
print(count)
# songs = total_words[0]
# songs = songs.strip('\n')
# print(len(songs.split(" ")))
# total_words = " ".join(total_words)
# print(average(len(total_words.split()))) 


# total_words =[]
# def get_lyrics():
#     global artist_name
#     lists_of_title = count_total_words_in_songs()
#     artist = 'Ariana Grande'
#     url = 'https://api.lyrics.ovh/v1/{:}/{:}'
#     for title in lists_of_title:
#         if artist == artist_name:
#             lyrics_dict = requests.get(url.format(artist, title)).json
#             if lyrics_dict == None:
#                 print (" No lyrics found")
#                 pass
            
#             lyrics=lyrics_dict.get('lyrics')
#             songs= str(lyrics)
#             words=len(songs.strip().split(" "))
#         total_words.append(words)

#     print(average(total_words))