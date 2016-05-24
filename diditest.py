# -*- coding: utf-8 -*-
"""
Created on Mon May 23 21:17:02 2016

@author: zhaoming
"""

import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor

if __name__ == '__main__':
    print 'start here~'
    boston_dataset = datasets.load_boston()
    X_full = boston_dataset.data
    Y = boston_dataset.target

    selector = SelectKBest(f_regression, k=1)
    selector.fit(X_full, Y)
    X = X_full[:, selector.get_support()]

    regressor = LinearRegression(normalize=True)
    regressor.fit(X, Y)
    plt.scatter(X, Y, color='black')
    plt.plot(X, regressor.predict(X), color='blue', linewidth=3)

    """
    regressor = SVR()
    regressor.fit(X, Y)
    plt.scatter(X, Y, color='black')
    plt.scatter(X, regressor.predict(X), color='blue', linewidth=3)
    """

    regressor = RandomForestRegressor()
    regressor.fit(X, Y)
    plt.scatter(X, Y, color='black');
    plt.scatter(X, regressor.predict(X), color='blue', linewidth=3)
    plt.show()

