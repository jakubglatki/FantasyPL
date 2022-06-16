# This is a sample Python script.

from AI.AIPrediction import AIPrediction
from AI.XGBoost import XGBoost

if __name__ == '__main__':
    # print(utilities.get_player_parameter(234, utilities.import_data('players_raw_17_18.csv'), 'now_cost'))
    # players = basic_method_self_made.get_players_with_most_points()
    # for index, player in players.iterrows():
    #     print(utilities.get_player_parameter(player['id'], players, 'web_name'))
    #basic_method_self_made.choose_team()
    ai = AIPrediction()
    xgboost = XGBoost()
    predicted_points = xgboost.train_model_XGBoost()
    xgboost.choose_team_with_predicted_points(predicted_points)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
