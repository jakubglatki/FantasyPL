from PIL import features
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

from AI.AIPrediction import AIPrediction


class DecisionTree(AIPrediction):

    def train_model(self):
        model = DecisionTreeClassifier()
        model.fit(self.X_train, self.y_train)
        self.calculate_RMSE(model)
        all_data_predicted = model.predict(self.X)
        return all_data_predicted
