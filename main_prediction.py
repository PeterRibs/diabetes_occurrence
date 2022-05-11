from prediction import Prediction

datasetName = "data.csv"
filename = 'best_model.sav'

row = 2

predict = Prediction(datasetName, filename)
predict.resultModel(predict.X_test[row])