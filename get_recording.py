import musicbrainzngs
import pandas as pd
import fuzzywuzzy as fuzz

from app import artist_name

musicbrainzngs.set_useragent(
    "python-musicbrainzngs", 
    "0.7.1", 
    "https://github.com/Garabella15"

)
# browsing the API to access recording of the artist

def browse_recordings(artist_id):
    limit =100
    offset = 0
    recordings =[]
    page = 1
    print("fetching page number %d.." % page)
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

    # selecting the title of songs where the artist is the primary artist 
        data = df[df['artist-credit-phrase'].str.startswith(artist_name)]

    # get the title of the songs
        Song_title = data ['title'].tolist()
        return Song_title
    