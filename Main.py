from fastapi import FastAPI
import pandas as pd
from funciones import max_playtime_year

app = FastAPI()

# Load the DataFrames when the application starts
df_steam_games = pd.read_parquet('GZIP/df_steam_games.gzip')
df_user_revs = pd.read_parquet('GZIP/df_user_revs.gzip')
user_items = pd.read_parquet('GZIP/user_items.gzip')
hours_per_year = pd.read_parquet('GZIP/hours_per_year.gzip')

@app.get("/")
def home():
    return {"message": "Welcome to the Home Page"}

@app.get("/max_playtime_year/{genre}")
async def max_play_year(genre: str):
    """
    Returns the year with the highest total play time for games of the specified genre.
    Parameters:
        - genre: Genre to filter games.
    Returns:
        - int: Year with the highest total play time for the specified genre. If the genre is not found, returns None.
    """
    # Call the PlayTimeGenre function with the loaded DataFrames
    max_year = max_playtime_year(hours_per_year, genre)
    
    return max_year
