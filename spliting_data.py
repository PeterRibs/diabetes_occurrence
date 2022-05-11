from sklearn.model_selection import train_test_split
from dataset import Dataset

class SplitingData(Dataset):
    def __init__(self, datasetName):
        super().__init__(datasetName)
        self.attributes = ['Preg', 'Glu', 'BP', 'ST', 'Insulin', 'BMI', 'DPF', 'Age']
        self.predictAttribute = ['Outcome']
        self.X = self.df[self.attributes].values
        self.Y = self.df[self.predictAttribute].values
        self.X_training = None
        self.X_test= None
        self.Y_training = None
        self.Y_test = None

    def changeAtt(self, attList):
        self.attributes = attList
        self.X = self.df[self.attributes].values

    def changePredictAtt(self, predictAttList):
        self.predictAttribute = predictAttList
        self.Y = self.df[self.predictAttribute].values

    def splitTestData(self, splitTestSize = 0.3):
        self.X_training, self.X_test, self.Y_training, self.Y_test = train_test_split(self.X, self.Y, test_size = splitTestSize, random_state = 42)
        
    def splitSpecs(self):    
        print('\n# Split data sizes:')
        print("- Training data: {0:0.2f}%".format((len(self.X_training)/len(self.df.index)) * 100))
        print("- Test data: {0:0.2f}%".format((len(self.X_test)/len(self.df.index)) * 100))

    def allDataSizes(self):
        df = self.df
        print("\n# All Data Sizes:")
        print("Original True : {0} ({1:0.2f}%)".format(len(df.loc[df['Outcome'] == 1]), 
                                               (len(df.loc[df['Outcome'] ==1])/len(df.index) * 100)))

        print("Original False : {0} ({1:0.2f}%)".format(len(df.loc[df['Outcome'] == 0]), 
                                                    (len(df.loc[df['Outcome'] == 0])/len(df.index) * 100)))
        print("")
        print("Training True : {0} ({1:0.2f}%)".format(len(self.Y_training[self.Y_training[:] == 1]), 
                                                    (len(self.Y_training[self.Y_training[:] == 1])/len(self.Y_training) * 100)))

        print("Training False : {0} ({1:0.2f}%)".format(len(self.Y_training[self.Y_training[:] == 0]), 
                                                    (len(self.Y_training[self.Y_training[:] == 0])/len(self.Y_training) * 100)))
        print("")
        print("Test True : {0} ({1:0.2f}%)".format(len(self.Y_training[self.Y_training[:] == 1]), 
                                                    (len(self.Y_training[self.Y_training[:] == 1])/len(self.Y_training) * 100)))

        print("Test False : {0} ({1:0.2f}%)".format(len(self.Y_training[self.Y_training[:] == 0]), 
                                               (len(self.Y_training[self.Y_training[:] == 0])/len(self.Y_training) * 100)))


















