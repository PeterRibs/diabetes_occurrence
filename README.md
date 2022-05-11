# Diabetes occurrence model

Using real dataset from the Machine Learning Repository from UCI / Kaggle (More information visite: 
`https://www.kaggle.com/uciml/pima-indians-diabetes-database/data`). The heatmap produced in order to check correlation between variables are in the 'Graphs' folder or 'https://peterribs.github.io/diabetes_occurrence/'.

There are 9 attributes in the dataset:
- Pregnancies (Preg) = Number of times pregnant.
- Glucose (Glu) = Plasma glucose concentration a 2 hours in an oral glucose tolerance test.
- BloodPressure (BP) = Diastolic blood pressure (mm Hg).
- SkinThickness (ST) = Triceps skin fold thickness (mm).
- Insulin = 2-Hour serum insulin (mu U/ml).
- BMI = Body mass index (weight in kg/(height in m)^2).
- DiabetesPedigreeFunction (DPF) = Diabetes pedigree function.
- Age = Age (years).
- Outcome = Class variable (0 or 1) 268 of 768 are 1 (Yes for Diabetes), the others are 0 (No Diabetes).

In order to answer the question, I tested 3 machine learning algorithms: Gaussian Naive Bayes, Random Forest and Logistic Regression. The best model was saved as `best_model.sav`.

## Question:

Can we predict with an accuracy of 75% whether a person will have diabetes?

## Technologies used:

- Python

## Used Python packages:

- matplotlib
- numpy
- pandas
- pickle
- seaborn
- sklearn

## Run

To run the project, use the `main_build_model.py` file to build the model and use the `main_prediction.py` to predict if someone will have diabetes using the model `best_model.sav`.