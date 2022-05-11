import pandas as pd

class Dataset():
    def __init__(self, datasetName):
        self.df = pd.read_csv(datasetName) 
        self.df = self.df.rename(columns = {"Pregnancies":"Preg", "Glucose":"Glu", "BloodPressure":"BP", "SkinThickness":"ST", "DiabetesPedigreeFunction":"DPF"})

    def dataSpecs(self):    
        print("\n# DataFrame shape:", self.df.shape)
        print("\n# DataFrame head:\n", self.df.head(5))
        print("\n# Describe:", self.df.describe())
        print("\n# Null:", self.df.isnull().values.any())

    def dataDistribution(self):
        num_true = len(self.df.loc[self.df['Outcome'] == True])
        num_false = len(self.df.loc[self.df['Outcome'] == False])
        print("\n# Data Distribution:")
        print("- Number of True case: {0} ({1:2.2f}%)".format(num_true, (num_true/ (num_true + num_false)) * 100))
        print("- Number of False case: {0} ({1:2.2f}%)".format(num_false, (num_false/ (num_true + num_false)) * 100))

    def hiddenMissingValues(self, value = 0):
        print('\n# Hidden Missing Values')
        print("# Dataframe rows: {0}".format(len(self.df)))
        print("# Pregnancies (Preg): {0}".format(len(self.df.loc[self.df['Preg'] == value])))
        print("# Missing row Glucose (Glu): {0}".format(len(self.df.loc[self.df['Glu'] == value])))
        print("# Missing row BloodPressure (BP): {0}".format(len(self.df.loc[self.df['BP'] == value])))
        print("# Missing row Thickness (ST): {0}".format(len(self.df.loc[self.df['ST'] == value])))
        print("# Missing row Insulin: {0}".format(len(self.df.loc[self.df['Insulin'] == value])))
        print("# Missing row BMI: {0}".format(len(self.df.loc[self.df['BMI'] == value])))
        print("# Missing row Age: {0}".format(len(self.df.loc[self.df['Age'] == value])))

