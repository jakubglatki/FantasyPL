import pandas as pd

import Gameweeks_data_manipulation
from AI.DecisionTree import DecisionTree
from AI.KNN import KNN
from AI.LinearRegressionAI import LinearRegressionAI
from AI.RandomForest import RandomForest
from AI.TabNet import TabNet
from AI.XGBoost import XGBoost

def check_all_algorithms(season):
    xgboost = XGBoost(season)
    predicted_points = xgboost.train_model()
    xgboost.choose_team_with_predicted_points(predicted_points)

    tree = DecisionTree(season)
    predicted_points = tree.train_model()
    tree.choose_team_with_predicted_points(predicted_points)

    randomForest = RandomForest(season)
    predicted_points = randomForest.train_model()
    randomForest.choose_team_with_predicted_points(predicted_points)

    knn = KNN(season)
    predicted_points = knn.train_model()
    knn.choose_team_with_predicted_points(predicted_points)

    linear_regression = LinearRegressionAI(season)
    predicted_points = linear_regression.train_model()
    linear_regression.choose_team_with_predicted_points(predicted_points)

    tab_net = TabNet(season)
    predicted_points = tab_net.train_model()
    tab_net.choose_team_with_predicted_points(predicted_points)

def compare_models():
    seasons = ['17_18', '18_19', '19_20', '20_21']
    gameweeks= [9,18,27,36]
    models=['linear_regression','knn','decision_tree','random_forest','XGBoost','TabNet']
    columns_names=[]
    first_gw=1
    for model in models:
        for season in seasons:
            for gameweek in gameweeks:
                columns_names.append(model+'_'+season+'_gw'+str(gameweek))

    df = pd.DataFrame(columns=columns_names, index=["RMSE", "Number of points"])
    # for season in seasons:
    #     first_gw=2
    #     for gameweek in gameweeks:
    #         xgboost = XGBoost(season)
    #         predicted_points = xgboost.train_model()
    #         points = xgboost.choose_team_with_predicted_points(predicted_points)
    #         rmse = xgboost.calculate_RMSE(xgboost.model, False)
    #         Gameweeks_data_manipulation.add_gameweeks_data(first_gw, gameweek, season)
    #         first_gw=gameweek
    #         d=3
    xd=4