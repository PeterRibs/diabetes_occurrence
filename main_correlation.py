from correlation import Correlation

datasetName = "data.csv"
plotTitle = 'Correlation between variables\n'

a = Correlation(datasetName)
a.correlationPlot(plotTitle)