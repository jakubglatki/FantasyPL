import utilities
import json
import pandas as pd

players = utilities.import_data('players_raw_17_18.csv')
budget = 1000


def get_players_with_most_points():
    players_list = pd.DataFrame()
    players_copy = players.sort_values('total_points', ascending=False)
    index = 0
    while index < 15:
        player_to_add = pd.DataFrame(players_copy.iloc[[index]])
        players_list = pd.concat([players_list, player_to_add])
        index += 1
    return players_list


def make_team():
    players_list = pd.DataFrame()
    players_with_most_points = players.sort_values('total_points', ascending=False)


teams = pd.read_json('data/teams.json')['teams']
positions = pd.read_json('data/element_types.json')['element_types']

test_df = players

##################################
# mapping team

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

# mapping position
position_list = []
for position in positions:
    position_id = {position['id']: position['plural_name_short']}
    position_list.append(position_id)

position_dictionary = {}
for position in position_list:
    position_dictionary.update(position)

##################################


##################################
# Filter data and preparing dataframe
wanted_features = ['first_name', 'second_name', 'team_code', 'element_type', 'news', 'now_cost', 'total_points',
                   'minutes',
                   'form', 'value_season', 'points_per_game', 'value_form',
                   'goals_scored', 'assists', 'dreamteam_count', 'clean_sheets',
                   'goals_conceded', 'own_goals', 'penalties_saved', 'penalties_missed',
                   'yellow_cards', 'red_cards', 'saves', 'bonus',
                   'influence', 'creativity', 'threat', 'ict_index', 'selected_by_percent'
                   ]

# Converting the list of players to a DataFrame
players_df = players
# Choosing only the columns that we want
players_df = players_df[wanted_features]

players_df = players_df.replace({'team_code': team_dictionary})
players_df = players_df.replace({'element_type': position_dictionary})

players_df = players_df.rename(columns={'team_code': 'team', 'element_type': 'position'})

players_df['player_name'] = players_df['first_name'].str.cat(players_df['second_name'], sep=' ')
players_df = players_df.drop(['first_name', 'second_name'], axis=1)


def unavialable(row):
    if row['news'] != '':
        return True
    else:
        return False


players_df['unavailable'] = players_df.apply(lambda row: unavialable(row), axis=1)

players_df = players_df[['player_name', 'team', 'position', 'unavailable', 'now_cost', 'total_points', 'minutes',
                         'form', 'value_season', 'points_per_game', 'value_form',
                         'goals_scored', 'assists', 'dreamteam_count', 'clean_sheets',
                         'goals_conceded', 'own_goals', 'penalties_saved', 'penalties_missed',
                         'yellow_cards', 'red_cards', 'saves', 'bonus',
                         'influence', 'creativity', 'threat', 'ict_index', 'selected_by_percent'
                         ]]

##################################

players_wanted_features = ['player_name', 'team', 'position', 'total_points', 'now_cost', 'unavailable']
most_points = players_df[players_wanted_features]
most_points = most_points.sort_values(by='total_points', ascending=False)

cheapest_players = players_df[players_wanted_features]
cheapest_players = cheapest_players.sort_values(by='now_cost')

value_players = players_df[players_wanted_features]
value_players['value'] = value_players.apply(lambda row: row.total_points / row.now_cost, axis=1)
value_players = value_players.sort_values(by='value', ascending=False)

##################################


def choose_players(value_team, row, position_limit_dictionary, squad, cheap_limit_dictionary=None):
    if cheap_limit_dictionary is None:
        cheap_limit_dictionary = {"GKP": 1, "DEF": 1, "MID": 1, "FWD": 1}
    global budget
    value_team.append(row.player_name)
    budget -= row.now_cost
    position_limit_dictionary[row.position] -= 1
    cheap_limit_dictionary[row.position] -= 1
    team_limit_dictionary[row.team] -= 1
    squad.append(row)


def choose_team():
    value_team = []
    squad = []

    gkp_squad = []
    def_squad = []
    mid_squad = []
    fwd_squad = []

    top_performer_limit = 7
    bottom_performer_limit = 3
    position_limit_dictionary = {"GKP": 2, "DEF": 5, "MID": 5, "FWD": 3}
    cheap_limit_dictionary = {"GKP": 0, "DEF": 2, "MID": 2, "FWD": 2}

    for idx, row in cheapest_players.iterrows():
        if row.position == "GKP":
            choose_players(value_team, row, position_limit_dictionary, squad)
            break

    for idx, row in cheapest_players.iterrows():
        if budget >= row.now_cost and len(value_team) < bottom_performer_limit and \
                cheap_limit_dictionary[row.position] != 0 and team_limit_dictionary[row.team] != 0:
            choose_players(value_team, row, position_limit_dictionary, squad, cheap_limit_dictionary)

    for idx, row in most_points.iterrows():
        if budget >= row.now_cost and len(value_team) < top_performer_limit and \
                position_limit_dictionary[row.position] != 0 and team_limit_dictionary[row.team] != 0:
            choose_players(value_team, row, position_limit_dictionary, squad)
        else:
            for idx2, row2 in value_players.iterrows():
                if row2.player_name not in value_team and budget >= row2.now_cost and \
                        position_limit_dictionary[row2.position] != 0 and team_limit_dictionary[row2.team] != 0:
                    choose_players(value_team, row2, position_limit_dictionary, squad)

    for row in squad:
        if row.position == 'GKP':
            gkp_squad.append(row.player_name)
        elif row.position == 'DEF':
            def_squad.append(row.player_name)
        elif row.position == 'MID':
            mid_squad.append(row.player_name)
        elif row.position == 'FWD':
            fwd_squad.append(row.player_name)

    print("Remaining Budget: " + str((budget / 10)) + "M")
    print(position_limit_dictionary)

    print('GKP: ' + str(gkp_squad))
    print('DEF: ' + str(def_squad))
    print('MID: ' + str(mid_squad))
    print('FWD: ' + str(fwd_squad))

# choose_team()
