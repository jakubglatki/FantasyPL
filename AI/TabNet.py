import math

from numpy import reshape, asarray
from pytorch_tabnet.tab_model import TabNetRegressor
from sklearn.metrics import mean_squared_error

from AI.AIPrediction import AIPrediction


class TabNet(AIPrediction):

    def train_model(self):
        print("Tab net")
        X_train_normalized = self.X_train_normalized.to_numpy().copy()
        X_normalized = self.X_normalized.to_numpy().copy()
        y_train_normalized = self.y_train.to_numpy().reshape(-1, 1).copy()
        model = TabNetRegressor()
        model.fit(X_train_normalized, y_train_normalized)
        #self.calculate_RMSE(model, True)
        #self.make_plot('TabNet_'+self.season, model)
        all_data_predicted = model.predict(X_normalized)
        all_data_predicted = all_data_predicted.flatten()
        y_pred = model.predict(X_normalized)
        mse = mean_squared_error(self.y, y_pred)
        print("RMSE: " + str(math.sqrt(mse)))

        return all_data_predicted
