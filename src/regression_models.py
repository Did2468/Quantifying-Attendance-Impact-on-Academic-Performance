from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


def linear_regression(X,y):
    model=LinearRegression()
    model.fit(X,y)
    return model
def polynomial_regression(X,y,degree=2):
    poly=PolynomialFeatures(degree=degree)
    X_poly=poly.fit_transform(X)
    model=LinearRegression().fit(X_poly, y)
    return model, poly
