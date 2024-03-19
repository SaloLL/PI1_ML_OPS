# Import libraries
import pandas as pd
import numpy as np


def max_playtime_year(hours_per_year, genre):
    """
    Returns the year with the highest total playtime for the specified genre.

    Parameters:
        genre (str): The genre to search for.

    Returns:
        int or Str: The year with the highest total playtime for the genre, or a message if the genre is not found.
    """
    # Convert genre to lowercase for case-insensitive matching
    try:
        genre = genre.lower().strip()
        # Filter the dataframe to retain only rows with the specified genre
        genre_df = hours_per_year[hours_per_year['Genre'].str.lower() == genre]

        # Check if any rows are found for the genre
        if not genre_df.empty:
            # Find the year with the highest total playtime for the genre
            max_playtime_year = genre_df.loc[genre_df['Playtime_Forever'].idxmax(), 'Release_Year']
            return int(max_playtime_year)
        else:
            # Genre not found in the dataframe
            return f"Couldn't find the {genre} genre. Please check your input."
    except Exception as e:
        print("An error occurred while processing your request.")
        print(e)
        raise e
    
def max_player_time_per_genre(hours_per_year, player_maxtime_genre, genre):
    genre = genre.lower().strip()
    genre_df = hours_per_year[hours_per_year['Genre'].str.lower() == genre]
    try:
        if genre_df.empty:
            return f"Couldn't find the {genre} genre. Please check your input." 
        
        genre_filter = player_maxtime_genre.groupby(player_maxtime_genre['Posted_Year'])['Playtime_Forever'].sum().reset_index()
        maxtime_user = player_maxtime_genre.loc[player_maxtime_genre['Playtime_Forever'].idxmax()]['User_Id']
        response = {
            "User with most hours for " + genre: maxtime_user,
            "Hours played:": [{"Year": year, "Hours": hours} for year, hours in zip(genre_filter['Posted_Year'], genre_filter['Playtime_Forever'])]
        }

        return response
    
    except Exception as e:
        print("An error occurred while processing your request.")
        print(e)

        raise e