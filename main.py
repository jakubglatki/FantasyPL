# This is a sample Python script.
import pandas as pd
import numpy as np

import basic_method_ai
import utilities


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(utilities.get_player_parameter(234, utilities.import_data('players_raw_17_18.csv'), 'now_cost'))
    players = basic_method_ai.get_players_with_most_points()
    for index, player in players.iterrows():
        print(utilities.get_player_parameter(player['id'], players, 'web_name'))
    basic_method_ai.choose_team()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
