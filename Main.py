from fastapi import FastAPI
import pandas as pd
from funciones import max_playtime_year
from funciones import max_player_time_per_genre

app = FastAPI()

# Load the DataFrames when the application starts
player_maxtime_genre = pd.read_parquet('GZIP/max_playtime_user_genre.gzip')
hours_per_year = pd.read_parquet('GZIP/max_hours_per_year.gzip')


@app.get("/")
def home():
    return {"message": "Welcome to the Home Page"}

@app.get("/max_playtime_year/{genre}")
async def max_play_time_year(genre: str):
    """
    Returns the year with the highest total play time for games of the specified genre.
    Parameters:
        - genre: Genre to filter games.
    Returns:
        - int: Year with the highest total play time for the specified genre. If the genre is not found, returns a message.
    """
    # Call the PlayTimeGenre function with the loaded DataFrames
    max_year = max_playtime_year(hours_per_year, genre)

    return f"Release year with most playtime for {genre} : {max_year}"

@app.get("/user_for_genre/{genre}")
async def  user_by_game_genre(genre: str):
    """
    Returns the player with the highest total play time for games of the specified genre.
    Parameters:
        - genre: Genre to filter games.
    Returns:
        - int: Year with the highest total play time for the specified genre. If the genre is not found, returns a message.
    """
    user_max_time = max_player_time_per_genre(hours_per_year, player_maxtime_genre, genre)
    
    return user_max_time
