from tkinter import font
import matplotlib.pyplot as plt
import seaborn as sns

from dataset import Dataset

class Correlation(Dataset):
    def __init__(self, datasetName):
        super().__init__(datasetName)
        self.correlationDF = self.df.corr()

    def correlationPlot(self, plotTitle, size=20):
        plt.figure(figsize=(size, size))
        sns.set(font_scale = 1.5)
        ax = sns.heatmap(self.correlationDF, cmap='PuOr')
        ax.set_title(plotTitle, fontsize = 20)
        plt.show()

    def correlationMatrix(self):
        print("\n# Correlation Matrix:\n", self.correlationDF)
