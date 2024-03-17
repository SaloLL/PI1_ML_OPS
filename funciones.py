# Import libraries
import pandas as pd


def get_available_genres(df_steam_games):
    """
    Returns a list of all available genres in the DataFrame.
    Parameters:
        - df_steam_games: DataFrame containing game data.
    Returns:
        - list: List of all available genres.
    """
    # Step 1: Split the 'Genres' column by ',' to separate multiple genres in a single entry
    genres_list = df_steam_games['Genres'].str.split(',')

    # Step 2: Create an empty set to store unique genres
    unique_genres = set()

    # Step 3: Iterate through each entry in the genres_list and add genres to the set
    for genres in genres_list:
        unique_genres.update(genres)

    # Step 4: Convert the set to a sorted list of unique genres
    all_genres = sorted(list(unique_genres))

    # Step 5: Return the list of all available genres
    return all_genres

def PlayTimeGenre(df_steam_games, user_items, genre):
    """
    Returns the year with the highest total play time for games of the specified genre.

    Parameters:
        - df_steam_games: DataFrame containing game data.
        - user_items: DataFrame containing user profiles and game ownership data.
        - genre: Genre to filter games.

    Returns:
        - int: Year with the highest total play time for the specified genre. If the genre is not found, returns None.
    """
    try:
        # Check if the provided genre exists in the list of available genres
        available_genres = get_available_genres(df_steam_games)
        if genre not in available_genres:
            print(f"The provided genre '{genre}' is not found in the list of available genres.")
            return None

        # Step 1: Filter games by genre
        filtered_games = df_steam_games[df_steam_games['Genres'].str.contains(genre, case=False)]

        # Step 2: Bring 'Release_Year' from df_steam_games and add it to the filtered DataFrame
        filtered_games = filtered_games.merge(df_steam_games[['Id', 'Release_Year']], on='Id', how='left')

        # Step 3: Group the IDs of games by release year
        grouped_games = filtered_games.groupby('Release_Year_x')['Id'].apply(list).reset_index(name='Game_IDs')

        # Step 4: For each row in grouped_games, sum the play time for users with the game ID
        for index, row in grouped_games.iterrows():
            game_ids = row['Game_IDs']
            # total_play_time = user_items[user_items['Item_Id'].isin(game_ids.tolist())]['Playtime_Forever'].sum()
            total_play_time = user_items[user_items['Item_Id'].isin(game_ids)]['Playtime_Forever'].sum()
            grouped_games.at[index, 'Total_Playtime'] = total_play_time
        # Step 5: Find the year with the highest total play time
        year_with_max_playtime = grouped_games.loc[grouped_games['Total_Playtime'].idxmax(), 'Release_Year_x']
        return int(year_with_max_playtime)

    except KeyError:
        # If a KeyError occurs, return None
        return None
