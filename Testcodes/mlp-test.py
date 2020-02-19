import pandas as pd
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn import linear_model
from sklearn.model_selection import cross_validate
from sklearn.ensemble import RandomForestRegressor



# set up the data set frame and parameters
wine = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data",
                   names=["Cultivator", "Alchol", "Malic_Acid", "Ash", "Alcalinity_of_Ash", "Magnesium",
                          "Total_phenols", "Falvanoids", "Nonflavanoid_phenols", "Proanthocyanins", "Color_intensity",
                          "Hue", "OD280", "Proline"])
wine.head()
x = wine.drop('Cultivator', axis=1)
y = wine['Cultivator']

# Split train data set and test data set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4)

# Preprocessing
scaler = StandardScaler()
# Fit only to the training data
scaler.fit(x_train)
StandardScaler(copy=True, with_mean=True, with_std=True)
# Now apply the transformations to the data:
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

# Classifier
# Since we have a relative small size dataset, we use "lbfgs" as the solver option
#
mlp = MLPClassifier(hidden_layer_sizes=(13, 13, 13), max_iter=10000, activation="logistic", solver="lbfgs", alpha=1e-6)
mlp.fit(x_train, y_train)

# Predication
predictions = mlp.predict(x_test)
print(accuracy_score(y_test, predictions))
print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))
# Result is 0.9722222

# Cross-Validation
lig = sklearn.ensemble.RandomForestRegressor()
results = cross_validate(lig, x, y, cv=None)
print(results['test_score'])
print(np.mean(results['test_score']))
# Result is 0.3137052325934935

# Batch Normalization

