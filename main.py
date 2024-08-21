#Edit of code
#----Modules----#
import pandas as pd
import matplotlib.pyplot as plt

#----Global Variables----#
quit = False

#----Setup dataframe and query it here prior to creating visualisation and UI functions----#
spotify_raw_data = pd.read_csv('data/spotify-2023.csv', 

on_bad_lines='warn' )

def showFullDataset():
    print(spotify_raw_data)






def userOptions():
    global quit

    print("""Welcome to the spotify data analysis of 2023!
          
    Please select an option:
    1 - Show full original dataset
    2 - Blank
    3 - Blank
    4 - Quit Program
        """)
    
    try:
        choice = int(input('Enter Selection: '))

        if choice == 1:
            showFullDataset()
        #elif choice == 2:
        #    showUpdatedData()
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