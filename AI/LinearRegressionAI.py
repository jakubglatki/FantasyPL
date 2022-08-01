from AI.AIPrediction import AIPrediction
from sklearn.linear_model import LinearRegression


class LinearRegressionAI(AIPrediction):

    def train_model(self):
        print("Linear regression")
        model = LinearRegression()
        model.fit(self.X_train_normalized, self.y_train)
        self.calculate_RMSE(model, True)
        #self.make_plot('LinearRegression_'+self.season, model, False)
        all_data_predicted = model.predict(self.X_normalized)
        return all_data_predicted
