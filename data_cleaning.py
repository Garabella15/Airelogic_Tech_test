import pandas as pd
import fuzzywuzzy as fuzz
from get_recording import browse_recordings

def Cleaning_data():
    data = browse_recordings(artist_id, artist_name)
    df = pd.DataFrame(data)
    print(df)

