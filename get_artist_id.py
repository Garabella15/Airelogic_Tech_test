import musicbrainzngs


musicbrainzngs.set_useragent(
    "python-musicbrainzngs", 
    "0.7.1", 
    "https://github.com/Garabella15"

)
artist_name = str(input('Enter a Name: '))
def search_artists():
    global artist_name
    result = musicbrainzngs.search_artists(artist=artist_name, strict=True)
    # print(result)
    for artist in result['artist-list']:
            if artist['name'] == artist_name:
                artist_id= artist.get('id')
                print(artist_id) 

search_artists()


