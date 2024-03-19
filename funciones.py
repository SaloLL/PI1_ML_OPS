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
            max_playtime_year = int(max_playtime_year)
            return f"Release year with most playtime for {genre} : {max_playtime_year}"
        else:
            # Genre not found in the dataframe
            return f"Couldn't find the {genre} genre. Please check your input."
    except Exception as e:
        print("An error occurred while processing your request.")
        print(e)
        raise e
    
def max_player_time_per_genre(hours_per_year, player_maxtime_genre, genre):
    # Convert the genre input to lowercase and remove leading/trailing whitespace
    genre = genre.lower().strip()
    
    # Filter the dataframe to include only rows with the specified genre
    genre_df = hours_per_year[hours_per_year['Genre'].str.lower() == genre]
    
    try:
        # Check if any rows are found for the genre
        if genre_df.empty:
            # Return an error message if no rows are found
            return f"Couldn't find the {genre} genre. Please check your input." 
        
        # Group the player_maxtime_genre dataframe by 'Posted_Year' and sum the playtime
        genre_filter = player_maxtime_genre.groupby(player_maxtime_genre['Posted_Year'])['Playtime_Forever'].sum().reset_index()
        
        # Find the user with the maximum playtime for the genre
        maxtime_user = player_maxtime_genre.loc[player_maxtime_genre['Playtime_Forever'].idxmax()]['User_Id']
        
        # Construct the response dictionary containing the user ID and hours played per year
        response = {
            "User with most hours for " + genre: maxtime_user,
            "Hours played:": [{"Year": year, "Hours": hours} for year, hours in zip(genre_filter['Posted_Year'], genre_filter['Playtime_Forever'])]
        }

        # Return the response
        return response
    
    except Exception as e:
        # Handle any exceptions that occur during processing
        print("An error occurred while processing your request.")
        print(e)

        # Raise the exception
        raise e