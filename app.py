import musicbrainzngs
import pandas as pd
import requests
import json
from fuzzywuzzy import fuzz


# setup the user_agent with to enable access to musicbrainzngs database
musicbrainzngs.set_useragent(
    "python-musicbrainzngs", 
    "0.7.1", 
    "https://github.com/Garabella15"

)

# enter name of artists

artist_name = str(input('Enter a name:'))

#searching the artist using the search method and output the artist_id

def search_artists(artist_name):
    result = musicbrainzngs.search_artists(artist=artist_name, strict=True)
    # print(result)
    for artist in result['artist-list']:
            if artist['name'] == artist_name:
                artist_id= artist.get('id')
                return artist_id

# browsing the database for recording specific to the artist (artist_id is used as key)

def browse_recordings(artist_id):
    global artist_name
    limit =100
    offset = 0
    recordings =[]
    page = 1
    # print("fetching page number %d.." % page)
    result = musicbrainzngs.browse_recordings(artist=artist_id, 
                        includes=["artist-credits"], limit=limit, offset=offset)
    # print(result)

    page_recording = result['recording-list']
    recordings += page_recording

    if "recording-count" in result:
            count = result['recording-count']
            print("")
    while len(page_recording) >= limit:
        offset += limit
        page += 1
        # print("fetching page number %d.." % page)
        result = musicbrainzngs.browse_recordings(artist=artist_id, 
                        includes=["artist-credits"], limit=limit, offset=offset)
        # print(result)
        page_recording = result['recording-list']
        recordings += page_recording
        # return recordings

    # cleaning data using pandas package, this to removing redundant data
        df = pd.DataFrame(recordings)

    # selecting the title of songs where the named artist is the primary artist 
        data = df[df['artist-credit-phrase'].str.startswith(artist_name)]

    # get the title of the songs
        Song_title = data ['title'].tolist()
    
    # sorted the data to remove reductant title in the data
        title_of_song = set(Song_title)

# fuzzywuzzy package is used to remove reductant title of songs

    elements = list(title_of_song)

    results = [[title, [], 0] for title in elements]

    for (i, element) in enumerate(elements):
        for (j, choice) in enumerate(elements[i+1:]):
            if fuzz.ratio(element, choice) >= 90:
                results[i][2] += 1
                results[i][1].append(choice)
                results[j+i+1][2] += 1
                results[j+i+1][1].append(element)

    clean_data = pd.DataFrame(results, columns=['title', 'duplicates', 'duplicate_count'])
    Song_title = clean_data['title']
    lists_of_titles = list(Song_title)
    return lists_of_titles




def fetch_lyrics_of_songs():
    global artist_name
    artist_id = search_artists(artist_name)
    lists_of_title = browse_recordings(artist_id)
    return lists_of_title

fetch_lyrics_of_songs()
    