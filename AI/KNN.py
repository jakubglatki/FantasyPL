from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor

from AI.AIPrediction import AIPrediction


class KNN(AIPrediction):

    def train_model(self):
        # leaf_size = list(range(1, 30))
        # n_neighbors = list(range(1, 20))
        # p = [1, 2]
        # hyperparameters = dict(leaf_size=leaf_size, n_neighbors=n_neighbors, p=p)
        #
        # # Create new KNN object
        # knn_2 = KNeighborsRegressor()
        # # Use GridSearch
        # clf = GridSearchCV(knn_2, hyperparameters, cv=10)
        # # Fit the model
        # best_model = clf.fit(self.X_normalized, self.y)
        # # Print The value of best Hyperparameters
        # print('Best leaf_size:', best_model.best_estimator_.get_params()['leaf_size'])
        # print('Best p:', best_model.best_estimator_.get_params()['p'])
        # print('Best n_neighbors:', best_model.best_estimator_.get_params()['n_neighbors'])
        print("KNN")
        model = KNeighborsRegressor(n_neighbors=5,leaf_size=1,p=2)
        model.fit(self.X_train_normalized, self.y_train)
        self.calculate_RMSE(model, True)
        #self.make_plot('KNN_'+self.season, model, True)
        all_data_predicted = model.predict(self.X_normalized)
        return all_data_predicted
