The source code is a simple CLI application which produces the average number of words in a songs given the name of the artist (e.g Snoop Dogg)
In implementing the application, inital research of the musicbraingnz website was performed to understand the musicbraingnz API, including the method, python package available to access the API, and the entity which stores data and their relationships.
the Various method used by the python_musicbraingnz API package includes, the GET, SEARCH AND BROWSE method.

the file app.py contains the function (search_artists) to retrieve the unique ID of the artist. this is parse into another function (browse_recording) the retrieve the title of the song. 

the file Lyrics.py contain a function to call the lyric.ovh API, it call the functions search_artist, browse_recording by importing from app.py

requriements.txt contains all the library/ package used for run the programming. 
