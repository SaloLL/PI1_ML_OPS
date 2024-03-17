from fastapi import FastAPI
import pandas as pd
from funciones import PlayTimeGenre

app=FastAPI()

# Load the DataFrames when the application starts
df_steam_games = pd.read_parquet('GZIP/df_steam_games.gzip')
df_user_revs = pd.read_parquet('GZIP/df_user_revs.gzip')
user_items = pd.read_parquet('GZIP/user_items.gzip')


@app.get("/")
def home():
    return {"message": "Welcome to the Home Page"}

@app.get("/play_time/{genre}")
async def get_play_time_by_genre(genre: str):
    """
    Returns the total play time for each user for games of the specified genre.

    Parameters:
        - genre: Genre to filter games.

    Returns:
        - dict: Dictionary containing user IDs as keys and total play time as values.
    """
    # Call the PlayTimeGenre function with the loaded DataFrames
    play_time_by_user = PlayTimeGenre(df_steam_games, user_items, genre)
    
    return play_time_by_user

