from xgboost import XGBRegressor

from AI.AIPrediction import AIPrediction


class XGBoost(AIPrediction):

    def train_model(self):
        # model = XGBRegressor().fit(X, y)
        # explainer = shap.Explainer(model)
        # shap_values = explainer(X)
        #
        # shap.plots.bar(shap_values)
        # shap.plots.waterfall(shap_values[0])
        print("XGBoost")
        model = XGBRegressor(missing=1)
        model.fit(self.X_train, self.y_train)
        self.calculate_RMSE(model, False)
        all_data_predicted = model.predict(self.X)
        return all_data_predicted
