#Edit of code
#----Modules----#
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pandasForSortingCSV
from IPython.display import display

#----Global Variables----#
quit = False

#----Setup dataframe and query it here prior to creating visualisation and UI functions----#
spotify_raw_data = pd.read_csv('spotify-2023.csv', on_bad_lines='warn', encoding='ISO-8859-1' )
# This prints all columns of the dataframe as well as the top 100 
def showFullDataFrame():
      with pd.option_context('display.max_rows', None,
                       'display.max_columns', None,
                       'display.precision', 3,
                       ):
        display(spotify_raw_data.head(100))
  

#This function will compare song's danceability% with the instrumentalness of the song
def danceabilityVSInstrumentallness(data):
    # Select relevant columns: track_name, danceability_%, instrumentalness_%, and energy_%
    columns_of_interest = ['track_name', 'danceability_%', 'instrumentalness_%', 'energy_%']
    filtered_data = data[columns_of_interest]
    
    # Sort the data by danceability in descending order
    sorted_data = filtered_data.sort_values(by='danceability_%', ascending=False)
    
    # Display only the top 100 records
    top_100_data = sorted_data.head(150)
    
    # Display the sorted top 100 DataFrame
    with pd.option_context('display.max_rows', None,
                       'display.max_columns', None,
                       'display.width', 1000,
                       'display.precision', 3,
                       'display.colheader_justify', 'left'):
        display(top_100_data)
  
    

#This function compares songs energy% to bpm of the song
# Defining
def energyVSBPM(data):
    # Selecting song name, energy% and bpm columns
    selected_data = data[['track_name', 'energy_%', 'bpm']]

    # Sorting the data by energy percentage in descending order
    sorted_data = selected_data.sort_values(by='energy_%', ascending=False)
    top_100_tracks = sorted_data.head(100)
    bottom_100_tracks = sorted_data.tail(100)
    # This lets there be no limit for how many rows the dataframe can print instead of getting truncated (shortened with only the first and last results)
    with pd.option_context('display.max_rows', None,
                       'display.max_columns', None,
                       'display.precision', 3,
                       ):
        display(top_100_tracks)
        display(bottom_100_tracks)

#This function is a calculator for different statistics from this dataset
def mMM():
    # Columns in the dataset
    columns = ['artist_count', 'released_year', 'released_month', 'released_day', 
               'in_spotify_playlists', 'in_spotify_charts', 'streams', 'in_apple_playlists', 
               'in_apple_charts', 'in_deezer_playlists', 'in_deezer_charts', 'in_shazam_charts', 
               'bpm', 'danceability_%', 'valence_%', 'energy_%', 'acousticness_%', 
               'instrumentalness_%', 'liveness_%', 'speechiness_%']

    try:
        # Ask user to select a category
        column_choice = int(input("""Welcome to the Spotify data calculator!
                                  Please choose a category:
                  1  - artist count
                  2  - released year
                  3  - released month
                  4  - released day
                  5  - amount in spotify playlists
                  6  - in spotify charts
                  7  - streams
                  8  - in apple playlists
                  9  - in apple charts
                  10 - in deezer playlists
                  11 - in deezer charts
                  12 - in shazam charts
                  13 - bpm
                  14 - danceability
                  15 - valence
                  16 - energy
                  17 - acousticness
                  18 - instrumentalness
                  19 - liveliness
                  20 - speechiness
                                   """))
        
        if column_choice < 1 or column_choice > 20:
            return "Invalid column choice. Please choose a number between 1 and 20."
        
        selected_col = columns[column_choice - 1]
        data = pd.to_numeric(spotify_raw_data[selected_col], errors='coerce').dropna()

        # Ask user to select a calculation
        calc_choice = int(input("""Please enter a number
                  1 - mean
                  2 - median
                  3 - mode 
                                """))
        
        if calc_choice == 1:
            result = data.mean()
            result_type = "mean"
        elif calc_choice == 2:
            result = data.median()
            result_type = "median"
        elif calc_choice == 3:
            result = data.mode()[0]  # Mode can return multiple values, take the first
            result_type = "mode"
        else:
            return "Please choose between 1 (mean), 2 (median), or 3 (mode)."

        # Finding the closest matching track name based on the result
        closest_track_index = (data - result).abs().idxmin()
        closest_track = spotify_raw_data.loc[closest_track_index, 'track_name']
    
        # Display the result
        return f"The {result_type} of '{selected_col}' is: {result}\nThe closest track to this value is: {closest_track}"
    
    except ValueError:
        return "Please enter a valid number."
    except KeyError:
        return "Column not found in the dataset."

def userOptions():
    global quit

    print("""Welcome to the spotify data analysis of 2023!
          
    Please select an option:
    1 - Show the full dataframe
    2 - Show a comparison between danceability, instrumentalness, and energy of the songs.
    3 - Show a comparison between energy and BPM of the songs.
    4 - Use the statistic calculator
    5 - Quit Program
        """)
    
    try:
        choice = int(input('Enter Selection: '))

        if choice == 1:
            showFullDataFrame()
        elif choice == 2:
            danceabilityVSInstrumentallness(spotify_raw_data)
        elif choice == 3:
            energyVSBPM(spotify_raw_data)
        elif choice == 4:
            print(mMM())
        elif choice == 5:
            quit = True
        else:
            print('A number between 1 and 4, come on!')

    except:
        print('Enter a number, it is not that hard.')

   

#----Main program----#
while not quit:
    userOptions()