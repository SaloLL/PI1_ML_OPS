# Import libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import NearestNeighbors


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
    
def recommend_games_for_user(df_reviews,User_Id):
    # Transform the DataFrame into a matrix of users and games
    user_item_matrix = pd.pivot_table(df_reviews, values='Sentiment_Score', index='User_Id', columns='App_Name', fill_value=0)
    
    # Split the data into training and test sets
    train_data, test_data = train_test_split(user_item_matrix, test_size=0.2, random_state=42)
    
    # Train a nearest neighbors model (KNN)
    model_knn = NearestNeighbors(metric='cosine', algorithm='brute')
    model_knn.fit(train_data.values)
    
    # Try to find the index of the user
    try:
        user_index = train_data.index.get_loc(User_Id)
    except KeyError:
        return "User name not found."
    
    # Find the nearest neighbors to the selected user
    distances, indices = model_knn.kneighbors(train_data.iloc[user_index, :].values.reshape(1, -1), n_neighbors=6)
    
    # Make recommendations based on the nearest neighbors (excluding the first neighbor, which is the user itself)
    recommended_games = set()  # Set to keep track of recommended games
    for i in range(1, len(distances.flatten())):
        similar_user_index = indices.flatten()[i]
        similar_user_id = train_data.index[similar_user_index]  # Get the User_Id of the similar user
        similar_user_games = df_reviews[df_reviews['User_Id'] == similar_user_id]['App_Name']  # Get the games of the similar user
        for game in similar_user_games:
            if len(recommended_games) < 5 and game not in recommended_games:  # Check if more games are needed and if the game has not been recommended before
                recommended_games.add(game)  # Add the game to the set of recommended games
        if len(recommended_games) >= 5:  # Exit the loop if 5 games have already been recommended
            break
    message = f"Recomendations for {User_Id}: {recommended_games}"
    return message
        