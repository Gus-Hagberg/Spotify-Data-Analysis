#Edit of code
#----Modules----#
import pandas as pd
import matplotlib.pyplot as plt

#----Global Variables----#
quit = False

#----Setup dataframe and query it here prior to creating visualisation and UI functions----#
spotify_raw_data = pd.read_csv('spotify-2023.csv', on_bad_lines='warn', encoding='ISO-8859-1' )
# This prints all columns of the dataframe but only the bottom 10 and top 10 are printed
def showFullDataFrame():   
    with pd.option_context('display.max_rows', 40,
                       'display.max_columns', None,
                       'display.precision', 3,
                       ):
        print(spotify_raw_data)

#This function will compare song's danceability with the instrumentalness of the song
def danceabilityVSInstrumentallness():
    print("yo wsg")




def userOptions():
    global quit

    print("""Welcome to the spotify data analysis of 2023!
          
    Please select an option:
    1 - Show the full dataframe
    2 - Show a comparison between danceability and the instrumentalness of songs
    3 - Blank
    4 - Quit Program
        """)
    
    try:
        choice = int(input('Enter Selection: '))

        if choice == 1:
            showFullDataFrame()
        elif choice == 2:
            danceabilityVSInstrumentallness()
        #elif choice == 3:
        #    showCharts()
        elif choice == 4:
            quit = True
        else:
            print('A number between 1 and 4, come on!')

    except:
        print('Enter a number, it is not that hard.')

   

#----Main program----#
while not quit:
    userOptions()