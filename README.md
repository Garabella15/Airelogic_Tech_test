The source code is a simple CLI application which produces the average number of words in a songs given the name of the artist (e.g Snoop Dogg)
In implementing the application, inital research of the musicbraingnz website was performed to understand the musicbraingnz API, including the method, python package available to access the API, and the entity which stores data and their relationships.
the Various method used by the python_musicbraingnz API package includes, the GET, SEARCH AND BROWSE method.

the file app.py contains the code to retrieve the title of the song, this is done using the search_artists method, the ouput is the artist_id (unique). the artist_id becomes input parameter to the Browse_recording method.
the browse_recording method allow for accessing titles of the songs 