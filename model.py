import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import pickle
# Load the csv file
dataset = pd.read_csv('flight.csv')
# capture the dependent feature and independent feature
y=dataset['ARRIVAL_DELAY']
x=dataset.drop(['ARRIVAL_DELAY'],axis=1)
# Splitting the data into train and test
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)
# Instantiate the model
regressor = DecisionTreeRegressor()
# Fit the model
regressor.fit(x_train,y_train)
# Make pickle file of our model
pickle.dump(regressor, open("model.pkl","wb"))

