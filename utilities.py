import pandas as pd


def import_data(file_name):
    return pd.read_csv(r'data/' + file_name)


# players id, data of given season, name of the column
def get_player_parameter(player, data, parameter):
    chosen_player = data[data['id'] == player]
    return chosen_player[parameter].values
