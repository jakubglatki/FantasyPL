from sklearn.neighbors import KNeighborsClassifier

from AI.AIPrediction import AIPrediction


class KNN(AIPrediction):

    def train_model(self):
        print("KNN")
        model = KNeighborsClassifier(n_neighbors=10)
        model.fit(self.X_train_normalized, self.y_train)
        self.calculate_RMSE(model, True)
        #self.make_plot('KNN_'+self.season, model, True)
        all_data_predicted = model.predict(self.X_normalized)
        return all_data_predicted
