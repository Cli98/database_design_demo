import matplotlib.pyplot as plt
import numpy as np
from sklearn.svm import SVR
yesterday=np.load('raw_yesterday.npy')
today=np.load('raw_today.npy')
add=np.array([1710])
today=np.hstack((today,add))
combine=np.dstack((yesterday,today))
target=np.load('raw_yesterday.npy')

svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
y_rbf = svr_rbf.fit(combine, target).predict(combine)

