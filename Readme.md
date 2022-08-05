
# Flight Dealy Predictor
When planning a trip, passengers should keep in mind that airlines do not guarantee their schedules. While airlines want to get passengers to their destinations on time, there are many things that can – and sometimes do – make it difficult for flights to arrive on time. Some problems, like bad weather, air traffic delays, and mechanical issues, are hard to predict and often beyond the airlines’ control. In this project we want predict the flight dealy.

## Understanding the Dataset
The dataset we are working on is a USA from 2013 and 2015. The dataset contains features 55 features like year, month, day.... The dataset contain both Numerical and Categorical dataset. This project we got different datasets of and we merged all the datasets and formed single dataset.

## Exploratory Data Analysis

In this Exploratory Data Analysis we started  basic exploring data whith shape of the dataset and info of dataset.


* Missing Values : Here we will check the percentage of nan values present in the in each features. There is a lot features contains nan values we have repleace this with meaningful which we will do in the Feature Engineering. 
* All The Numerical Variables:The dataset contains 39 Numerical Variables in that 16-Discrete variables and 21-Continuous features.   
* Outliers: We plot Box plot to see the outliers thers is more outliers we remove that in feature eangineering. 


## Feature Engineering
In feature engineering we treat the data that we seen in Exploratory Data Analysis
* Outlers:  In this process we used IQR method to remove outliers.
* Missing Values: In this proces we drop few columns containing 90% null values. After removing we used median method to fill Na values.

## Feature Selection
Feature selection we used Lasso and Selecteformmodel. In this setp we fit Independent features and got four fatures Scheduled_Time, Departure_Delay, Wheels_off and Elaspsed_Time are Independent features.

## Model Building

### Descion Tree Regressor
Decision tree regression observes features of an object and trains a model in the structure of a tree to predict data in the future to produce meaningful continuous output. Continuous output means that the output/result is not discrete, i.e., it is not represented just by a discrete, known set of numbers or values.

- Mean Absolute Error: 0.2782590113510548
- Mean Squared Error: 14.042787834325525
- Root Mean Squared Error: 3.7473707895437203

## Deployment
### Flask 
Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries.[2] It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions.

- The out will be ginven in minutes.
- The app runs on local host.
- To deplot it on the internet we have to deploy it on Heroku.

### Heroku
We deploy our Flask app to [Heroku.com][https://flightd.herokuapp.com/predict].

We prepared the needed files to deploy our app sucessfully:
- Procfile: Contains run statements for app file.
- requirements.txt: contains the libraries must be downloaded by Heroku to run app file.
- app.py: contains the python code for a Flask web app.
- model.pkl: contains our Descion Tree Regressor model that built by modeling part.








