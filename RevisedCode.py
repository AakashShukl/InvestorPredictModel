# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 19:34:43 2018

@author: AAKASH
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as py

dataset=pd.read_csv("50_startups.csv")
X=dataset.iloc[:,:-1].values
y=dataset.iloc[:,4].values

#Categorical data
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelEncoder=LabelEncoder()
X[:,3]=labelEncoder.fit_transform(X[:,3])
onehotEncoder=OneHotEncoder(categorical_features=[3])
X=onehotEncoder.fit_transform(X).toarray()

X=X[:,1:]
#Splitting the dataset into test set and training set
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train,y_train)
y_pred=regressor.predict(X_test)

#Building the Optimal Model using Backward Elimination check for P<SL
import statsmodels.formula.api as sm 
X=np.append(arr=np.ones((50,1)).astype(int),values=X,axis=1)
X_opt=X[:,[0,1,2,3,4,5]]
regressor=sm.OLS(endog=y,exog=X_opt).fit()
regressor.summary()
X_opt=X[:,[0,3]]
regressor=sm.OLS(endog=y,exog=X_opt).fit()
y_statistical=regressor.predict(X_opt)