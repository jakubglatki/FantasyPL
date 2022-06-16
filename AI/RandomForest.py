from sklearn.ensemble import RandomForestRegressor

from AI.AIPrediction import AIPrediction


class RandomForest(AIPrediction):

    def train_model(self):
        model = RandomForestRegressor(n_estimators=1000, random_state=42)
        model.fit(self.X_train, self.y_train)
        self.calculate_RMSE(model)
        all_data_predicted = model.predict(self.X)
        return all_data_predicted
