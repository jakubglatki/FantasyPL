# This is a sample Python script.

from AI.AIPrediction import AIPrediction
from AI.DecisionTree import DecisionTree
from AI.KNN import KNN
from AI.LinearRegressionAI import LinearRegressionAI
from AI.RandomForest import RandomForest
from AI.TabNet import TabNet
from AI.XGBoost import XGBoost

if __name__ == '__main__':
    # print(utilities.get_player_parameter(234, utilities.import_data('players_raw_17_18.csv'), 'now_cost'))
    # players = basic_method_self_made.get_players_with_most_points()
    # for index, player in players.iterrows():
    #     print(utilities.get_player_parameter(player['id'], players, 'web_name'))
    #basic_method_self_made.choose_team()
    ai = AIPrediction()
    xgboost = XGBoost()
    predicted_points = xgboost.train_model()
    xgboost.choose_team_with_predicted_points(predicted_points)

    tree = DecisionTree()
    predicted_points = tree.train_model()
    tree.choose_team_with_predicted_points(predicted_points)

    randomForest = RandomForest()
    predicted_points = randomForest.train_model()
    randomForest.choose_team_with_predicted_points(predicted_points)

    knn = KNN()
    predicted_points = knn.train_model()
    knn.choose_team_with_predicted_points(predicted_points)

    linear_regression = LinearRegressionAI()
    predicted_points = linear_regression.train_model()
    linear_regression.choose_team_with_predicted_points(predicted_points)

    tab_net = TabNet()
    predicted_points = tab_net.train_model()
    tab_net.choose_team_with_predicted_points(predicted_points)
