# Import libraries
import pandas as pd
import numpy as np

def max_playtime_year(hours_per_year, genre):
    """
    Returns the year with the highest total play time for games of the specified genre.
    Parameters:
        - hours_per_year: DataFrame containing total playtime per year and genre.
        - genre: Genre to filter games.
    Returns:
        - int: Year with the highest total play time for the specified genre. If the genre is not found, returns None.
    """
    try:
        genre = genre.lower()
        # Initialize an empty list to store unique genres
        unique_genres = []

        # Loop through each entry in the 'Genres' column
        for genres_entry in hours_per_year['Genres']:
            # Split the entry by comma and strip any leading or trailing spaces
            genres_list = [genre.strip() for genre in genres_entry.split(',')]
    
            # Add each genre from the entry to the list of unique genres
            for genre in genres_list:
                if genre not in unique_genres:
                    unique_genres.append(genre)
        # Now unique_genres contains a list of unique genres
                    
        print(unique_genres)
        if genre not in unique_genres:
            return f"Can't find the genre that you're looking for..."
        # Filter the DataFrame by the specified genre
        filtered_data = hours_per_year[hours_per_year['Genres'].str.contains(genre, case=False)]
        # Find the year with the highest total play time
        max_playtime_year = filtered_data.loc[filtered_data['Total_Playtime'].idxmax(), 'Release_Year']
        return int(max_playtime_year)
    except Exception as e:
        # If a KeyError occurs, return None
        print(e)
        return e
