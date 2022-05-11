from sklearn.impute import SimpleImputer

class HandlingMissingValues():
    def __init__(self, X_training, X_test, missingValue = 0, strategyUse = "mean"):    
        fillValues = SimpleImputer(missing_values = missingValue, strategy = strategyUse)
        X_training = fillValues.fit_transform(X_training)
        X_test = fillValues.fit_transform(X_test)
        print("\n# Training Data:")
        print(X_training)