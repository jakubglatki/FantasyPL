import math

import xgboost as xgb
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import shap
from shap.plots import *
from xgboost import XGBRegressor, XGBClassifier

import basic_method_self_made
import utilities


class AIPrediction:
    players = utilities.import_data('players_raw_17_18.csv')

    team_dictionary, team_limit_dictionary = utilities.map_teams()
    position_dictionary = utilities.map_positions()

    players_df = utilities.get_players_data_frame()

    X = players_df.drop('total_points', axis=1).copy()
    y = players_df['total_points'].copy()

    seed = 8
    test_size = 0.2
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=seed)


    def calculate_RMSE(self, model):
        y_pred_test = model.predict(self.X_test)
        y_pred_train = model.predict(self.X_train)
        mse_test = mean_squared_error(self.y_test, y_pred_test)
        mse_train = mean_squared_error(self.y_train, y_pred_train)
        print("RMSE_Test: " + str(math.sqrt(mse_test)))
        print("RMSE_Train: " + str(math.sqrt(mse_train)))

    def choose_team_with_predicted_points(self, all_data_predicted):
        self.X['total_points'] = all_data_predicted.tolist()
        players_predicted_df = utilities.get_players_data_frame_with_understandable_values(self.X, self.team_dictionary,
                                                                                           self.position_dictionary)
        most_points, cheapest_players, value_players = utilities.get_specific_data_frames(players_predicted_df)
        basic_method_self_made.choose_team(most_points, cheapest_players, value_players)


