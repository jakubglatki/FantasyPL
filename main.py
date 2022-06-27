# This is a sample Python script.
import pandas as pd

import utilities

from AI.AIPrediction import AIPrediction
from AI.DecisionTree import DecisionTree
from AI.KNN import KNN
from AI.LinearRegressionAI import LinearRegressionAI
from AI.RandomForest import RandomForest
from AI.TabNet import TabNet
from AI.XGBoost import XGBoost

if __name__ == '__main__':
    # players = pd.read_csv('data/players_20_21.csv')
    # players2 = pd.read_csv('data/players_21_22.csv')
    # players = players.merge(players2, left_on=['first_name', 'second_name'],
    #                         right_on=['first_name_21_22', 'second_name_21_22'],
    #                         how='right')
    # players = players.drop(labels=['first_name', 'second_name'], axis=1)
    # players = players.rename(columns={'first_name_21_22': 'first_name', 'second_name_21_22': 'second_name'})
    # players.to_csv('data/players_21_22.csv', index=False)
    # players = pd.read_csv('data/players_21_22.csv')
    # wanted_features = utilities.wanted_features
    # column_list = []
    # for feature in wanted_features:
    #     for column in players.columns:
    #         if feature in column:
    #             column_list.append(column)
    # players = players[column_list]
    # players = players.add_suffix('_21_22')
    # players.to_csv('data/players_21_22.csv', index=False)
    # # basic_method_self_made.choose_team()
    # #ai = AIPrediction()
    xgboost = XGBoost('18_19')
    predicted_points = xgboost.train_model()
    xgboost.choose_team_with_predicted_points(predicted_points)

    # tree = DecisionTree()
    # predicted_points = tree.train_model()
    # tree.choose_team_with_predicted_points(predicted_points)
    #
    # randomForest = RandomForest()
    # predicted_points = randomForest.train_model()
    # randomForest.choose_team_with_predicted_points(predicted_points)
    #
    # knn = KNN()
    # predicted_points = knn.train_model()
    # knn.choose_team_with_predicted_points(predicted_points)
    #
    # linear_regression = LinearRegressionAI()
    # predicted_points = linear_regression.train_model()
    # linear_regression.choose_team_with_predicted_points(predicted_points)
    #
    # tab_net = TabNet()
    # predicted_points = tab_net.train_model()
    # tab_net.choose_team_with_predicted_points(predicted_points)
