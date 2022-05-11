import pickle
from spliting_data import SplitingData

class Prediction(SplitingData):
    def __init__(self, datasetName, filename):
        super().__init__(datasetName)
        self.splitTestData(0.3)
        self.filename = filename
        self.loaded_model = pickle.load(open(self.filename, 'rb'))

    def resultModel(self, dataRow):    
        result = self.loaded_model.predict(dataRow.reshape(1, -1))
        print("\n# The prediction for the data is:", result)