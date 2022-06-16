import basic_method_self_made
import utilities
import pandas as pd

players = utilities.import_data('players_raw_17_18.csv')

team_dictionary, team_limit_dictionary = utilities.map_teams()
position_dictionary = utilities.map_positions()

players_df = utilities.get_players_data_frame()
players_df = utilities.get_players_data_frame_with_understandable_values(players_df, team_dictionary,
                                                                         position_dictionary)
most_points, cheapest_players, value_players = utilities.get_specific_data_frames(players_df)


def get_players_with_most_points():
    players_list = pd.DataFrame()
    players_copy = players.sort_values('total_points', ascending=False)
    index = 0
    while index < 15:
        player_to_add = pd.DataFrame(players_copy.iloc[[index]])
        players_list = pd.concat([players_list, player_to_add])
        index += 1
    return players_list


def choose_players(chosen_team, row, position_limit_dictionary, squad, budget, cheap_limit_dictionary=None):
    if cheap_limit_dictionary is None:
        cheap_limit_dictionary = {"GKP": 1, "DEF": 1, "MID": 1, "FWD": 1}
    chosen_team.append(row.player_name)
    budget -= row.now_cost
    position_limit_dictionary[row.position] -= 1
    cheap_limit_dictionary[row.position] -= 1
    team_limit_dictionary[row.team] -= 1
    squad.append(row)
    return budget


def choose_team(most_points=basic_method_self_made.most_points,
                cheapest_players=basic_method_self_made.cheapest_players,
                value_players=basic_method_self_made.value_players):
    budget = 1000
    chosen_team = []
    squad = []

    gkp_squad = []
    def_squad = []
    mid_squad = []
    fwd_squad = []

    bottom_performer_limit = 4
    position_limit_dictionary = {"GKP": 2, "DEF": 5, "MID": 5, "FWD": 3}
    cheap_limit_dictionary = {"GKP": 0, "DEF": 2, "MID": 2, "FWD": 2}

    for idx, row in cheapest_players.iterrows():
        if row.position == "GKP":
            budget = choose_players(chosen_team, row, position_limit_dictionary, squad, budget)
            break

    for idx, row in cheapest_players.iterrows():
        if len(chosen_team) < bottom_performer_limit and \
                cheap_limit_dictionary[row.position] != 0 and team_limit_dictionary[row.team] != 0:
            budget = choose_players(chosen_team, row, position_limit_dictionary, squad, budget, cheap_limit_dictionary)
        elif len(chosen_team) == bottom_performer_limit:
            break

    for idx2, row2 in most_points.iterrows():
        if (budget - len(chosen_team) * 60 >= row2.now_cost or len(chosen_team) <= 7) and \
                position_limit_dictionary[row2.position] != 0 and team_limit_dictionary[row2.team] != 0:
            budget = choose_players(chosen_team, row2, position_limit_dictionary, squad, budget)
        elif len(chosen_team) == 15:
            break

    for idx3, row3 in value_players.iterrows():
        if row3.player_name not in chosen_team and budget >= row3.now_cost and \
                position_limit_dictionary[row3.position] != 0 and team_limit_dictionary[row3.team] != 0:
            budget = choose_players(chosen_team, row3, position_limit_dictionary, squad, budget)
        elif len(chosen_team) == 15:
            break

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
