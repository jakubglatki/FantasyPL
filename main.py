import pandas as pd
from matplotlib import pyplot
import glob
import os

import Gameweeks_data_manipulation
import basic_method_self_made
import compare_classes
import utilities

from AI.AIPrediction import AIPrediction
from AI.DecisionTree import DecisionTree
from AI.KNN import KNN
from AI.LinearRegressionAI import LinearRegressionAI
from AI.RandomForest import RandomForest
from AI.TabNet import TabNet
from AI.XGBoost import XGBoost

if __name__ == '__main__':

    #Gameweeks_data_manipulation.add_gameweeks_data(1, 1, '21_22')
    #compare_classes.compare_models()
    # os.chdir(r'data/17_18')
    # allFiles = glob.glob("*.csv")  # match your csvs
    # for file in allFiles:
    #     df = pd.read_csv(file, encoding="ISO-8859-1")
    #     try:
    #         df = df.drop_duplicates('name', keep='last')  # read from row 34 onwards.
    #         df.to_csv(file, index=False)
    #     finally:
    #         continue

    # df = pd.read_csv('data/17_18/players_gws.csv', encoding="ISO-8859-1")
    # print(df)
    # df = df.drop_duplicates(['first_name', 'second_name'], keep='last')  # read from row 34 onwards.
    # df.to_csv(r'data/17_18/players_gws.csv', index=False)
    # utilities.check_all_algorithms('21_22')
    # players = pd.read_csv('data/players_22_23.csv' , encoding="ISO-8859-1")
    # players2 = pd.read_csv('data/players_23_24.csv', encoding="ISO-8859-1")
    # players = players.merge(players2, left_on=['first_name', 'second_name'],
    #                         right_on=['first_name_23_24', 'second_name_23_24'],
    #                         how='right')
    # players = players.drop(labels=['first_name', 'second_name'], axis=1)
    # players = players.rename(columns={'first_name_23_24': 'first_name', 'second_name_23_24': 'second_name'})
    # players.to_csv('data/players_23_24.csv', index=False)
    # players = pd.read_csv('data/players_21_22.csv')
    # players = pd.read_csv('data/players_16_17.csv')
    # players2 = pd.read_csv('data/gw1_16_17.csv')
    # players = players.merge(players2, left_on=['first_name', 'second_name'],
    #                         right_on=['first_name_21_22', 'second_name_21_22'],
    #                         how='right')
    # players = players.drop(labels=['first_name', 'second_name'], axis=1)
    # players = players.rename(columns={'first_name_21_22': 'first_name', 'second_name_21_22': 'second_name'})
    # players.to_csv('data/players_21_22.csv', index=False)
    # players = pd.read_csv('data/players_23_24.csv')
    #
    # wanted_features = utilities.wanted_features
    # column_list = []
    # for feature in wanted_features:
    #     for column in players.columns:
    #         if feature in column:
    #             column_list.append(column)
    # players = players[column_list]
    # players = players.add_suffix('_23_24')
    # players.to_csv('data/players_23_24.csv', index=False)
    # players= pd.read_csv('data/21_22/players_gws.csv', encoding="ISO-8859-1")
    # team_dictionary, team_limit_dictionary = utilities.map_teams()
    # position_dictionary = utilities.map_positions()
    #
    # players_predicted_df = utilities.get_players_data_frame_with_understandable_values(players,
    #                                                                                    team_dictionary,
    #                                                                                    position_dictionary,
    #                                                                                    '20_21')
    # most_points, cheapest_players, value_players = utilities.get_specific_data_frames(players_predicted_df,
    #                                                                                   '20_21')
    # basic_method_self_made.choose_team(most_points, cheapest_players, value_players, '20_21')
    # #ai = AIPrediction()
    #
#    Gameweeks_data_manipulation.add_gameweeks_data(1, 1, '22_23')
    xgboost = XGBoost('23_24')
    predicted_points = xgboost.train_model()
    xgboost.choose_team_with_predicted_points(predicted_points)

    # tree = DecisionTree('20_21')
    # predicted_points = tree.train_model()
    # tree.choose_team_with_predicted_points(predicted_points)

    # randomForest = RandomForest('20_21')
    # predicted_points = randomForest.train_model()
    # randomForest.choose_team_with_predicted_points(predicted_points)

    # knn = KNN('20_21')
    # predicted_points = knn.train_model()
    # knn.choose_team_with_predicted_points(predicted_points)

    # linear_regression = LinearRegressionAI('20_21')
    # predicted_points = linear_regression.train_model()
    # linear_regression.choose_team_with_predicted_points(predicted_points)
#
    # tab_net = TabNet('20_21')
    # predicted_points = tab_net.train_model()
    # tab_net.choose_team_with_predicted_points(predicted_points)
