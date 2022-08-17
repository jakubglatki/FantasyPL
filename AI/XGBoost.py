import shap
from sklearn.model_selection import GridSearchCV
from xgboost import XGBRegressor
from matplotlib import pyplot as plt

from AI.AIPrediction import AIPrediction


class XGBoost(AIPrediction):
    model = 0
    rmse=0
    def train_model(self):
        # params = {'max_depth': [3, 6, 10],
        #           'learning_rate': [0.01, 0.05, 0.1],
        #           'n_estimators': [100, 500, 1000],
        #           'colsample_bytree': [0.3, 0.7]}
        # xgbr = XGBRegressor(seed=20)
        # clf = GridSearchCV(estimator=xgbr,
        #                    param_grid=params,
        #                    scoring='neg_mean_squared_error',
        #                    verbose=1)
        # clf.fit(self.X, self.y)
        # print("Best parameters:", clf.best_params_)
        # print("Lowest RMSE: ", (-clf.best_score_) ** (1 / 2.0))
        # model = XGBRegressor().fit(X, y)
        print("XGBoost")
        model = XGBRegressor(colsample_bytree=0.7, max_depth= 3, n_estimators= 500, learning_rate=0.1)# 'learning_rate': 0.01, 'max_depth': 3, 'n_estimators': 1000
        model.fit(self.X_train, self.y_train)
        self.rmse = self.calculate_RMSE(model, False)
        self.make_plot('XGBoost_'+self.season, model, False)
        self.model=model
        all_data_predicted = model.predict(self.X)
        # shap.plots.waterfall(shap_values[0])
        return all_data_predicted
