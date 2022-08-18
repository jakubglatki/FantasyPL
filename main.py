import pandas as pd
from matplotlib import pyplot
import glob
import os

import Gameweeks_data_manipulation
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

    # seasons = ['17_18', '18_19', '19_20', '20_21']
    # for season in seasons:
    #      Gameweeks_data_manipulation.add_gameweeks_data(1, 1, season)
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
    # players = pd.read_csv('data/players_20_21.csv')
    # players2 = pd.read_csv('data/players_21_22.csv')
    # players = players.merge(players2, left_on=['first_name', 'second_name'],
    #                         right_on=['first_name_21_22', 'second_name_21_22'],
    #                         how='right')
    # players = players.drop(labels=['first_name', 'second_name'], axis=1)
    # players = players.rename(columns={'first_name_21_22': 'first_name', 'second_name_21_22': 'second_name'})
    # players.to_csv('data/players_21_22.csv', index=False)
    # players = pd.read_csv('data/players_21_22.csv')
    # players = pd.read_csv('data/players_16_17.csv')
    # players2 = pd.read_csv('data/gw1_16_17.csv')
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

    # xgboost = XGBoost('19_20')
    # predicted_points = xgboost.train_model()
    # xgboost.choose_team_with_predicted_points(predicted_points)

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
    tab_net = TabNet('20_21')
    predicted_points = tab_net.train_model()
    tab_net.choose_team_with_predicted_points(predicted_points)

String
text = "As visible in the Figure 5.3, models are varying stongly with their performence, in both metrics- RMSE and the number of points. There are some situations with the RMSE being low, "
+ "but the total number of points being relatively low as well. In most cases it is caused by correctly predicting most of the players, who did not get a lot of points, but failing at "
+ "predicting the positive outliers, the players with most points. Since the decision support system is supposed to help with choosing the best performing players,"
+ ", and not the average ones, the total number of points is a parameter which is more important in the decision making process, about choosing the best model."
+ "Another important metric in choosing the best model is the time when the model was making good predictions. The predictions made in the last two seasons,"
+ "when the models had more data to learn from are more important than the predictions from the beginning, with limited informations. "
+ "Is is expected, that the machine learning models would perform better with having more data, but as showed in this example it is not true for all of them,"
+ "especially the linear regression. Beside expected better performence with each season it would also be expected, that the algorithms will perform better during"
+ "the course of the season, having more game-weeks to learn from. Some of the algorithms, like linear regression or KNN are performing visibly worse during the course of the season,"
+ "being unable to correctly identify how the new data should affect the prediction. From the other checked models, the decision tree is consisntent in its results, but they are worse than"
+ "the best performing models. Random forest, after bad first season started to perform much better, but got worse results at the end of the course. In some places it also"
+ "got single, very bad results in the most point category, like with 1849 points after game-week 9 of the 19/20 season, or 1831 points after game-week 27 of the 20/21 season. "
+ "TabNet's behaviour is similar to the one of the random forest, getting bettere with time, having some problems during the last season, and having some bad outliers in performence,"
+ "like 1872 points after 36 game-weeks of the 18/19 season, or 1852 points after game-week 9 of the 19/20 season. After taking all that "
+ "into consideration, the XGBoost was chosen for the detailed case study, showned in the next section.";
