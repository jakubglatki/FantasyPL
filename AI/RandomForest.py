import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV

from AI.AIPrediction import AIPrediction


class RandomForest(AIPrediction):

    def train_model(self):
        # # Number of trees in random forest
        # n_estimators = [int(x) for x in np.linspace(start=200, stop=2000, num=10)]
        # # Number of features to consider at every split
        # max_features = ['auto', 'sqrt']
        # # Maximum number of levels in tree
        # max_depth = [int(x) for x in np.linspace(10, 110, num=11)]
        # max_depth.append(None)
        # # Minimum number of samples required to split a node
        # min_samples_split = [2, 5, 10]
        # # Minimum number of samples required at each leaf node
        # min_samples_leaf = [1, 2, 4]
        # # Method of selecting samples for training each tree
        # bootstrap = [True, False]
        # random_grid = {'n_estimators': n_estimators,
        #                'max_features': max_features,
        #                'max_depth': max_depth,
        #                'min_samples_split': min_samples_split,
        #                'min_samples_leaf': min_samples_leaf,
        #                'bootstrap': bootstrap}
        # rf = RandomForestRegressor()
        #
        # rf_random = RandomizedSearchCV(estimator=rf, param_distributions=random_grid, n_iter=100, cv=3, verbose=2,
        #                                random_state=8, n_jobs=-1)
        # # Fit the random search model
        # rf_random.fit(self.X, self.y)
        # print(rf_random.best_params_)
        print("Random forest")
        model = RandomForestRegressor(n_estimators=1400, bootstrap=True, min_samples_split= 2, min_samples_leaf= 1, max_features='auto', max_depth= 110, random_state=8)
        model.fit(self.X_train, self.y_train)
        self.calculate_RMSE(model, False)
        #self.make_plot('RandomForest_'+self.season, model, False)
        all_data_predicted = model.predict(self.X)
        return all_data_predicted
