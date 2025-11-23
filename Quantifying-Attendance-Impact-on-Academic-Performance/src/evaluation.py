from sklearn.metrics import r2_score
import numpy as np


def evaluate(y_true,y_pred):
    r2score=r2_score(y_true,y_pred)
    return r2score
def correlation(x,y):
    return np.corrcoef(x,y)[0,1]
