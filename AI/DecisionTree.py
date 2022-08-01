import shap
from PIL import features
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from matplotlib import pyplot as plt

from AI.AIPrediction import AIPrediction


class DecisionTree(AIPrediction):

    def train_model(self):
        print("Decision Tree")
        model = DecisionTreeClassifier(random_state=8)
        model.fit(self.X_train, self.y_train)
        self.calculate_RMSE(model, False)
        #self.make_plot('DecisionTree_'+self.season, model, False)
        #shap.TreeExplainer(model)
        #plt.savefig('data/plots/DecisionTree_' + self.season, bbox_inches='tight', dpi=300)
        all_data_predicted = model.predict(self.X)
        return all_data_predicted
