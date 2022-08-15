import math

import pandas as pd
import xgboost as xgb
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import itertools
from matplotlib import pyplot as plt
import shap
from shap.plots import *
from xgboost import XGBRegressor, XGBClassifier

import basic_method_self_made
import utilities


class AIPrediction:
    def __init__(self, season):
        self.season = season
        self.players_df = pd.read_csv('data/' + season + '/players_gws.csv', encoding="ISO-8859-1")
        self.players_df = self.players_df.loc[~(self.players_df['total_points_' + season] == 0)]
        self.players_df = self.players_df.drop(labels=['first_name', 'second_name'], axis=1).copy()
        self.team_dictionary, self.team_limit_dictionary = utilities.map_teams()
        self.position_dictionary = utilities.map_positions()

        self.X = self.players_df.drop('total_points_' + season, axis=1).copy()
        self.y = self.players_df['total_points_' + season].copy()

        seed = 8
        test_size = 0.2
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=test_size,
                                                                                random_state=seed)

        regex_list = self.X.filter(regex='team_code') + self.X.filter(regex='element_type')
        self.X_normalized = self.X.drop(labels=regex_list, axis=1).copy()
        self.X_normalized.iloc[:, 0:-1] = self.X_normalized.iloc[:, 0:-1].apply(lambda x: (x - x.mean()) / x.std(),
                                                                                axis=0)
        self.X_normalized = self.X_normalized.fillna(0)

        self.X_train_normalized = self.X_train.drop(labels=regex_list, axis=1).copy()
        self.X_train_normalized.iloc[:, 0:-1] = self.X_train_normalized.iloc[:, 0:-1].apply(
            lambda x: (x - x.mean()) / x.std(),
            axis=0)
        self.X_train_normalized = self.X_train_normalized.fillna(0)

        self.X_test_normalized = self.X_test.drop(labels=regex_list, axis=1).copy()
        self.X_test_normalized.iloc[:, 0:-1] = self.X_test_normalized.iloc[:, 0:-1].apply(
            lambda x: (x - x.mean()) / x.std(),
            axis=0)
        self.X_test_normalized = self.X_test_normalized.fillna(0)

    def train_model(self):
        pass

    def calculate_RMSE(self, model, is_normalized):
        if is_normalized:
            test_data = self.X_test_normalized.copy()
            train_data = self.X_train_normalized.copy()
            pred_data = self.X_normalized.copy()
        else:
            test_data = self.X_test.copy()
            train_data = self.X_train.copy()
            pred_data = self.X.copy()
        y_pred_test = model.predict(test_data)
        y_pred_train = model.predict(train_data)
        y_pred = model.predict(pred_data)
        mse_test = mean_squared_error(self.y_test, y_pred_test)
        mse_train = mean_squared_error(self.y_train, y_pred_train)
        mse = mean_squared_error(self.y, y_pred)
        # print("RMSE_Test: " + str(math.sqrt(mse_test)))
        # print("RMSE_Train: " + str(math.sqrt(mse_train)))
        print("RMSE: " + str(math.sqrt(mse)))

    def choose_team_with_predicted_points(self, all_data_predicted):
        data_with_predicted_values = self.X.copy()
        data_with_predicted_values['total_points_' + self.season] = all_data_predicted.tolist()
        players_predicted_df = utilities.get_players_data_frame_with_understandable_values(data_with_predicted_values,
                                                                                           self.team_dictionary,
                                                                                           self.position_dictionary,
                                                                                           self.season)
        most_points, cheapest_players, value_players = utilities.get_specific_data_frames(players_predicted_df,
                                                                                          self.season)
        basic_method_self_made.choose_team(most_points, cheapest_players, value_players, self.season)

    def make_plot(self, plot_name, model, masker):
        if masker:
            data = self.X_normalized.copy()
            explainer = shap.Explainer(model, data)

            # explainer = shap.KernelExplainer(model.predict, data)
        else:
            data = self.X.copy()
            explainer = shap.Explainer(model)
        shap_values = explainer(data)
        shap.plots.waterfall(shap_values[0], show=False)
        plt.savefig('data/plots/' + plot_name, bbox_inches='tight', dpi=300)
