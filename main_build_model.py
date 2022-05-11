from building_model import BuildingModel

datasetName = "data.csv"

model = BuildingModel(datasetName)
model.trainingModelGaussianNB()
model.modelVerify(model.nb_predict_test)
model.confusionMatrix(model.nb_predict_test)

model.trainingModelRandomForest()
model.modelVerify(model.rf_predict_test)
model.confusionMatrix(model.rf_predict_test)

model.trainingModelLogisticRegression()
model.modelVerify(model.lr_predict_test)
model.confusionMatrix(model.lr_predict_test)

filename = 'best_model.sav'
model.savingModel(model.model_RandomForest, filename)