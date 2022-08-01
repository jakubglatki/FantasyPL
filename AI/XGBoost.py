import shap
from xgboost import XGBRegressor
from matplotlib import pyplot as plt

from AI.AIPrediction import AIPrediction


class XGBoost(AIPrediction):

    def train_model(self):
        # model = XGBRegressor().fit(X, y)
        print("XGBoost")
        model = XGBRegressor(missing=1)
        model.fit(self.X_train, self.y_train)
        self.calculate_RMSE(model, False)
        self.make_plot('XGBoost_'+self.season, model, False)
        all_data_predicted = model.predict(self.X)
        # shap.plots.waterfall(shap_values[0])
        return all_data_predicted
