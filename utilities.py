import pandas as pd

players = pd.read_csv('data/players_raw_17_18.csv')
teams = pd.read_json('data/teams.json')['teams']
positions = pd.read_json('data/element_types.json')['element_types']
wanted_features = ['team_code', 'element_type', 'now_cost', 'total_points',
                   'minutes', 'value_season', 'goals_scored', 'assists', 'dreamteam_count', 'clean_sheets',
                   'goals_conceded', 'own_goals', 'penalties_saved', 'penalties_missed',
                   'yellow_cards', 'red_cards', 'saves', 'bonus', 'bps',
                   'influence', 'creativity', 'threat', 'ict_index', 'selected_by_percent'
                   ]


def import_data(file_name):
    return pd.read_csv(r'data/' + file_name)


# players id, data of given season, name of the column
def get_player_parameter(player, data, parameter):
    chosen_player = data[data['id'] == player]
    return chosen_player[parameter].values


def map_teams():
    team_list = []
    team_limit_list = []
    for team in teams:
        team_id = {team['code']: team['name']}
        team_limit_id = {team['name']: 3}

        team_list.append(team_id)
        team_limit_list.append(team_limit_id)

    team_dictionary = {}
    for team in team_list:
        team_dictionary.update(team)

    team_limit_dictionary = {}
    for team_limit in team_limit_list:
        team_limit_dictionary.update(team_limit)

    return team_dictionary, team_limit_dictionary


def map_positions():
    position_list = []
    for position in positions:
        position_id = {position['id']: position['plural_name_short']}
        position_list.append(position_id)

    position_dictionary = {}
    for position in position_list:
        position_dictionary.update(position)

    return position_dictionary


def get_players_data_frame():
    players_df = players
    players_df = players_df[wanted_features]
    return players_df


def get_players_data_frame_with_understandable_values(players_df, team_dictionary, position_dictionary):
    players_df = players_df.replace({'team_code': team_dictionary})
    players_df = players_df.replace({'element_type': position_dictionary})

    players_df = players_df.rename(columns={'team_code': 'team', 'element_type': 'position'})
    players_names = players['first_name'].str.cat(players['second_name'], sep=' ')
    players_df['player_name'] = players_names

    return players_df


def get_specific_data_frames(players_df):
    players_wanted_features = ['player_name', 'team', 'position', 'total_points', 'now_cost']
    most_points = players_df[players_wanted_features]
    most_points = most_points.sort_values(by='total_points', ascending=False)

    cheapest_players = players_df[players_wanted_features]
    cheapest_players = cheapest_players.sort_values(by='now_cost')

    value_players = players_df[players_wanted_features]
    value_players['value'] = value_players.apply(lambda row: row.total_points / row.now_cost, axis=1)
    value_players = value_players.sort_values(by='value', ascending=False)

    return most_points, cheapest_players, value_players
