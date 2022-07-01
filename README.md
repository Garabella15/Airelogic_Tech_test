The source code is a simple CLI application which produces the average number of words in a songs given the name of the artist (e.g Snoop Dogg)
In implementing the application, inital research of the musicbraingnz website was performed to understand the musicbraingnz API, including the method, python package available to access the API, and the entity which stores data and their relationships.
the Various method used by the python_musicbraingnz API package includes, the GET, SEARCH AND BROWSE method.

the file app.py contains the function (search_artists) to retrieve the unique ID of the artist. this is parse into another function (browse_recording) the retrieve the title of the song. 

the file Lyrics.py contain a function to call the lyric.ovh API, it call the functions search_artist, browse_recording by importing from app.py

requriements.txt contains all the library/ package used for run the programming. 


Also, because of the large amount of data (titles of song) obtained through browse_recording function in the app.py, it takes time for the code to output the value of the desired variable (Mean). 

I was unable to clean all the data, this is because there are different versions of the same type of song which made it difficult to clean using the pandas package. However, I was able to remove duplicates title and null values. ( I shall continue working on the data as a way of improving my data cleaning skills. one idea will be to run a loop over the "list_of_title)