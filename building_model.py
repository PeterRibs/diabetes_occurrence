import pickle
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

from handling_missing_values import HandlingMissingValues
from spliting_data import SplitingData

class BuildingModel(SplitingData):
    def __init__(self, datasetName):
        super().__init__(datasetName)
        self.splitTestData(0.3)
        self.allDataSizes()
        self.hiddenMissingValues()
        HandlingMissingValues(self.X_training, self.X_test)
        self.model_GaussianNB = None
        self.nb_predict_test = None
        self.model_RandomForest = None
        self.rf_predict_test = None
        self.model_LogisticRegression = None
        self.lr_predict_test = None

    def trainingModelGaussianNB(self):
        print("\n### Gaussian Naive Bayes ###")
        self.model_GaussianNB = GaussianNB()
        self.model_GaussianNB.fit(self.X_training, self.Y_training.ravel())
        self.nb_predict_test = self.model_GaussianNB.predict(self.X_test)

    def trainingModelRandomForest(self):
        print("\n### Random Forest ###")
        self.model_RandomForest = RandomForestClassifier(random_state = 42)
        self.model_RandomForest.fit(self.X_training, self.Y_training.ravel())
        self.rf_predict_test = self.model_RandomForest.predict(self.X_test)

    def trainingModelLogisticRegression(self):
        print("\n### Logistic Regression ###")
        self.model_LogisticRegression = LogisticRegression(C = 0.7, random_state = 42, max_iter = 1000)
        self.model_LogisticRegression.fit(self.X_training, self.Y_training.ravel())
        self.lr_predict_test = self.model_LogisticRegression.predict(self.X_test)

    def modelVerify(self, predict_test):
        if predict_test is None:
            print('You have to train the model first')
        else:
            print('\n# Model verification:')
            print("Accuracy: {0:.4f}".format(metrics.accuracy_score(self.Y_test, predict_test)))

    def confusionMatrix(self, predict_test):
        if predict_test is None:
            print('You have to train the model first')
        else:
            print("\n# Confusion Matrix:")

            print("{0}".format(metrics.confusion_matrix(self.Y_test, predict_test, labels = [1, 0])))

            print("\n# Classification Report")
            print(metrics.classification_report(self.Y_test, predict_test, labels = [1, 0]))

    def savingModel(self, model, filename):
        self.filename = filename
        pickle.dump(model, open(filename, 'wb'))


