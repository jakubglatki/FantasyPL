import utilities
import numpy as np
import pandas as pd

players = utilities.import_data('players_raw_17_18.csv')


def get_players_with_most_points():
    players_list = pd.DataFrame()
    players_copy = players.sort_values('total_points', ascending=False)
    index = 0
    while index < 11:
        player_to_add = pd.DataFrame(players_copy.iloc[[index]])
        players_list = pd.concat([players_list, player_to_add])
        index += 1
    return players_list
