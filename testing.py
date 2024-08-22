import pandas as pd
import matplotlib.pyplot as plt

spotify_raw_data = pd.read_csv('spotify-2023.csv', on_bad_lines='warn', encoding='ISO-8859-1' )
with pd.option_context('display.max_rows', None,
                       'display.max_columns', None,
                       'display.width', None,
                       'display.precision', 3,
                       'display.colheader_justify', 'left'):
    print(spotify_raw_data)