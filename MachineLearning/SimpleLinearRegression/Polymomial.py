#coding:utf-8
'''
Created on 2015年5月25日

@author: Administrator
'''
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

X_train = [[6], [8], [10], [14], [18]]
y_train = [[7], [9], [13], [17.5], [18]]

X_test = [[6], [8], [11], [16]]
y_test = [[8], [12], [15], [18]]

regression = LinearRegression()
regression.fit(X_train, y_train)
xx = np.linspace(0, 26, 100)
yy = regression.predict(xx.reshape(xx.shape[0],1))

plt.plot(xx,yy)

#plt.show()


quadratic_featurizer = PolynomialFeatures(degree=2)

X_train_quadratic = quadratic_featurizer.fit_transform(X_train)

X_test_quadratic = quadratic_featurizer.transform(X_test)



















