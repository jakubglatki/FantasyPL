import utilities
import pandas as pd


def choose_players(chosen_team, row, position_limit_dictionary, team_limit_dictionary, squad, budget, season,
                   cheap_limit_dictionary=None):
    if cheap_limit_dictionary is None:
        cheap_limit_dictionary = {"GKP": 1, "DEF": 1, "MID": 1, "FWD": 1}
    chosen_team.append(row.player_name)
    budget -= row['now_cost_' + season]
    position_limit_dictionary[row.position] -= 1
    cheap_limit_dictionary[row.position] -= 1
    team_limit_dictionary[row.team] -= 1
    squad.append(row)
    return budget


def choose_team(most_points,
                cheapest_players,
                value_players, season):
    team_dictionary, team_limit_dictionary = utilities.map_teams()

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
            budget = choose_players(chosen_team, row, position_limit_dictionary, team_limit_dictionary, squad, budget,
                                    season)
            break

    for idx, row in cheapest_players.iterrows():
        if len(chosen_team) < bottom_performer_limit and \
                cheap_limit_dictionary[row.position] != 0 and team_limit_dictionary[row.team] != 0:
            budget = choose_players(chosen_team, row, position_limit_dictionary, team_limit_dictionary, squad, budget,
                                    season, cheap_limit_dictionary)
        elif len(chosen_team) == bottom_performer_limit:
            break

    for idx2, row2 in most_points.iterrows():
        if (budget - len(chosen_team) * 60 >= row2['now_cost_' + season] or len(chosen_team) <= 7) and \
                position_limit_dictionary[row2.position] != 0 and team_limit_dictionary[row2.team] != 0:
            budget = choose_players(chosen_team, row2, position_limit_dictionary, team_limit_dictionary, squad, budget,
                                    season)
        elif len(chosen_team) == 15:
            break

    for idx3, row3 in value_players.iterrows():
        if row3.player_name not in chosen_team and budget >= row3['now_cost_' + season] and \
                position_limit_dictionary[row3.position] != 0 and team_limit_dictionary[row3.team] != 0:
            budget = choose_players(chosen_team, row3, position_limit_dictionary, team_limit_dictionary, squad, budget,
                                    season)
        elif len(chosen_team) == 15:
            break

    total_points = 0

    players = utilities.import_data('players_' + season + '.csv')
    for row in squad:
        if row.position == 'GKP':
            gkp_squad.append(row.player_name)
        elif row.position == 'DEF':
            def_squad.append(row.player_name)
        elif row.position == 'MID':
            mid_squad.append(row.player_name)
        elif row.position == 'FWD':
            fwd_squad.append(row.player_name)
        for idx, rowPlayer in players.iterrows():
            if rowPlayer['second_name'] in row.player_name:
                if rowPlayer['now_cost_'+season] >= 45:
                    total_points += rowPlayer['total_points_' + season]

    print("Remaining Budget: " + str((budget / 10)) + "M")
    print("Total points: " + str(total_points))
    print(position_limit_dictionary)

    print('GKP: ' + str(gkp_squad))
    print('DEF: ' + str(def_squad))
    print('MID: ' + str(mid_squad))
    print('FWD: ' + str(fwd_squad))
    print('\n\n\n\n\n')
